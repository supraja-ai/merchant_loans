# LLM2 Multi-Model Chatbot Flask App
This project is a Flask web application that demonstrates how to use multiple large language models (OpenAI, Groq, Gemini) for chat-based tasks with session-based memory using LangChain.

## Features
- Supports OpenAI, Groq, and Google Gemini models via LangChain.
- Maintains chat history per session.
- `/generate_text` API endpoint for JSON-based text generation.
- `/chatresponse` web endpoint for interactive chat using an HTML form.
- Loads API keys from a `.env` file.
- Easily switch between models for experimentation.

## Setup
1. **Clone the repository** and navigate to the `llm2` directory.

2. **Install dependencies:**
   
   pip install flask 
   pip install langchain-openai 
   pip install langchain-groq 
   pip install langchain-google-genai 
   pip install langchain-core 
   pip installjoblib 
   pip install numpy 
   pip installpython-dotenv


3. **Create a `.env` file** in the project root with your API keys:
   
   OPENAI_API_KEY=your_openai_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   

4. **Run the app:**

   python textgen.py
  

5. **Access the web interface:**
   - Open [http://localhost:5000/](http://localhost:5000/) in your browser.

## How It Works
- The app receives user input (via web or API), selects the requested model, and sends the prompt to the chosen LLM.
- Chat history is maintained per session using LangChain's `InMemoryChatMessageHistory`.
- The response is returned as JSON (API) or rendered in the HTML template (web).

## API Usage
- **POST** `/generate_text`
  - Request JSON:  
    ```json
    {
      "in_message": "Your prompt here",
      "session_id": "unique_session_id"
    }
    ```
  - Response JSON:  
    ```json
    {
      "Generated Response": "AI response here"
    }
    ```

## File Structure
- `textgen.py` - Main Flask app with multi-model support.
- `templates/inputtest.html` - HTML template for chat interface.

