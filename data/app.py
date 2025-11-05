import streamlit as st

st.title("College Chatbot - Bits Pilani")

queries = {
    "exam": "Exams start on Dec 10, 2025.",
    "fees": "Hostel fees: ₹50,000/year.",
    "admission": "Apply at bits-pilani.ac.in/admissions",
    "library": "Open 9 AM - 5 PM",
    "hostel": "Apply in admin office",
    "timetable": "Monday: Maths 9AM, Physics 10AM"
}

user = st.text_input("Ask anything:").lower()

if user:
    if "exam" in user:
        st.write("Bot:", queries["exam"])
    elif "fee" in user:
        st.write("Bot:", queries["fees"])
    elif "admission" in user:
        st.write("Bot:", queries["admission"])
    elif "library" in user:
        st.write("Bot:", queries["library"])
    elif "hostel" in user:
        st.write("Bot:", queries["hostel"])
    elif "timetable" in user:
        st.write("Bot:", queries["timetable"])
    else:
        st.write("Bot: Sorry, try asking about exams, fees, or admission.")
