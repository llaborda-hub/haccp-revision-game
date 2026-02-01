import streamlit as st

st.set_page_config(page_title="HACCP Exam Trainer", page_icon="📋")

# --- SESSION STATE ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'hp' not in st.session_state:
    st.session_state.hp = 3
if 'level' not in st.session_state:
    st.session_state.level = 1

# --- CONTENT FROM YOUR TABLES ---
# Table 1: Methodology Logic
methodology_tasks = [
    {"term": "Frequency", "definition": "How often? (The planned periodicity of checks)", "source": "Page 3"},
    {"term": "Verification Activity", "definition": "What to check? (Actions to see if practices are correct)", "source": "Page 3"},
    {"term": "Check Procedure", "definition": "How? (Time, conditions, place and steps for the check)", "source": "Page 3"},
    {"term": "Person in Charge", "definition": "Who? (The person responsible for the activity)", "source": "Page 3"},
    {"term": "Record", "definition": "How to save results? (Models to record results and incidents)", "source": "Page 3"}
]

# Table 2: The 7 Principles Examples
principles = [
    {"p": "Principle 1", "task": "Analyze hazards", "ex": "Microorganism growth", "source": "Page 3"},
    {"p": "Principle 3", "task": "Set critical limits", "ex": "Preservative: 2-2.5g/Kg", "source": "Page 4"},
    {"p": "Principle 4", "task": "Surveillance system", "ex": "Supervise weighing and adding", "source": "Page 4"},
    {"p": "Principle 5", "task": "Corrective measures", "ex": "Decide what to do if the additive amount is wrong", "source": "Page 4"},
    {"p": "Principle 7", "task": "Documentation", "ex": "Register of additive weights", "source": "Page 4"}
]

# --- GAME UI ---
st.title("🛡️ HACCP Professional Revision")
st.write("Master the tables for your exam. Use the icons to help you!")

# Stats Bar
c1, c2, c3 = st.columns(3)
c1.metric("❤️ HP", st.session_state.hp)
c2.metric("⭐ SCORE", st.session_state.score)
c3.metric("📈 LEVEL", st.session_state.level)

if st.session_state.hp <= 0:
    st.error("💀 GAME OVER! You need more revision.")
    if st.button("Try Again"):
        st.session_state.hp, st.session_state.score, st.session_state.level = 3, 0, 1
        st.rerun()

# --- LEVEL 1: THE METHODOLOGY TABLE ---
elif st.session_state.level == 1:
    st.header("Phase 1: The Methodology Table")
    st.info("Match the 'Question' to the correct 'Table Column'.")
    
    q_item = methodology_tasks[st.session_state.score // 10 % len(methodology_tasks)]
    st.subheader(f"If the question is: '{q_item['definition']}'")
    
    choice = st.selectbox("Which column is it?", [m['term'] for m in methodology_tasks])
    
    if st.button("Confirm Choice"):
        if choice == q_item['term']:
            st.success(f"✅ Correct! [Source: {q_item['source']}]")
            st.session_state.score += 10
            if st.session_state.score >= 50:
                st.session_state.level = 2
            st.rerun()
        else:
            st.error("❌ Wrong match.")
            st.session_state.hp -= 1
            st.rerun()

# --- LEVEL 2: THE 7 PRINCIPLES MATCHING ---
elif st.session_state.level == 2:
    st.header("Phase 2: HACCP Principles & Examples")
    st.info("Look at the 'Example' and choose the correct 'Principle Number'.")
    
    p_item = principles[(st.session_state.score - 50) // 10 % len(principles)]
    st.warning(f"EXAMPLE: '{p_item['ex']}'")
    
    p_choice = st.radio("Which Principle is this?", [p['p'] for p in principles])
    
    if st.button("Verify Principle"):
        if p_choice == p_item['p']:
            st.success(f"✅ Correct! This is {p_item['task']}. [Source: {p_item['source']}]")
            st.session_state.score += 10
            if st.session_state.score >= 100:
                st.session_state.level = 3
            st.rerun()
        else:
            st.error("❌ Not that one.")
            st.session_state.hp -= 1
            st.rerun()

# --- LEVEL 3: TRACEABILITY STAGES ---
elif st.session_state.level == 3:
    st.header("Phase 3: Input, Process, or Output?")
    st.info("Where do we record these documents? [Source: Page 5]")
    
    doc_q = st.selectbox("Document: 'Sales Tickets & Transportation Vouchers'", ["INPUTS", "PRODUCTION PROCESS", "OUTPUTS"])
    
    if st.button("Submit"):
        if doc_q == "OUTPUTS":
            st.balloons()
            st.success("🏆 MASTER! You finished the revision.")
            if st.button("Restart Game"):
                st.session_state.hp, st.session_state.score, st.session_state.level = 3, 0, 1
                st.rerun()
        else:
            st.error("❌ Remember: Sales happen at the end (Output)!")
            st.session_state.hp -= 1
            st.rerun()
