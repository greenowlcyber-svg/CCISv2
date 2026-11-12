import json
import random

SEED_QUESTIONS = [
    {
        "topic": "Data Privacy Regulations",
        "question": "Under the California Consumer Privacy Act (CCPA) as amended by the CPRA, which right gives consumers the ability to restrict the use and disclosure of their Sensitive Personal Information?",
        "options": [
            "The right to limit the use and disclosure of sensitive personal information to what is necessary to perform the services",
            "An unconditional opt-in right to sell personal data to third parties regardless of age",
            "The right to demand absolute data deletion from all global backups without exception",
            "The right to cross-industry data portability in proprietary enterprise formats"
        ],
        "correct_index": 0,
        "explanation": "The CPRA introduced a distinct right for consumers to direct businesses to limit the use and disclosure of sensitive personal information (such as SSNs, financial data, or health info) to permitted purposes.",
        "hint": "Think about the expanded tier of personal data introduced by the CPRA that goes beyond basic identifiers."
    },
    {
        "topic": "Network Defense & Underwriting",
        "question": "Why is Multi-Factor Authentication (MFA) applied to remote access (RDP, VPN) and corporate email considered a baseline critical control during cyber underwriting?",
        "options": [
            "It drastically mitigates the primary entry vectors used by threat actors for initial access and credential compromise",
            "It completely eliminates the possibility of social engineering and phishing attacks against employees",
            "It stops all types of ransomware from executing on local endpoint devices once an infection occurs",
            "It permanently replaces the need for network firewalls, segmentation, and endpoint detection tools"
        ],
        "correct_index": 0,
        "explanation": "Compromised credentials and exposed remote access services represent the vast majority of initial intrusion paths into corporate networks.",
        "hint": "Consider the most common initial access points that threat actors exploit to gain an initial foothold."
    },
    {
        "topic": "AI Exposure",
        "question": "Which of the following best describes 'data poisoning' as an AI-related cyber exposure?",
        "options": [
            "Manipulating or injecting malicious data into a machine learning training dataset to introduce vulnerabilities, biases, or backdoors",
            "Exfiltrating proprietary source code from a machine learning repository",
            "Failing to encrypt personally identifiable information stored in a cloud database",
            "Using unauthorized synthetic media or deepfakes to conduct spear-phishing campaigns"
        ],
        "correct_index": 0,
        "explanation": "Data poisoning occurs during the training phase where an adversary corrupts input data to alter the behavior or integrity of the resulting AI model.",
        "hint": "Focus on the phase before model deployment—specifically how an adversary corrupts training inputs."
    },
    {
        "topic": "Silent AI",
        "question": "What does the term 'silent AI' refer to in commercial insurance and risk management?",
        "options": [
            "Potential, unquantified insurance losses arising from AI-related liabilities embedded within traditional, non-cyber policies not designed to cover AI risks",
            "AI systems that operate without generating system log files, audit trails, or telemetry",
            "Losses caused by AI models that permanently stop responding due to hardware or power failures",
            "Mandatory confidentiality clauses in vendor agreements regarding algorithmic failures"
        ],
        "correct_index": 0,
        "explanation": "Analogous to 'silent cyber,' silent AI refers to unmodeled AI exposures lurking inside traditional property, casualty, or general liability policies.",
        "hint": "Compare it to the well-known insurance concept of 'silent cyber.'"
    },
    {
        "topic": "First-Party Cyber Coverage",
        "question": "Which first-party cyber insurance insuring agreement responds to lost business income and extra expenses incurred when a critical cloud service provider (CSP) suffers a cyber outage?",
        "options": [
            "Contingent Business Interruption (CBI) Coverage",
            "Cyber Extortion and Ransomware Response Coverage",
            "Media and Intellectual Property Liability Coverage",
            "Regulatory Fines and Penalties Coverage"
        ],
        "correct_index": 0,
        "explanation": "Contingent Business Interruption (also called dependent business interruption) covers income losses when a third-party IT vendor or cloud provider experiences a cyber event.",
        "hint": "Look for the term denoting business interruption caused by a third-party dependency."
    },
    {
        "topic": "Third-Party Cyber Coverage",
        "question": "Network Security and Privacy Liability (third-party) coverage typically protects the insured against which scenario?",
        "options": [
            "Claims brought by customers, business partners, or regulatory bodies alleging financial injury or privacy violations resulting from a data breach or security failure",
            "The cost of hiring a public relations firm to repair brand reputation after a minor internal IT glitch",
            "The direct ransom demand paid to a threat actor to decrypt internal corporate operational files",
            "The physical replacement cost of server hardware damaged during an electrical power surge"
        ],
        "correct_index": 0,
        "explanation": "Third-party liability coverage indemnifies the insured against legal liability, settlements, and defense costs arising from lawsuits or claims made by external parties.",
        "hint": "Distinguish between claims made against your organization by external parties versus direct internal costs."
    },
    {
        "topic": "Policy Anatomy & Exclusions",
        "question": "How have modern cyber insurance policies evolved in response to state-sponsored cyberattacks and war exclusions?",
        "options": [
            "They utilize updated war exclusion models featuring formal attribution standards, burden-of-proof requirements, and carve-backs for non-state actors",
            "They provide unconditional, full-limit coverage for all geopolitical and military cyber operations worldwide",
            "They completely exclude all cyber incidents of any kind once a national emergency is declared",
            "They automatically transfer any war-related cyber claim to standard commercial general liability policies"
        ],
        "correct_index": 0,
        "explanation": "Following market-wide updates such as Lloyd's principles, cyber policies require clear attribution standards and carve back coverage for cyberattacks conducted by non-state actors.",
        "hint": "Think about market shifts following major attribution debates like NotPetya."
    },
    {
        "topic": "Ransomware Handling & Extortion",
        "question": "Under a Cyber Extortion insuring agreement, why must an insurer or policyholder screen a ransom payment destination against OFAC sanctions lists before disbursing funds?",
        "options": [
            "To avoid severe civil and criminal penalties for illegal financial transactions with sanctioned entities, rogue nation-states, or designated terrorist groups",
            "To verify that the decryption key provided by the threat actor is technically functional",
            "To ensure the ransom amount does not exceed the policy’s aggregate limit",
            "To automatically trigger federal law enforcement attribution and military retaliation"
        ],
        "correct_index": 0,
        "explanation": "Remitting payment to a threat actor linked to a sanctioned entity violates U.S. federal law and carries strict liability penalties under OFAC regulations.",
        "hint": "Consider regulatory compliance obligations regarding financial dealings with blocked persons."
    },
    {
        "topic": "Underwriting",
        "question": "When a cyber underwriter requires evidence of 'immutable backups' during a risk assessment, what key security property are they verifying?",
        "options": [
            "Backups that are protected from being altered, deleted, or encrypted by ransomware even if an attacker gains administrative domain credentials",
            "Backups that are compressed and stored on a single local administrative workstation",
            "Backups that are updated only once every calendar year for compliance auditing",
            "Backups that are stored exclusively on public-facing social media repositories"
        ],
        "correct_index": 0,
        "explanation": "Immutable backups (often WORM-enabled or air-gapped) cannot be modified or encrypted by threat actors who compromise domain admin accounts.",
        "hint": "The word 'immutable' means unchangeable or read-only once written."
    },
    {
        "topic": "Claims Processes",
        "question": "What is the primary purpose of the 'cooperation clause' and 'panel vendor' requirement in a cyber insurance policy's claims conditions?",
        "options": [
            "To ensure that specialized, pre-vetted incident response, legal, and forensics experts manage the breach efficiently and control escalating claims costs",
            "To force the insured to represent themselves in court without legal counsel",
            "To allow the insurance company to take full operational ownership of the company's daily IT department permanently",
            "To waive the policy deductible entirely if the breach is reported within 24 hours"
        ],
        "correct_index": 0,
        "explanation": "Panel vendors (breach coaches, forensics firms, PR agencies) ensure rapid, compliant handling while cooperation clauses prevent the insured from prejudicing the claim.",
        "hint": "Think about why insurers insist on approved breach coaches rather than arbitrary vendors."
    }
]

SCENARIO_CONTEXTS = [
    "a mid-sized healthcare provider",
    "a global manufacturing enterprise",
    "a regional financial institution",
    "a cloud-native SaaS vendor",
    "an e-commerce retail corporation",
    "a municipal utility operator",
    "a multinational logistics firm",
    "a legal services partnership",
    "a higher education institution",
    "a technology consulting agency"
]

def build_1000_questions(output_file="questions.json"):
    bank = []
    for i in range(1000):
        base = SEED_QUESTIONS[i % len(SEED_QUESTIONS)]
        context = SCENARIO_CONTEXTS[(i // len(SEED_QUESTIONS)) % len(SCENARIO_CONTEXTS)]
        
        indexed_options = list(enumerate(base["options"]))
        rng = random.Random(i + 42)
        rng.shuffle(indexed_options)
        
        shuffled_texts = [opt_text for _, opt_text in indexed_options]
        new_correct_idx = next(idx for idx, (orig_idx, _) in enumerate(indexed_options) if orig_idx == base["correct_index"])
        
        bank.append({
            "id": i + 1,
            "topic": base["topic"],
            "question": f"[Q{i+1} • Context: {context.capitalize()}] {base['question']}",
            "options": shuffled_texts,
            "correct_index": new_correct_idx,
            "explanation": base["explanation"],
            "hint": base["hint"]
        })
        
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(bank, f, indent=2)
    print(f"Successfully generated {len(bank)} questions in '{output_file}'.")

if __name__ == "__main__":
    build_1000_questions()
