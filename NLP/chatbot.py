def preprocess_text(text):
    # Simple preprocessing: lowercase and strip whitespace
    return text.lower().strip()

def chatbot_response(user_input):
    processed_text = preprocess_text(user_input)

    if "hello" in processed_text or "hi" in processed_text:
        return "Hello! How can I assist you?"
    elif "weather" in processed_text:
        return "I'm not a weather bot, but I can help with other queries!"
    else:
        return "I'm still learning! Can you rephrase your question?"

# Test chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    print(f"Chatbot: {chatbot_response(user_input)}")
