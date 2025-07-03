# LLM3 Streaming Multi-Model Chatbot Flask App
This project is a Flask web application that demonstrates real-time streaming chat responses from multiple large language models (OpenAI, Groq, Gemini) using LangChain, with session-based memory and server-sent events (SSE).

## Features
- Supports OpenAI, Groq, and Google Gemini models via LangChain.
- Real-time streaming chat responses using SSE (`/chatresponsestream` endpoint).
- Maintains chat history per session.
- Easily switch between models for experimentation.
- Loads API keys from a `.env` file.

## Setup
1. **Clone the repository** and navigate to the `llm3` directory.

2. **Install dependencies:**
   pip install flask langchain-openai langchain-groq langchain-google-genai langchain-core joblib numpy python-dotenv
  

3. **Create a `.env` file** in the project root with your API keys:
   OPENAI_API_KEY=your_openai_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here


4. **Run the app:**
   python textgenerator.py
 

5. **Access the web interface:**
   - Open [http://localhost:5000/](http://localhost:5000/) in your browser.

## How It Works

- The app receives user input (via web or API), selects the requested model, and streams the response back to the client in real time.
- Chat history is maintained per session using LangChain's `InMemoryChatMessageHistory`.
- The `/chatresponsestream` endpoint streams responses using server-sent events (SSE), allowing for a responsive chat UI.

## API Usage

- **GET** `/chatresponsestream`
  - Query parameters:
    - `in_message`: The user's prompt.
    - `session_id`: Unique session identifier.
    - `model_name`: Model to use (`openai`, `groq`, or `gemini`).
  - Streams response chunks as SSE.

## File Structure

- `textgenerator.py` - Main Flask app with streaming and multi-model support.
- `templates/streaming_output.html` - HTML template for streaming chat interface.

