# OpenAI Text Generator Flask App
This project is a simple Flask web application that uses OpenAI's API to generate text responses based on user input.

## Features
- `/generate_text` API endpoint for JSON-based text generation.
- `/chatresponse` web endpoint for interactive chat using an HTML form.
- Uses OpenAI's GPT-4o-mini model.
- Loads API key from a `.env` file.

## Setup
1. **Clone the repository** and navigate to the `llm1` directory.

2. **Install dependencies:**
   pip install flask 
   pip install openai 
   pip install python-dotenv 
   pip install joblib
   pip install numpy
   

3. **Create a `.env` file** in the project root with your OpenAI API key:
   
   OPENAI_API_KEY=your_openai_api_key_here
   

4. **Run the app:**
   
   python textgenerator.py
   

5. **Access the web interface:**
   - Open [http://localhost:5000/](http://localhost:5000/) in your browser.

## API Usage

- **POST** `/generate_text`
  - Request JSON: `{"in_message": "Your prompt here"}`
  - Response JSON: `{"Generated Response": "AI response here"}`

## File Structure

- `textgenerator.py` - Main Flask app.
- `templates/inputtest.html` - HTML template for chat interface.

