# 📄 RAG Chatbot using LangChain, FAISS, Gemini & Streamlit

A Retrieval-Augmented Generation (RAG) Chatbot that allows users to upload PDF documents and ask questions about their content. The system retrieves relevant information from the uploaded PDF and generates accurate answers using Google's Gemini model.

---

## 🚀 Features

- Upload PDF documents
- Extract text from PDFs
- Split documents into chunks
- Generate embeddings using Hugging Face
- Store embeddings in FAISS Vector Database
- Retrieve relevant chunks using similarity search
- Generate contextual answers using Gemini AI
- Interactive Streamlit web interface
- Source document display for transparency

---

## 🛠️ Technologies Used

- Python
- LangChain
- Google Gemini API
- FAISS Vector Store
- Hugging Face Embeddings
- PyPDF
- Streamlit
- dotenv

---

## 📂 Project Structure

```text
rag-chatbot/
│
├── app.py
├── .env
├── requirements.txt
│
├── uploads/
├── vectorstore/
│
├── src/
│   ├── pdf_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_db.py
│   └── rag_chain.py
│
├── test_pdf.py
├── test_chunking.py
├── test_embeddings.py
├── test_vector_db.py
├── test_retrieval.py
├── test_gemini.py
└── test_rag.py
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd rag-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API Key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_api_key_here
```

Get your API key from:

https://aistudio.google.com/

---

## ▶️ Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 🔄 How It Works

### Step 1: PDF Upload

The user uploads a PDF document through the Streamlit interface.

### Step 2: Text Extraction

The PDF is processed using PyPDFLoader and converted into LangChain documents.

### Step 3: Chunking

Large documents are split into smaller chunks using RecursiveCharacterTextSplitter.

### Step 4: Embedding Generation

Each chunk is converted into vector embeddings using:

```text
sentence-transformers/all-MiniLM-L6-v2
```

### Step 5: Vector Storage

Embeddings are stored in a FAISS Vector Database for fast similarity search.

### Step 6: Retrieval

When a user asks a question, the most relevant chunks are retrieved from FAISS.

### Step 7: Answer Generation

The retrieved context is sent to Gemini, which generates an accurate response.

---

## 📸 Sample Questions

- What skills does Sathwik have?
- What projects are mentioned in the resume?
- What is the educational background?
- What technologies were used in the projects?
- Summarize the resume.

---

## 🧪 Testing Modules

### PDF Loader

```bash
python test_pdf.py
```

### Chunking

```bash
python test_chunking.py
```

### Embeddings

```bash
python test_embeddings.py
```

### Vector Database

```bash
python test_vector_db.py
```

### Retrieval

```bash
python test_retrieval.py
```

### Gemini API

```bash
python test_gemini.py
```

### Complete RAG Pipeline

```bash
python test_rag.py
```

---

## 📈 Future Improvements

- Multiple PDF support
- Chat history memory
- PDF summarization
- Citation highlighting
- Multi-user support
- Cloud deployment
- Voice-based queries

---

## 👨‍💻 Author

**Dubakunta Sathwik**

- GitHub: https://github.com/sathwik-creator
- LinkedIn: https://linkedin.com/in/sathwik-dubakunta

---

## 📄 License

This project is developed for educational and learning purposes.