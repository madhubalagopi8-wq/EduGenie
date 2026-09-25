import streamlit as st

st.set_page_config(page_title="EduGenie - AI Study Buddy")

st.title("🎓 EduGenie - Your AI Study Buddy")
st.write("Welcome to EduGenie!")

subject = st.selectbox("Subject select pannu:", ["Maths", "Science", "Computer Science"])
question = st.text_input("Un doubt enna?")

if st.button("Ask Genie"):
    if question:
        st.success(f"{subject} la un doubt: {question}")
        st.write("AI Answer: Ithukku answer soon varum! (Demo version)")
    else:
        st.warning("Please oru question type pannu da!")

st.sidebar.write("Created by Madhubala G")
