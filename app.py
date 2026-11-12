import json
import random
import time
import streamlit as st

st.set_page_config(
    page_title="CCIS V2 Practice Exam Simulator",
    page_icon="🛡️",
    layout="centered"
)

REAL_EXAM_QUESTIONS = 50
REAL_EXAM_DURATION_SEC = 110 * 60  # 1 hr 50 min per CCIS V2 Exam Guide
REAL_EXAM_PASS_PCT = 70.0          # 70% to pass per CCIS V2 Exam Guide

@st.cache_data
def load_questions(filepath="questions.json"):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def init_session():
    defaults = {
        "quiz_started": False,
        "exam_mode": "custom",  # "custom" or "real_exam"
        "quiz_questions": [],
        "current_idx": 0,
        "answers": {},
        "submitted": {},
        "show_hint": {},
        "start_time": None,
        "scored_early": False,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

def reset_to_home():
    st.session_state.quiz_started = False
    st.session_state.exam_mode = "custom"
    st.session_state.quiz_questions = []
    st.session_state.current_idx = 0
    st.session_state.answers = {}
    st.session_state.submitted = {}
    st.session_state.show_hint = {}
    st.session_state.start_time = None
    st.session_state.scored_early = False

def start_custom_quiz(all_questions, num_questions, selected_chapters):
    filtered = [q for q in all_questions if q.get("chapter", q["topic"]) in selected_chapters]
    count = min(num_questions, len(filtered))
    st.session_state.quiz_questions = random.sample(filtered, count)
    st.session_state.exam_mode = "custom"
    st.session_state.current_idx = 0
    st.session_state.answers = {}
    st.session_state.submitted = {}
    st.session_state.show_hint = {}
    st.session_state.start_time = time.time()
    st.session_state.scored_early = False
    st.session_state.quiz_started = True

def start_real_exam_simulation(all_questions):
    """
    Simulates the official CCIS V2 proctored exam:
    - 50 total questions
    - ~15% AI-focused questions (8 questions) across AI Threats, Governance, and Silent AI
    - Balanced distribution across all 10 CCIS V2 syllabus chapters
    """
    ai_pool = [q for q in all_questions if q.get("is_ai", False)]
    non_ai_pool = [q for q in all_questions if not q.get("is_ai", False)]

    target_ai = min(8, len(ai_pool))  # ~15% of 50 = 7.5 -> 8 questions
    target_non_ai = REAL_EXAM_QUESTIONS - target_ai

    selected = []
    selected.extend(random.sample(ai_pool, target_ai))

    # Stratify non-AI questions evenly across chapters for realistic blueprint coverage
    chapters = sorted(list({q.get("chapter", q["topic"]) for q in non_ai_pool}))
    by_chapter = {
        ch: [q for q in non_ai_pool if q.get("chapter", q["topic"]) == ch]
        for ch in chapters
    }

    per_ch = max(1, target_non_ai // len(chapters))
    for ch in chapters:
        pool = by_chapter[ch]
        take = min(per_ch, len(pool))
        selected.extend(random.sample(pool, take))

    # Top up remaining slots randomly from unused non-AI questions
    selected_ids = {q["id"] for q in selected}
    remaining_pool = [q for q in non_ai_pool if q["id"] not in selected_ids]
    needed = REAL_EXAM_QUESTIONS - len(selected)
    if needed > 0 and remaining_pool:
        selected.extend(random.sample(remaining_pool, min(needed, len(remaining_pool))))

    selected = selected[:REAL_EXAM_QUESTIONS]
    random.shuffle(selected)

    st.session_state.quiz_questions = selected
    st.session_state.exam_mode = "real_exam"
    st.session_state.current_idx = 0
    st.session_state.answers = {}
    st.session_state.submitted = {}
    st.session_state.show_hint = {}
    st.session_state.start_time = time.time()
    st.session_state.scored_early = False
    st.session_state.quiz_started = True

def main():
    init_session()

    try:
        all_questions = load_questions()
    except FileNotFoundError:
        st.error("`questions.json` not found. Run `python generate_bank.py` first to build the question bank.")
        st.stop()

    all_chapters = sorted(list({q.get("chapter", q["topic"]) for q in all_questions}))

    with st.sidebar:
        st.header("🎯 Exam Simulation")
        st.caption("Official Format: **50 Qs** • **1h 50m** • **70% Pass** • **~15% AI**")
        if st.button("🎓 Simulate Real Test (50 Qs)", use_container_width=True, type="primary"):
            start_real_exam_simulation(all_questions)
            st.rerun()

        st.divider()
        st.header("⚙️ Custom Practice Settings")
        st.caption(f"Question Bank: **{len(all_questions):,}** unique questions")

        selected_chapters = st.multiselect(
            "Filter by CCIS V2 Syllabus Chapter",
            options=all_chapters,
            default=all_chapters
        )

        available_count = len([q for q in all_questions if q.get("chapter", q["topic"]) in selected_chapters])
        max_q = max(1, available_count)
        default_q = min(20, max_q)

        num_questions = st.number_input(
            "Number of Questions",
            min_value=1,
            max_value=max_q,
            value=default_q,
            step=1,
            help="Select how many questions you want in a custom practice session."
        )

        if st.button("🚀 Start Custom Quiz", use_container_width=True):
            if not selected_chapters:
                st.warning("Please select at least one syllabus chapter.")
            else:
                start_custom_quiz(all_questions, num_questions, selected_chapters)
                st.rerun()

        if st.session_state.quiz_started:
            st.divider()
            if st.button("🔄 Start Over", use_container_width=True):
                reset_to_home()
                st.rerun()

    st.title("🛡️ CCIS V2 Certification Practice Simulator")
    st.markdown("Certified Cyber Insurance Specialist • Cyber & AI Risk Assessment")

    if not st.session_state.quiz_started:
        st.info(
            "Click **Simulate Real Test (50 Qs)** in the sidebar for a full blueprint exam "
            "(50 questions, ~15% AI coverage, 1h 50m timer, 70% passing score), or configure a **Custom Quiz**."
        )
        st.stop()

    questions = st.session_state.quiz_questions
    total_q = len(questions)
    idx = st.session_state.current_idx
    is_real_exam = st.session_state.exam_mode == "real_exam"

    # Check timer expiration in Real Exam mode
    time_expired = False
    if is_real_exam and st.session_state.start_time is not None:
        elapsed = time.time() - st.session_state.start_time
        remaining = max(0, int(REAL_EXAM_DURATION_SEC - elapsed))
        if remaining == 0:
            time_expired = True
        else:
            mins, secs = divmod(remaining, 60)
            hrs, mins = divmod(mins, 60)
            st.caption(f"⏱️ **Real Exam Mode** • Time Remaining: **{hrs:02d}:{mins:02d}:{secs:02d}**")

    # --- RESULTS / SCORECARD VIEW ---
    if idx >= total_q or st.session_state.scored_early or time_expired:
        if time_expired:
            st.warning("⏰ Time has expired! Your exam has been automatically scored.")

        correct_count = sum(
            1 for i, q in enumerate(questions)
            if st.session_state.answers.get(i) == q["correct_index"]
        )
        answered_count = len(st.session_state.answers)
        score_pct = (correct_count / total_q) * 100
        pass_mark = REAL_EXAM_PASS_PCT if is_real_exam else 70.0
        passed = score_pct >= pass_mark

        if passed:
            st.success(f"### 🎉 Exam Complete — PASS ({score_pct:.1f}%)")
        else:
            st.error(f"### 📚 Exam Complete — REVIEW NEEDED ({score_pct:.1f}%)")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Final Score", f"{score_pct:.1f}%")
        col2.metric("Correct", f"{correct_count} / {total_q}")
        col3.metric("Answered", f"{answered_count} / {total_q}")
        col4.metric("Pass Threshold", f"{pass_mark:.0f}%")

        # Domain/Chapter Breakdown
        st.subheader("📊 Performance by Syllabus Chapter")
        chapter_stats = {}
        for i, q in enumerate(questions):
            ch = q.get("chapter", q["topic"])
            chapter_stats.setdefault(ch, [0, 0])
            chapter_stats[ch][1] += 1
            if st.session_state.answers.get(i) == q["correct_index"]:
                chapter_stats[ch][0] += 1

        for ch, (c_ok, c_tot) in sorted(chapter_stats.items()):
            pct = (c_ok / c_tot) * 100
            st.write(f"- **{ch}:** {c_ok}/{c_tot} ({pct:.0f}%)")

        st.divider()
        st.subheader("📋 Question-by-Question Review")
        for i, q in enumerate(questions):
            user_ans = st.session_state.answers.get(i)
            is_correct = user_ans == q["correct_index"]
            icon = "✅" if is_correct else "❌"
            ai_badge = " 🤖 [AI]" if q.get("is_ai") else ""
            with st.expander(f"{icon} Question {i+1}: {q.get('chapter', q['topic'])}{ai_badge}"):
                st.write(q["question"])
                st.write(f"**Your Answer:** {q['options'][user_ans] if user_ans is not None else 'Unanswered / Skipped'}")
                st.write(f"**Correct Answer:** {q['options'][q['correct_index']]}")
                st.info(f"**Explanation:** {q['explanation']}")

        col_restart1, col_restart2 = st.columns(2)
        with col_restart1:
            if st.button("🎓 Simulate Another Real Test", type="primary", use_container_width=True):
                start_real_exam_simulation(all_questions)
                st.rerun()
        with col_restart2:
            if st.button("🔄 Start Over (Setup Screen)", use_container_width=True):
                reset_to_home()
                st.rerun()
        st.stop()

    # --- ACTIVE QUESTION VIEW ---
    q = questions[idx]
    chapter_label = q.get("chapter", q["topic"])
    ai_tag = " • 🤖 AI Focus" if q.get("is_ai") else ""
    st.progress((idx + 1) / total_q, text=f"Question {idx + 1} of {total_q} • **{chapter_label}**{ai_tag}")

    st.subheader(q["question"])

    # Hint button (hidden in Real Exam mode to mirror proctored conditions)
    if not is_real_exam:
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
        disabled=is_submitted and not is_real_exam,
        key=f"radio_{idx}"
    )

    # In Real Exam mode, save selection immediately so users can navigate freely before scoring
    if is_real_exam and choice is not None:
        st.session_state.answers[idx] = choice

    # Navigation & Action Buttons
    col_primary, col_prev, col_next = st.columns(3)

    with col_primary:
        if is_real_exam:
            if st.button("➡️ Save & Next", type="primary", use_container_width=True, disabled=(idx == total_q - 1)):
                st.session_state.current_idx += 1
                st.rerun()
        else:
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
        if is_real_exam:
            if idx == total_q - 1:
                if st.button("🏁 Submit Exam", type="primary", use_container_width=True):
                    st.session_state.scored_early = True
                    st.rerun()
        else:
            next_label = "Finish Quiz 🏁" if idx == total_q - 1 else "Next ➡️"
            if st.button(next_label, use_container_width=True, disabled=not is_submitted):
                st.session_state.current_idx += 1
                st.rerun()

    # Immediate Feedback in Custom Practice Mode
    if not is_real_exam and is_submitted:
        st.divider()
        if choice == q["correct_index"]:
            st.success(f"**Correct!** {q['explanation']}")
        else:
            st.error(f"**Incorrect.** The correct answer is: **{q['options'][q['correct_index']]}**")
            st.info(f"**Explanation:** {q['explanation']}")

    # Persistent Bottom Controls: Score Now & Start Over
    st.divider()
    col_score, col_reset = st.columns(2)
    with col_score:
        if st.button("📊 Score Now", use_container_width=True, help="End the session immediately and calculate your score."):
            if choice is not None and idx not in st.session_state.answers:
                st.session_state.answers[idx] = choice
            st.session_state.scored_early = True
            st.rerun()
    with col_reset:
        if st.button("🔄 Start Over", use_container_width=True, help="Abandon this session and return to setup."):
            reset_to_home()
            st.rerun()

if __name__ == "__main__":
    main()
