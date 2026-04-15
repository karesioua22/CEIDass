
# 💻 CEID Assistant Chatbot (CEIDass)

Welcome to **CEIDass**, a Retrieval-Augmented Generation (RAG) agent designed specifically for the Computer Engineering and Informatics Department (CEID) at the University of Patras.

This digital assistant answers student queries regarding courses, professors, department regulations, building instructions, and laboratory information using advanced natural language processing.

---

## ⚠️ The Hardest Part: Data Preprocessing (To be uploaded)

The biggest challenge in building this project was the data preprocessing pipeline. The original data (course catalogs, department rules, etc.) was trapped in complex PDF formats.

To transform this data into a structured format usable by an LLM, the following steps were taken:

1. **OCR Extraction**  
   Raw text was extracted from PDFs using OCR techniques.

2. **Custom Processing Scripts**  
   Handmade scripts were developed to clean, separate, and structure the noisy OCR output into hierarchical Markdown files.

This carefully structured Markdown enables accurate document chunking based on headers, allowing the LLM to retrieve highly relevant and contextual information.

---

## 🚀 Getting Started

### 1. Rename the Folder

Ensure the main project folder is named:

```bash
ceid_chatbot
````

---

### 2. Set Up Environment Variables

The chatbot uses OpenAI models and requires an API key.

1. Create a `.env` file in the root directory.
2. Add your API key:

```env
OPENAI_API_KEY=your_api_key_here
```

---

### 3. Install Required Packages

It is recommended to use a virtual environment.

Install dependencies:

```bash
pip install streamlit langchain-openai langchain-chroma langchain-text-splitters python-dotenv
```

---

## 🗄️ Database & Ingestion (`ingest_final.py`)

The `ingest_final.py` script:

* Reads structured Markdown files
* Splits them into chunks based on headers
* Generates embeddings
* Stores them in a local Chroma vector database (`db/`)

### ⚠️ Important Note

A pre-built `db/` folder is already included.

👉 **You do NOT need to run ingestion.**

If you want to rebuild the database:

```bash
rm -rf db
python ceid_chatbot/ingest_final.py
```

---

## ▶️ Running the Application

After setting up your `.env` file and installing dependencies, run:

```bash
streamlit run ceid_chatbot/src1/app.py
```

This will launch the Streamlit interface in your browser, and you can start chatting with **CEIDass**.


