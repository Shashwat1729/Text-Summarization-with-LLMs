# Text-Summarization-with-LLMs

This project leverages **Large Language Models (LLMs)** to summarize text from uploaded **PDF** and **DOCX** documents. The summarization is performed using the **`facebook/bart-large-cnn`** model from Hugging Face's **transformers** library, integrated into a simple web interface built with **Flask**.

## **Features**
- **Supports PDF and DOCX** file uploads.
- Automatically extracts text from documents and summarizes it using **pre-trained LLMs**.
- A user-friendly web interface for uploading files and displaying summaries.

## **Live Demo**
You can run this project locally on your machine to upload a document and generate summaries in real-time.

---

## **Installation & Setup**

### 1. **Clone the Repository**
To get started, clone the repository using the following command:

```bash
git clone https://github.com/Shashwat1729/Text-Summarization-with-LLMs.git
cd Text-Summarization-with-LLMs
```

### 2. **Install Dependencies**
Install the required dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 3. **Run the Flask Application**
To launch the web app locally, run the following command:

```bash
python app.py
```

The Flask app will start, and you can access it in your web browser at:

```
http://127.0.0.1:5000/
```

---

## **How to Use**

1. Open your browser and navigate to `http://127.0.0.1:5000/`.
2. Upload a **PDF** or **DOCX** document via the interface.
3. The app will extract text from the document and provide a **summarized version** below the upload form.

---

## **Project Structure**

```
Text-Summarization-with-LLMs/
│
├── app.py                   # Main Flask application for file upload and summarization
├── requirements.txt          # Python dependencies for the project
├── README.md                 # Documentation of the project
├── static/                   # Folder for static files (e.g., CSS)
│   ├── style.css             # Basic styling for the web interface
└── templates/                # Folder for HTML templates
    ├── index.html            # Main HTML page for the app
```

### **Key Files**:
- **`app.py`**: The main script to run the Flask web application and handle file uploads and summarization.
- **`requirements.txt`**: Lists all dependencies (e.g., Flask, Hugging Face Transformers, PyPDF2, docx).
- **`templates/index.html`**: The HTML template for the file upload page.
- **`static/style.css`**: Basic styling for the web interface.

---

## **Dependencies**

The project relies on the following Python libraries:

```txt
Flask==2.1.1
transformers==4.30.2
torch==2.0.1
PyPDF2==3.0.0
python-docx==0.8.11
```

To install the dependencies, simply run:

```bash
pip install -r requirements.txt
```

---

## **Contributing**

Feel free to fork the repository and submit **pull requests** if you would like to contribute to improving the project. Suggestions, feature requests, and bug reports are welcome!

---

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## **Contact**

If you have any questions or need further assistance, feel free to reach out

---
