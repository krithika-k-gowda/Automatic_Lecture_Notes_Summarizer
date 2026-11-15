
import streamlit as st

from text_processor import extract_text_from_pdf, chunk_text
from summarizer import generate_notes

st.set_page_config(
    page_title="Lecture Notes Summarizer",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Lecture Notes Summarizer")

st.write(
    "Upload your lecture PDF and generate "
    "short, meaningful notes using AI."
)

uploaded_file = st.file_uploader(
    "Upload your lecture PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    if st.button("Generate Notes"):

        with st.spinner("Extracting lecture content..."):

            extracted_text = extract_text_from_pdf(uploaded_file)

        if not extracted_text.strip():

            st.error("No readable text found in the PDF.")

        else:

            chunks = chunk_text(extracted_text)
            st.write(f"Total chunks: {len(chunks)}")

            with st.spinner("Generating AI notes..."):

                notes = generate_notes(chunks)

            st.success("Notes generated successfully!")

            st.subheader("Your Lecture Notes")

            st.markdown(notes)

            st.download_button(
                label="Download Notes",
                data=notes,
                file_name="lecture_notes.txt",
                mime="text/plain"
            )
