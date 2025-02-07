# 🏋️ Fitness Chatbot

Your Personal Fitness Assistant built with **LangGraph**, **Streamlit**, and **Chroma Vector Store**. This chatbot can answer questions related to fitness, diet, and nutrition by retrieving information from health-related web content.

## 🚀 Features
- **AI-powered Assistant:** Uses LLM (ChatGroq) for generating intelligent responses.
- **Vector Search:** Retrieves relevant information using Chroma and Hugging Face embeddings.
- **User-friendly UI:** Built with Streamlit for easy interaction.
- **Session Persistence:** Remembers conversation context using session IDs.

## 🛠️ Tech Stack
- **Frameworks:** LangGraph, Streamlit
- **LLM:** ChatGroq (Gemma2-9b-It)
- **Vector Store:** Chroma
- **Embeddings:** Hugging Face (all-MiniLM-L6-v2)
- **Environment Variables:** dotenv

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kiruba11k/Fitness-Chatbot-Agentic-Rag.git
   cd fitness-chatbot
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file:
   ```env
   GROQ_API_KEY=your_groq_api_key
   USER_AGENT=AgenticLLM/1.0
   ```

5. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## 💡 Usage
1. Open the app in your browser (usually at `http://localhost:8501`).
2. Type your question about fitness, diet, or nutrition.
3. The AI assistant will respond with accurate information.
4. Use the "Clear Chat" button to reset the conversation.

## 📋 File Structure
```
fitness-chatbot/
├── main.py               # Core logic for AI Assistant
├── app.py                # Streamlit UI
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not to be committed)
└── README.md             # Project documentation
```

## ⚙️ Customization
- **Modify AI Prompt:** Adjust the `PromptTemplate` in `main.py` to change the assistant's behavior.
- **Change Data Source:** Replace the `WebBaseLoader` URL to fetch content from other sources.
- **Add New Tools:** Integrate additional LangChain tools to enhance functionality.

## 🗝️ Environment Variables
| Variable       | Description                  | Example                 |
|----------------|------------------------------|-------------------------|
| GROQ_API_KEY   | API key for ChatGroq         | `your_groq_api_key`     |
| USER_AGENT     | Custom user agent identifier | `AgenticLLM/1.0`        |

## 🚀 Future Enhancements
- Add more AI tools for diverse health queries.
- Support voice-based interactions.
- Implement multi-language support.

## 🤝 Contributing
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.



---

💬 [**Developed by Kirubakaran Periyasamy**](https://github.com/kiruba11k)

