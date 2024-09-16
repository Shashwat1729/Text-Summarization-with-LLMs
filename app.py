import os
from flask import Flask, request, render_template
from transformers import pipeline
import docx
import PyPDF2

app = Flask(__name__)

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to extract text from PDFs
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

# Function to extract text from DOCX
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

# Function to summarize text
def summarize_text(text):
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    file_ext = os.path.splitext(file.filename)[1].lower()

    # Extract text based on file type
    if file_ext == '.pdf':
        text = extract_text_from_pdf(file)
    elif file_ext == '.docx':
        text = extract_text_from_docx(file)
    else:
        return "Unsupported file type", 400

    # Summarize the extracted text
    summary = summarize_text(text)
    
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
