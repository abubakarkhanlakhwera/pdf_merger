# Streamlit PDF Merger

This project is a simple Streamlit application that allows users to upload multiple PDF files, merge them into a single PDF, and download the merged file. The application utilizes the PyPDF2 library for PDF manipulation.

## Project Structure

```
streamlit-pdf-merger
├── app.py                # Main entry point of the Streamlit application
├── requirements.txt      # Lists the dependencies required for the project
├── uploads               # Directory for storing uploaded files
│   └── .gitkeep          # Keeps the uploads directory in version control
└── README.md             # Documentation for the project
```

## Requirements

To run this application, you need to have Python installed on your machine. You can install the required packages using the following command:

```
pip install -r requirements.txt
```

The `requirements.txt` file includes the following dependencies:

- Streamlit
- PyPDF2

## Running the Application

To start the Streamlit application, navigate to the project directory in your terminal and run:

```
streamlit run app.py
```

This will launch the application in your default web browser.

## Usage

1. Open the application in your web browser.
2. Upload multiple PDF files using the file uploader.
3. Click the "Merge PDFs" button to merge the uploaded files.
4. Once the merging is complete, a download link will be provided for the merged PDF file.

## License

This project is open-source and available under the MIT License.