import streamlit as st
from PyPDF2 import PdfMerger
import os
import io

UPLOAD_FOLDER = "uploads"
MERGED_FILE = "merged_output.pdf"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

st.title("PDF Merger")

uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

if st.button("Merge PDFs"):
    if uploaded_files:
        merger = PdfMerger()
        file_paths = []

        for uploaded_file in uploaded_files:
            filename = uploaded_file.name
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            with open(filepath, "wb") as f:
                f.write(uploaded_file.getbuffer())
            file_paths.append(filepath)

        for path in sorted(file_paths):
            merger.append(path)

        merged_file_path = os.path.join(UPLOAD_FOLDER, MERGED_FILE)
        merger.write(merged_file_path)
        merger.close()

        # Read the merged PDF file
        with open(merged_file_path, "rb") as file:
            pdf_bytes = file.read()
        
        # Create a download button for the merged PDF
        st.success("PDFs merged successfully!")
        st.download_button(
            label="Download Merged PDF",
            data=pdf_bytes,
            file_name="merged_document.pdf",
            mime="application/pdf"
        )

        # Clean up uploaded files
        for path in file_paths:
            os.remove(path)
    else:
        st.error("No files uploaded")