# RAG-LLM: Movie Recommendation Chatbot with Retrieval-Augmented Generation

This project is a Flask web application that combines Retrieval-Augmented Generation (RAG) with multi-model LLM support (OpenAI, Groq, Gemini) for movie recommendations. It features user authentication, persistent chat history in MongoDB, and real-time streaming responses using LangChain.

## Features

- **Retrieval-Augmented Generation (RAG):**  
  Integrates vector search over a movie database to provide context-aware recommendations.
- **Multi-Model Support:**  
  Switch between OpenAI, Groq, and Google Gemini models.
- **User Authentication:**  
  Login/logout and session management with Flask-Login.
- **Persistent Chat History:**  
  Stores user chats and chat details in MongoDB.
- **Streaming Responses:**  
  Real-time chat using server-sent events (SSE).
- **Session-Based Memory:**  
  Maintains chat history per user and chat session.

## Setup

1. **Clone the repository** and navigate to the `rag-llm` directory.

2. **Install dependencies:**
   pip install flask 
   pip install flask-login 
   pip install langchain-openai 
   pip install langchain-groq 
   pip install langchain-google-genai 
   pip install langchain-core 
   pip install joblib 
   pip install numpy 
   pip install python-dotenv 
   pip install pymongo 
   pip installpandas


3. **Create a `.env` file** in the project root with your API keys and MongoDB connection string:
   OPENAI_API_KEY=your_openai_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   MONGO_DB_CONNECTION=your_mongodb_connection_string
 

4. **Ensure MongoDB is running** and accessible with the provided connection string.

5. **Run the app:**
   python textgenerator.py
   

6. **Access the web interface:**
   - Open [http://localhost:5000/](http://localhost:5000/) in your browser.

## How It Works

- **Login:**  
  Users log in to start a chat session. User and chat data are managed in MongoDB.
- **Chat:**  
  User messages are augmented with relevant movie context retrieved via vector search.
- **Model Selection:**  
  The app supports OpenAI, Groq, and Gemini models for generating responses.
- **Streaming:**  
  Responses are streamed to the client in real time.
- **Chat History:**  
  All chats and responses are stored and can be retrieved for each user.

## API Usage

- **GET** `/chatresponsestream`
  - Query parameters:
    - `in_message`: The user's prompt.
    - `chat_id`: Unique chat identifier.
    - `model_name`: Model to use (`openai`, `groq`, or `gemini`).
  - Streams response chunks as SSE.

## File Structure

- `textgenerator.py` - Main Flask app with RAG, authentication, and streaming.
- `models/user.py` - User model for authentication.
- `util/chats.py` - Chat utilities for MongoDB operations.
- `util/movies.py` - Vector search for movie recommendations.
- `templates/streaming_output.html` - HTML template for chat interface.
- `templates/index.html` - Login page template.
