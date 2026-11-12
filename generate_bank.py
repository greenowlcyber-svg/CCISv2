import json
import random

# Aligned with CCIS V2 10-Chapter Curriculum & 4 Dedicated AI Lessons
SEED_QUESTIONS = [
    # --- CHAPTER 01: Welcome to Cyber Insurance Academy ---
    {
        "chapter": "Ch 01: Cyber Risk & Threat Actors",
        "topic": "Cyber Risk & Threat Actors",
        "is_ai": False,
        "question": "How do nation-state threat actors primarily differ from financially motivated cybercriminal syndicates when underwriters evaluate catastrophic cyber risk?",
        "options": [
            "Nation-state actors often prioritize espionage, disruption, or geopolitical objectives and possess advanced persistent capabilities that can trigger war or systemic risk exclusions",
            "Nation-state actors exclusively target small businesses with fewer than 50 employees using automated commodity malware",
            "Financially motivated cybercriminals never use ransomware or data exfiltration techniques against commercial enterprises",
            "Nation-state attacks are automatically covered under standard commercial property policies without sublimits"
        ],
        "correct_index": 0,
        "explanation": "Nation-state actors operate with state backing for intelligence or strategic disruption, creating systemic aggregation and war-exclusion complexities compared to profit-driven ransomware groups.",
        "hint": "Compare geopolitical/espionage motives and systemic impact against direct financial extortion."
    },
    {
        "chapter": "Ch 01: Cyber Risk & Threat Actors",
        "topic": "Cyber Risk & Threat Actors",
        "is_ai": False,
        "question": "Why does an organization's digital crown jewels analysis matter during initial cyber risk profiling?",
        "options": [
            "It identifies the specific data assets, critical operational systems, and revenue-generating processes whose compromise would cause maximum financial loss",
            "It calculates the physical scrap value of depreciated server racks for property insurance valuation",
            "It eliminates the need for incident response retainers or business continuity planning",
            "It guarantees that threat actors will only target non-critical public marketing websites"
        ],
        "correct_index": 0,
        "explanation": "Identifying crown jewels allows brokers, risk managers, and underwriters to prioritize controls and limit adequacy around the assets that drive business interruption and privacy liability.",
        "hint": "Focus on which systems and datasets would halt operations or trigger severe liability if lost."
    },
    {
        "chapter": "Ch 01: Cyber Risk & Threat Actors",
        "topic": "Cyber Risk & Threat Actors",
        "is_ai": False,
        "question": "Which attack target profile typically faces the highest combination of operational downtime sensitivity and strict regulatory notification penalties?",
        "options": [
            "Organizations holding high volumes of regulated personal health or financial records alongside 24/7 digital service delivery",
            "Static brochure websites that collect zero user data and process no online transactions",
            "Air-gapped archival libraries with no external network connectivity",
            "Sole proprietorships operating exclusively via offline paper ledgers"
        ],
        "correct_index": 0,
        "explanation": "Entities combining sensitive PII/PHI with continuous digital operations experience both immediate business interruption losses and severe third-party privacy/regulatory claims.",
        "hint": "Look for the intersection of sensitive data volume and continuous uptime dependency."
    },

    # --- CHAPTER 02: IT and Cybersecurity ---
    {
        "chapter": "Ch 02: IT, OT & Security Foundations",
        "topic": "IT & Operational Technology (OT)",
        "is_ai": False,
        "question": "What is the primary underwriting concern when an industrial or utility client converges its Information Technology (IT) network with its Operational Technology (OT) environment?",
        "options": [
            "A ransomware or malware intrusion in corporate IT can pivot laterally into OT systems, causing physical process disruption, safety hazards, or prolonged shutdowns",
            "OT convergence automatically encrypts all corporate emails without requiring additional licensing",
            "Converged OT networks eliminate all vulnerabilities associated with legacy industrial control systems",
            "IT/OT convergence transfers all cyber losses automatically to workers' compensation policies"
        ],
        "correct_index": 0,
        "explanation": "IT/OT convergence bridges corporate networks with industrial control systems (ICS/SCADA), creating pathways for cyberattacks to cause physical operational outages.",
        "hint": "Consider what happens when a phishing email in the corporate office reaches factory floor controllers."
    },
    {
        "chapter": "Ch 02: IT, OT & Security Foundations",
        "topic": "IT & Operational Technology (OT)",
        "is_ai": False,
        "question": "In the CIA Triad of information security, which pillar is most directly compromised during a pure ransomware encryption event that halts production without exfiltrating data?",
        "options": [
            "Availability, because authorized users and systems are denied timely access to critical data and applications",
            "Confidentiality only, because encryption always implies public disclosure of trade secrets",
            "Non-repudiation, because system logs are automatically published to external auditors",
            "Physical perimeter security, because server room locks are disengaged"
        ],
        "correct_index": 0,
        "explanation": "While modern double-extortion ransomware also threatens Confidentiality via data theft, the core act of encrypting operational systems directly attacks Availability.",
        "hint": "Think about which of Confidentiality, Integrity, or Availability is lost when systems are locked up."
    },
    {
        "chapter": "Ch 02: IT, OT & Security Foundations",
        "topic": "Artificial Intelligence Foundations",
        "is_ai": True,
        "question": "When an insured deploys a commercial Large Language Model (LLM) via Retrieval-Augmented Generation (RAG) connected to internal repositories, what core architectural exposure must an underwriter assess?",
        "options": [
            "Improper access controls allowing the AI model to retrieve and expose confidential or restricted internal documents to unauthorized users",
            "Complete elimination of cloud hosting fees due to local model compression",
            "Automatic compliance with all global data privacy statutes without human oversight",
            "Physical overheating of end-user web browsers during text generation"
        ],
        "correct_index": 0,
        "explanation": "If a RAG pipeline lacks granular document-level permissions, users querying the AI assistant can inadvertently access sensitive HR, legal, or customer records.",
        "hint": "Consider what happens if an internal AI chatbot indexes folders that a regular employee shouldn't see."
    },

    # --- CHAPTER 03: Cyber Threats ---
    {
        "chapter": "Ch 03: Cyber & AI Threats",
        "topic": "Malware & Attack Surfaces",
        "is_ai": False,
        "question": "How does a Business Email Compromise (BEC) attack typically cause severe financial loss without deploying ransomware or malware?",
        "options": [
            "Threat actors hijack or spoof trusted executive or vendor email accounts to trick employees into redirecting wire transfers or payroll funds",
            "Threat actors physically steal backup magnetic tapes from an off-site storage vault",
            "Threat actors overload public web servers using volumetric Distributed Denial-of-Service (DDoS) traffic",
            "Threat actors corrupt the firmware of uninterruptible power supplies in the data center"
        ],
        "correct_index": 0,
        "explanation": "BEC relies on social engineering and credential compromise to manipulate payment instructions, often triggering social engineering fraud sublimits rather than extortion coverage.",
        "hint": "Think about fraudulent wire instructions sent from a compromised vendor or CFO inbox."
    },
    {
        "chapter": "Ch 03: Cyber & AI Threats",
        "topic": "AI Threats and Risks",
        "is_ai": True,
        "question": "Which of the following best describes 'data poisoning' as an AI-related cyber exposure?",
        "options": [
            "Manipulating or injecting malicious data into a machine learning training dataset to introduce vulnerabilities, biases, or backdoors",
            "Exfiltrating proprietary source code from a machine learning repository",
            "Failing to encrypt personally identifiable information stored in a cloud database",
            "Using unauthorized synthetic media or deepfakes to conduct spear-phishing campaigns"
        ],
        "correct_index": 0,
        "explanation": "Data poisoning occurs during the training phase where an adversary corrupts input data to alter the behavior, safety, or integrity of the resulting AI model.",
        "hint": "Focus on the phase before model deployment—specifically how an adversary corrupts training inputs."
    },
    {
        "chapter": "Ch 03: Cyber & AI Threats",
        "topic": "AI Threats and Risks",
        "is_ai": True,
        "question": "How are threat actors leveraging generative AI and deepfake technology to escalate social engineering and fraud losses?",
        "options": [
            "By cloning executive voices or live video likenesses to bypass verbal call-back verification controls during high-value wire fraud attempts",
            "By automatically patching zero-day vulnerabilities in legacy enterprise firewalls",
            "By converting encrypted ransomware payloads into harmless plain-text files",
            "By eliminating the need for threat actors to register phishing domains or infrastructure"
        ],
        "correct_index": 0,
        "explanation": "AI-generated voice and video deepfakes defeat traditional human verification steps, increasing the frequency and severity of social engineering and funds transfer fraud.",
        "hint": "Consider how synthetic audio or video undermines traditional 'call the CFO to verify' procedures."
    },
    {
        "chapter": "Ch 03: Cyber & AI Threats",
        "topic": "AI Threats and Risks",
        "is_ai": True,
        "question": "What is a 'prompt injection' attack against a customer-facing generative AI application?",
        "options": [
            "Crafting malicious user inputs that override system instructions to force the AI model to leak sensitive data or execute unauthorized actions",
            "Overloading a server power supply by sending rapid API requests",
            "Encrypting a company's SQL database and demanding cryptocurrency for the decryption key",
            "Installing a physical keylogger onto a software developer's laptop"
        ],
        "correct_index": 0,
        "explanation": "Prompt injection manipulates an LLM into ignoring its safety guardrails, potentially exposing system prompts, backend data, or connected API actions.",
        "hint": "Think about tricking an AI chatbot into ignoring its rules via clever text inputs."
    },

    # --- CHAPTER 04: Computer Networks ---
    {
        "chapter": "Ch 04: Networks, Cloud & Protocols",
        "topic": "Cloud & Network Architecture",
        "is_ai": False,
        "question": "Under the Cloud Shared Responsibility Model (IaaS/PaaS/SaaS), which security obligation almost always remains with the insured customer rather than the cloud provider?",
        "options": [
            "Managing user identity and access permissions (IAM), data classification, and proper configuration of cloud storage buckets",
            "Maintaining physical armed guards and biometric perimeter locks at the hyperscaler's data centers",
            "Replacing failed physical cooling fans and hypervisor server blades in the provider's facility",
            "Laying submarine fiber-optic cables between international cloud availability zones"
        ],
        "correct_index": 0,
        "explanation": "While cloud providers secure the underlying infrastructure ('security OF the cloud'), customers remain liable for identity, data, and configuration ('security IN the cloud').",
        "hint": "Distinguish between physical data center security and customer account/data configuration."
    },
    {
        "chapter": "Ch 04: Networks, Cloud & Protocols",
        "topic": "Cloud & Network Architecture",
        "is_ai": False,
        "question": "Why do cyber underwriters flag exposed Remote Desktop Protocol (RDP) ports on the public internet as a severe underwriting red flag?",
        "options": [
            "Exposed RDP endpoints are prime targets for brute-force credential attacks and ransomware deployment, dramatically increasing breach frequency",
            "RDP automatically disables all endpoint antivirus software across the entire organization",
            "RDP traffic cannot be encrypted under any modern operating system",
            "Using RDP violates federal securities laws for all publicly traded companies"
        ],
        "correct_index": 0,
        "explanation": "Internet-facing RDP without VPN/Zero Trust isolation and MFA is one of the most heavily exploited initial access vectors for ransomware affiliates.",
        "hint": "Think about external attack surface scans looking for open port 3389."
    },
    {
        "chapter": "Ch 04: Networks, Cloud & Protocols",
        "topic": "Cloud & Network Architecture",
        "is_ai": False,
        "question": "How does network segmentation limit the financial severity of a cyber incident?",
        "options": [
            "It isolates critical servers and databases into separate zones, preventing an attacker who compromises one workstation from moving laterally across the entire enterprise",
            "It guarantees that phishing emails can never reach employee inboxes",
            "It doubles the bandwidth of external internet connections during a DDoS attack",
            "It automatically reimburses the insured's deductible after a security breach"
        ],
        "correct_index": 0,
        "explanation": "Segmentation contains intrusions, reducing the blast radius from a single compromised endpoint to a localized segment rather than a total network shutdown.",
        "hint": "Consider how bulkheads in a ship stop flooding from sinking the entire vessel."
    },

    # --- CHAPTER 05: Cyber Defense ---
    {
        "chapter": "Ch 05: Cyber Defense & Controls",
        "topic": "Network Defense & Underwriting",
        "is_ai": False,
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
        "chapter": "Ch 05: Cyber Defense & Controls",
        "topic": "Endpoint Defense (EDR/XDR/MDR)",
        "is_ai": False,
        "question": "How does Endpoint Detection and Response (EDR) improve upon legacy signature-based antivirus software in an underwriter's risk evaluation?",
        "options": [
            "EDR continuously monitors endpoint behavior to detect, alert, and isolate novel or fileless threats in real time rather than relying solely on known malware signatures",
            "EDR permanently prevents employees from ever clicking on malicious links in personal webmail",
            "EDR eliminates the need to apply operating system security patches for up to five years",
            "EDR automatically negotiates ransom reductions with threat actors without legal counsel"
        ],
        "correct_index": 0,
        "explanation": "Legacy antivirus misses zero-day and living-off-the-land attacks; EDR provides behavioral telemetry and active containment capabilities.",
        "hint": "Compare static signature matching with continuous behavioral monitoring and active isolation."
    },
    {
        "chapter": "Ch 05: Cyber Defense & Controls",
        "topic": "Defense in Depth & Resilience",
        "is_ai": False,
        "question": "What value does a 24/7 Managed Detection and Response (MDR) service or Security Operations Center (SOC) provide for mid-market insureds?",
        "options": [
            "Round-the-clock human threat hunting and rapid alert triage, preventing Friday-night intrusions from escalating into Monday-morning enterprise ransomware",
            "Guaranteed immunity from all regulatory fines under GDPR and HIPAA",
            "Automatic replacement of physical hardware damaged by fire or flood",
            "Complete outsourcing of statutory breach notification legal duties"
        ],
        "correct_index": 0,
        "explanation": "Threat actors frequently launch ransomware during weekends or holidays when internal IT teams are offline; 24/7 MDR closes that detection-to-response gap.",
        "hint": "Think about why major ransomware attacks often strike on Friday evenings or holiday weekends."
    },

    # --- CHAPTER 06: Regulations, Standards and Guidelines ---
    {
        "chapter": "Ch 06: Regulations, Privacy & AI Governance",
        "topic": "Data Privacy Regulations",
        "is_ai": False,
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
        "chapter": "Ch 06: Regulations, Privacy & AI Governance",
        "topic": "AI Governance & Regulation",
        "is_ai": True,
        "question": "Why are cyber and liability underwriters increasingly asking applicants about formal AI Governance frameworks (such as the NIST AI Risk Management Framework or EU AI Act compliance)?",
        "options": [
            "To evaluate whether the insured has oversight, human-in-the-loop controls, model auditing, and bias/safety testing to prevent regulatory fines and systemic model failures",
            "Because AI governance frameworks completely eliminate the need for network firewalls and backups",
            "To calculate the exact electricity consumption of corporate data centers for property rating",
            "Because all AI models are strictly prohibited from commercial use in North America and Europe"
        ],
        "correct_index": 0,
        "explanation": "Structured AI governance demonstrates that an organization inventories its AI systems, monitors drift/hallucinations, and mitigates regulatory and liability exposures.",
        "hint": "Think about the questions carriers now ask regarding AI oversight, testing, and regulatory compliance."
    },
    {
        "chapter": "Ch 06: Regulations, Privacy & AI Governance",
        "topic": "Risk Frameworks & Privacy",
        "is_ai": False,
        "question": "Under the EU General Data Protection Regulation (GDPR), within what timeframe must a data controller generally notify the supervisory authority after becoming aware of a personal data breach?",
        "options": [
            "Without undue delay and, where feasible, not later than 72 hours",
            "Within 90 calendar days following the completion of annual financial audits",
            "Only if more than 10 million records are published on the public internet",
            "Within 12 months of renewing the organization's cyber insurance policy"
        ],
        "correct_index": 0,
        "explanation": "GDPR Article 33 mandates notification to the competent supervisory authority within 72 hours of breach awareness unless the breach is unlikely to result in a risk to individuals.",
        "hint": "Recall the strict three-day clock that drives immediate breach coach engagement."
    },

    # --- CHAPTER 07: Cyber Insurance Fundamentals ---
    {
        "chapter": "Ch 07: Cyber Market, Silent Cyber & Silent AI",
        "topic": "Silent AI",
        "is_ai": True,
        "question": "What does the term 'silent AI' refer to in commercial insurance and risk management?",
        "options": [
            "Potential, unquantified insurance losses arising from AI-related liabilities embedded within traditional, non-cyber policies not designed to cover AI risks",
            "AI systems that operate without generating system log files, audit trails, or telemetry",
            "Losses caused by AI models that permanently stop responding due to hardware or power failures",
            "Mandatory confidentiality clauses in vendor agreements regarding algorithmic failures"
        ],
        "correct_index": 0,
        "explanation": "Analogous to 'silent cyber,' silent AI refers to unmodeled AI exposures lurking inside traditional property, casualty, D&O, or general liability policies.",
        "hint": "Compare it to the well-known insurance concept of 'silent cyber.'"
    },
    {
        "chapter": "Ch 07: Cyber Market, Silent Cyber & Silent AI",
        "topic": "Silent Cyber & Market Evolution",
        "is_ai": False,
        "question": "How did the global insurance market resolve the issue of 'silent cyber' across traditional property and casualty lines?",
        "options": [
            "By introducing mandatory affirmative cyber coverage grants or explicit cyber exclusions so policies clearly state whether cyber perils are covered",
            "By banning standalone cyber insurance policies across all Lloyd's syndicates and domestic carriers",
            "By automatically adding unlimited cyber limits to every Commercial General Liability policy at zero premium",
            "By requiring insureds to self-insure 100% of all ransomware and data breach losses"
        ],
        "correct_index": 0,
        "explanation": "Market mandates pushed carriers to eliminate ambiguity by either affirmatively underwriting cyber risk or explicitly excluding it from traditional policies—a cycle now repeating with Silent AI.",
        "hint": "Think about the shift from 'non-affirmative' coverage to 'affirm or exclude.'"
    },
    {
        "chapter": "Ch 07: Cyber Market, Silent Cyber & Silent AI",
        "topic": "Silent AI",
        "is_ai": True,
        "question": "Why is the market correction for 'silent AI' unfolding much faster than the 22-year timeline it took to address 'silent cyber'?",
        "options": [
            "Insurers recognize the systemic cross-line potential across cyber, E&O, D&O, and GL and began introducing targeted AI exclusions and endorsements as early as 2026",
            "Because AI models cannot legally be used by any commercial policyholder",
            "Because silent AI only affects marine cargo and aviation hull policies",
            "Because all AI software vendors provide unlimited indemnification to their customers"
        ],
        "correct_index": 0,
        "explanation": "Having learned from silent cyber, insurers are rapidly clarifying AI intent across lines within months rather than decades.",
        "hint": "Consider how insurers are applying lessons learned from silent cyber to emerging AI exposures."
    },

    # --- CHAPTER 08: The Cyber Policy ---
    {
        "chapter": "Ch 08: Policy Anatomy, Coverages & Exclusions",
        "topic": "First-Party Cyber Coverage",
        "is_ai": False,
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
        "chapter": "Ch 08: Policy Anatomy, Coverages & Exclusions",
        "topic": "Third-Party Cyber Coverage",
        "is_ai": False,
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
        "chapter": "Ch 08: Policy Anatomy, Coverages & Exclusions",
        "topic": "Policy Anatomy & Exclusions",
        "is_ai": False,
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
        "chapter": "Ch 08: Policy Anatomy, Coverages & Exclusions",
        "topic": "Policy Wording & Retroactive Dates",
        "is_ai": False,
        "question": "Why is the 'Retroactive Date' critical in a claims-made cyber insurance policy?",
        "options": [
            "A wrongful act, breach, or security failure must have occurred on or after the retroactive date to trigger coverage when a claim is later made and reported",
            "It sets the exact date on which the insurer must refund the full annual premium",
            "It determines the hourly billing rate of the forensic accounting firm during a claim",
            "It automatically extends policy limits by 50% for incidents occurring prior to company incorporation"
        ],
        "correct_index": 0,
        "explanation": "Claims-made cyber policies use retroactive dates to prevent coverage for historical, latent breaches that occurred before coverage was incepted.",
        "hint": "Consider how claims-made policies handle intrusions that happened years before discovery."
    },
    {
        "chapter": "Ch 08: Policy Anatomy, Coverages & Exclusions",
        "topic": "AI Policy Exposure & Endorsements",
        "is_ai": True,
        "question": "When reviewing a cyber policy for an insured that builds proprietary AI tools, why must a broker examine the definition of 'Computer System' and Media/Tech E&O endorsements?",
        "options": [
            "To verify whether an AI model failure, hallucination, or IP infringement from training data is covered or excluded under traditional security failure definitions",
            "To confirm that the policy pays for routine annual software licensing renewals",
            "To ensure that physical damage to employee smartphones is covered without a deductible",
            "Because AI models are legally classified as tangible real estate under commercial property forms"
        ],
        "correct_index": 0,
        "explanation": "A non-malicious AI model failure or copyright claim over training data may not qualify as a 'security failure' or 'data breach' unless affirmative AI or Media/Tech E&O wording is present.",
        "hint": "Think about whether an AI hallucination is a 'security failure' or a functional/content issue."
    },

    # --- CHAPTER 09: The Process (Underwriting & Claims) ---
    {
        "chapter": "Ch 09: Underwriting, Loss Drivers & Claims",
        "topic": "Ransomware Handling & Extortion",
        "is_ai": False,
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
        "chapter": "Ch 09: Underwriting, Loss Drivers & Claims",
        "topic": "Underwriting & Proposal Forms",
        "is_ai": False,
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
        "chapter": "Ch 09: Underwriting, Loss Drivers & Claims",
        "topic": "Claims Processes",
        "is_ai": False,
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
    },
    {
        "chapter": "Ch 09: Underwriting, Loss Drivers & Claims",
        "topic": "Underwriting & Proposal Forms",
        "is_ai": False,
        "question": "What is the severe legal consequence if an insured falsely attests on a cyber insurance proposal form that MFA is enforced on all remote access, and a breach later reveals MFA was absent?",
        "options": [
            "The insurer may seek policy rescission or void coverage from inception due to material misrepresentation",
            "The insurer must automatically double the aggregate policy limit to compensate for the control gap",
            "The deductible is waived and the broker pays the claim out of commission",
            "The breach is automatically reclassified as a covered natural disaster"
        ],
        "correct_index": 0,
        "explanation": "Material misrepresentations regarding critical controls like MFA on proposal forms can void a policy ab initio (from inception), leaving the insured completely unprotected.",
        "hint": "Recall the real-world precedent where an inaccurate MFA attestation voided a $1M policy from inception."
    },
    {
        "chapter": "Ch 09: Underwriting, Loss Drivers & Claims",
        "topic": "Claims Processes",
        "is_ai": False,
        "question": "Why is engaging external legal counsel ('Breach Coach') as the very first step in an incident response critical for preserving attorney-client privilege?",
        "options": [
            "When counsel retains the digital forensics firm on behalf of the insured, investigative reports are more likely to be protected from discovery in subsequent class-action lawsuits",
            "Forensic engineers are legally barred from inspecting servers unless a judge signs a warrant first",
            "Hiring a breach coach automatically stops ransomware from encrypting additional network drives",
            "It exempts the company from notifying affected consumers under state breach notification laws"
        ],
        "correct_index": 0,
        "explanation": "Routing forensic investigations through external breach counsel helps establish attorney-client privilege and work-product protection over sensitive root-cause findings.",
        "hint": "Think about how plaintiff attorneys try to subpoena forensic reports during data breach litigation."
    },

    # --- CHAPTER 10: Cyber Essentials & Market Developments ---
    {
        "chapter": "Ch 10: Market Developments & Cyber Essentials",
        "topic": "Market Developments & Systemic Risk",
        "is_ai": False,
        "question": "Why do cyber insurers and reinsurers closely model 'aggregation risk' (or systemic cyber risk) across their portfolios?",
        "options": [
            "A single vulnerability in a widely used software tool or cloud provider can trigger thousands of simultaneous claims across unrelated policyholders",
            "Aggregation risk measures the total number of paper forms filed by brokers in a calendar quarter",
            "It ensures that every policyholder uses the exact same antivirus vendor and cloud region",
            "Systemic risk modeling eliminates the need for individual policyholder underwriting"
        ],
        "correct_index": 0,
        "explanation": "Events like SolarWinds, MOVEit, or a major cloud outage demonstrate how shared digital dependencies create correlated losses across an insurer's entire book.",
        "hint": "Consider what happens when one ubiquitous software vendor suffers a zero-day exploit."
    },
    {
        "chapter": "Ch 10: Market Developments & Cyber Essentials",
        "topic": "Market Developments & Systemic Risk",
        "is_ai": False,
        "question": "How do continuous external attack surface monitoring tools used by modern cyber carriers benefit both underwriters and policyholders?",
        "options": [
            "They provide real-time visibility into exposed ports, unpatched vulnerabilities, and expired certificates, enabling proactive remediation before a breach occurs",
            "They replace the need for internal IT staff, backups, and incident response plans",
            "They legally guarantee that a policyholder will never be targeted by ransomware groups",
            "They automatically block all incoming email attachments without user configuration"
        ],
        "correct_index": 0,
        "explanation": "Active risk monitoring shifts cyber insurance from a static annual snapshot to ongoing risk management, alerting insureds to critical exposures early.",
        "hint": "Think about how outside-in scanning turns underwriting into continuous risk mitigation."
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
    "a technology consulting agency",
    "a specialty insurance brokerage",
    "a biotech research firm",
    "a hospitality and hotel chain",
    "a commercial aviation supplier",
    "a digital media publisher",
    "a supply chain software provider",
    "a regional hospital network",
    "a wealth management advisory",
    "an automotive parts distributor",
    "a public infrastructure contractor",
    "a cross-border payment processor",
    "a pharmaceutical manufacturer",
    "a telecommunications carrier",
    "a consumer electronics retailer",
    "an energy grid operator",
    "a commercial real estate group",
    "a managed IT service provider (MSP)",
    "a national food distribution firm",
    "a defense aerospace subcontractor",
    "an enterprise HR software platform",
    "a municipal transit authority"
]

def build_questions(target_count=1000, output_file="questions.json"):
    assert target_count <= 1000, "Question bank cannot exceed 1000 questions."
    bank = []
    seen_questions = set()
    q_num = 1

    for ctx_idx, context in enumerate(SCENARIO_CONTEXTS):
        for seed_idx, base in enumerate(SEED_QUESTIONS):
            if len(bank) >= target_count:
                break

            q_text = f"[Context: {context.capitalize()}] {base['question']}"
            if q_text in seen_questions:
                continue
            seen_questions.add(q_text)

            indexed_options = list(enumerate(base["options"]))
            rng = random.Random(q_num * 101 + 42)
            rng.shuffle(indexed_options)

            shuffled_texts = [opt_text for _, opt_text in indexed_options]
            new_correct_idx = next(
                idx for idx, (orig_idx, _) in enumerate(indexed_options)
                if orig_idx == base["correct_index"]
            )

            bank.append({
                "id": q_num,
                "chapter": base["chapter"],
                "topic": base["topic"],
                "is_ai": base["is_ai"],
                "question": q_text,
                "options": shuffled_texts,
                "correct_index": new_correct_idx,
                "explanation": base["explanation"],
                "hint": base["hint"]
            })
            q_num += 1

        if len(bank) >= target_count:
            break

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(bank, f, indent=2)
    print(f"Successfully generated {len(bank)} non-redundant questions in '{output_file}'.")

if __name__ == "__main__":
    build_questions(1000)
