import streamlit as st
from study_chain import study_chain

st.set_page_config(page_title="AI Study Assistant")

st.title("📚 AI Study Assistant")

topic = st.text_area("Enter Study Topic or Notes")

if st.button("Generate Study Material"):

    if topic.strip():
        with st.spinner("Generating... ⏳"):
            try:
                result = study_chain.invoke({"topic": topic})

                st.markdown("### 📘 Summary")
                st.markdown(result["summary"])

                st.markdown("### 🧠 Notes")
                st.markdown(result["notes"])

                st.markdown("### ❓ Quiz Questions")
                st.markdown(result["quiz"])

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a topic!")