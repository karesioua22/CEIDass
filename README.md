readme_content = """# 💻 CEID Assistant Chatbot (CEIDass)

Welcome to **CEIDass**, a Retrieval-Augmented Generation (RAG) agent designed specifically for the Computer Engineering and Informatics Department (CEID) at the University of Patras. 

This digital assistant answers student queries regarding courses, professors, department regulations, building instructions, and laboratory information using advanced natural language processing.

---

## ⚠️ The Hardest Part: Data Preprocessing

The biggest challenge in building this project was the data preprocessing pipeline. The original data (course catalogs, department rules, etc.) was trapped in complex PDF formats. 

To get this data into a structured format that actually helps the LLM understand the context, the following steps were taken:
1. **OCR Extraction:** Raw text was extracted from the PDFs using OCR techniques.
2. **Handmade Scripts:** Custom scripts were written to clean, separate, and format the messy OCR output into structured, hierarchical Markdown files. 

This meticulously formatted Markdown allows the ingestion pipeline to split the documents accurately by headers, providing the LLM with highly relevant and contextual chunks.

---

## 🚀 Getting Started

### 1. Rename the Folder
If you haven't already, make sure the main project folder is renamed to `ceid_chatbot`.

### 2. Set Up Your Environment Variables
The chatbot relies on OpenAI's models. You need to provide your API key.
* Create a new file named `.env` in the root of your project folder.
* Add your OpenAI API key to the file like this:
### 3. Install Required Packages
It is highly recommended to use a virtual environment. Once your virtual environment is activated, install the necessary dependencies:
pip install streamlit langchain-openai langchain-chroma langchain-text-splitters python-dotenv
🗄️ Database & Ingestion (ingest_final.py)
The file ingest_final.py is responsible for reading the structured Markdown files, chunking them intelligently based on headers, generating embeddings, and saving them to a local Chroma vector database (db).

🛑 IMPORTANT NOTE: I have already provided the db folder with the pre-built vector database. You do not need to run the ingestion script! If you want to run it anyway (for example, if you modify the markdown files), you must delete the existing db folder first, and then run:
python ceid_chatbot/ingest_final.py
▶️ Running the Application
Once your .env file is set up and your packages are installed, you can start the chatbot interface.

Run the following command from the root directory:
streamlit run ceid_chatbot/src1/app.py
This will launch the Streamlit frontend in your default web browser, and you can start chatting with CEIDass!
