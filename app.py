import json
import random
import streamlit as st

st.set_page_config(
    page_title="CCIS V2 Practice Exam Simulator",
    page_icon="🛡️",
    layout="centered"
)

@st.cache_data
def load_questions(filepath="questions.json"):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def init_session():
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
    if "quiz_questions" not in st.session_state:
        st.session_state.quiz_questions = []
    if "current_idx" not in st.session_state:
        st.session_state.current_idx = 0
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "submitted" not in st.session_state:
        st.session_state.submitted = {}
    if "show_hint" not in st.session_state:
        st.session_state.show_hint = {}

def start_new_quiz(all_questions, num_questions, selected_topics):
    filtered = [q for q in all_questions if q["topic"] in selected_topics]
    count = min(num_questions, len(filtered))
    st.session_state.quiz_questions = random.sample(filtered, count)
    st.session_state.current_idx = 0
    st.session_state.answers = {}
    st.session_state.submitted = {}
    st.session_state.show_hint = {}
    st.session_state.quiz_started = True

def main():
    init_session()
    
    try:
        all_questions = load_questions()
    except FileNotFoundError:
        st.error("`questions.json` not found. Ensure `questions.json` is in the same directory or run `python generate_bank.py` first.")
        st.stop()

    all_topics = sorted(list({q["topic"] for q in all_questions}))

    with st.sidebar:
        st.header("⚙️ Quiz Settings")
        st.caption(f"Total Bank Size: **{len(all_questions):,}** questions")
        
        selected_topics = st.multiselect(
            "Filter by CCIS V2 Domain",
            options=all_topics,
            default=all_topics
        )
        
        available_count = len([q for q in all_questions if q["topic"] in selected_topics])
        max_q = max(1, available_count)
        default_q = min(20, max_q)
        
        num_questions = st.number_input(
            "Number of Questions",
            min_value=1,
            max_value=max_q,
            value=default_q,
            step=1,
            help="Select how many questions you want in this session (defaults to 20)."
        )
        
        if st.button("🚀 Start / Reset Quiz", use_container_width=True, type="primary"):
            if not selected_topics:
                st.warning("Please select at least one topic.")
            else:
                start_new_quiz(all_questions, num_questions, selected_topics)
                st.rerun()

    st.title("🛡️ CCIS V2 Certification Practice Quiz")
    st.markdown("Certified Cyber Insurance Specialist • Interactive Exam Simulator")

    if not st.session_state.quiz_started:
        st.info(
            "Configure your quiz length (default: **20 questions**) and topic filters in the sidebar, "
            "then click **Start / Reset Quiz** to begin."
        )
        st.stop()

    questions = st.session_state.quiz_questions
    total_q = len(questions)
    idx = st.session_state.current_idx

    if idx >= total_q:
        correct_count = sum(
            1 for i, q in enumerate(questions)
            if st.session_state.answers.get(i) == q["correct_index"]
        )
        score_pct = (correct_count / total_q) * 100

        st.success("### 🎉 Quiz Complete!")
        col1, col2, col3 = st.columns(3)
        col1.metric("Score", f"{score_pct:.1f}%")
        col2.metric("Correct", f"{correct_count} / {total_q}")
        col3.metric("Status", "PASS" if score_pct >= 75 else "REVIEW")

        st.divider()
        st.subheader("📋 Question-by-Question Review")
        for i, q in enumerate(questions):
            user_ans = st.session_state.answers.get(i)
            is_correct = user_ans == q["correct_index"]
            icon = "✅" if is_correct else "❌"
            with st.expander(f"{icon} Question {i+1}: {q['topic']}"):
                st.write(q["question"])
                st.write(f"**Your Answer:** {q['options'][user_ans] if user_ans is not None else 'Skipped'}")
                st.write(f"**Correct Answer:** {q['options'][q['correct_index']]}")
                st.info(f"**Explanation:** {q['explanation']}")

        if st.button("🔄 Take Another Quiz", type="primary"):
            start_new_quiz(all_questions, num_questions, selected_topics)
            st.rerun()
        st.stop()

    q = questions[idx]
    st.progress((idx + 1) / total_q, text=f"Question {idx + 1} of {total_q} • Domain: **{q['topic']}**")

    st.subheader(q["question"])

    if st.button("💡 Need a Hint?", key=f"hint_btn_{idx}"):
        st.session_state.show_hint[idx] = not st.session_state.show_hint.get(idx, False)
    if st.session_state.show_hint.get(idx, False):
        st.warning(f"**Hint:** {q['hint']}")

    is_submitted = st.session_state.submitted.get(idx, False)
    previous_choice = st.session_state.answers.get(idx, None)

    choice = st.radio(
        "Select one answer:",
        options=list(range(len(q["options"]))),
        format_func=lambda x: q["options"][x],
        index=previous_choice,
        disabled=is_submitted,
        key=f"radio_{idx}"
    )

    col_submit, col_prev, col_next = st.columns(3)

    with col_submit:
        if not is_submitted:
            if st.button("Check Answer", type="primary", use_container_width=True):
                if choice is None:
                    st.warning("Please select an option before submitting.")
                else:
                    st.session_state.answers[idx] = choice
                    st.session_state.submitted[idx] = True
                    st.rerun()

    with col_prev:
        if idx > 0:
            if st.button("⬅️ Previous", use_container_width=True):
                st.session_state.current_idx -= 1
                st.rerun()

    with col_next:
        next_label = "Finish Quiz 🏁" if idx == total_q - 1 else "Next ➡️"
        if st.button(next_label, use_container_width=True, disabled=not is_submitted):
            st.session_state.current_idx += 1
            st.rerun()

    if is_submitted:
        st.divider()
        if choice == q["correct_index"]:
            st.success(f"**Correct!** {q['explanation']}")
        else:
            st.error(f"**Incorrect.** The correct answer is: **{q['options'][q['correct_index']]}**")
            st.info(f"**Explanation:** {q['explanation']}")

if __name__ == "__main__":
    main()
