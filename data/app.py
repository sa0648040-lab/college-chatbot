import streamlit as st
import random

# All responses in English
responses = {
    "greet": ["Hello! I'm the BITS Pilani Smart Chatbot. Ask me about exams, fees, admission, placements — anything! 😊"],
    "ask_exam_schedule": ["Mid-semester exams are typically held from **December 10 to 18, 2025**. Check the student portal for the detailed timetable. Practice School has a separate schedule."],
    "ask_fees": ["M.Tech semester fee is **₹2,05,000** (tuition + hostel + mess). Merit scholarships reduce it. Pay via BITS Pay portal before the deadline."],
    "ask_admission": ["M.Tech admission is based on **BITSAT score**. Apply at **bitsadmission.com**. Last date: **May 30, 2026**. Eligibility: B.Tech with 60%+."],
    "ask_library": ["Central Library is open **8 AM to 12 AM** (Monday to Sunday). You can issue up to 5 books for 15 days. Digital library access is available online."],
    "ask_hostel": ["Hostel rooms are allotted on a first-come-first-served basis. Room change is allowed at the end of the semester. Mess menu changes weekly — check with the warden."],
    "ask_placement": ["2024 placement stats: **Average ₹30 LPA**, **Highest ₹1 Cr+**. 90%+ M.Tech students placed. Top recruiters: Google, Microsoft, Goldman Sachs."],
    "ask_contact": ["Admin Office: **01596-242210** | Registrar: **01596-242093** | HOD CSE: **cse@bits-pilani.ac.in** | Emergency: **01596-244090**"],
    "ask_events": ["Oasis Cultural Fest: **October 2026** | Waves Tech Fest: **February 2026** | Sports Meet: **March 2026** | Convocation: **May 2026**"],
    "ask_scholarship": ["Merit Scholarship: **15% fee waiver** for top 1% students. Need-based aid available. Apply at **scholarship@bits-pilani.ac.in**."],
    "ask_academics": ["M.Tech CSE includes DS, AI, ML, DBMS. Course registration is online. CGPA = (Credits × Grade) / Total Credits. Minimum 75% attendance required."],
    "default": ["Sorry, I don't know that yet. 😅\nTry asking about: **exams, fees, admission, library, hostel, placement, events, scholarship, academics**"]
}

# Streamlit App
st.set_page_config(page_title="BITS Pilani Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 BITS Pilani Smart Chatbot")
st.markdown("Ask anything — exams, fees, placements, events, and more!")

user_input = st.text_input("Your Question:", placeholder="e.g., When are mid-semester exams?")

if user_input:
    query = user_input.lower()

    # Intent Detection (50+ query support)
    if any(word in query for word in ["hello", "hi", "hey", "morning"]):
        intent = "greet"
    elif any(word in query for word in ["exam", "mid", "compre", "quiz", "timetable", "schedule", "practice school"]):
        intent = "ask_exam_schedule"
    elif any(word in query for word in ["fee", "tuition", "hostel", "mess", "payment", "scholarship", "installment"]):
        intent = "ask_fees"
    elif any(word in query for word in ["admission", "apply", "bitsat", "eligibility", "application", "deadline"]):
        intent = "ask_admission"
    elif "library" in query:
        intent = "ask_library"
    elif "hostel" in query:
        intent = "ask_hostel"
    elif "placement" in query or "package" in query or "company" in query:
        intent = "ask_placement"
    elif "contact" in query or "number" in query or "email" in query:
        intent = "ask_contact"
    elif any(word in query for word in ["oasis", "waves", "fest", "event", "convocation", "sports"]):
        intent = "ask_events"
    elif "scholarship" in query:
        intent = "ask_scholarship"
    elif any(word in query for word in ["syllabus", "course", "cgpa", "credit", "thesis", "attendance"]):
        intent = "ask_academics"
    else:
        intent = "default"

    # Show Response
    reply = random.choice(responses[intent])
    st.success(f"**Bot:** {reply}")
