import re

def get_bot_response(user_input):
    # Convert input to lowercase to make pattern matching easier and case-insensitive
    user_input = user_input.lower()

    # Rule 1: Greetings using Regex pattern matching
    # \b matches word boundaries so it doesn't trigger on words like "thick" (which has 'hi')
    if re.search(r'\b(hi|hello|hey|greetings)\b', user_input):
        return "Hello there! How can I help you today?"

    # Rule 2: Simple string matching for "how are you"
    elif "how are you" in user_input:
        return "I'm just a simple bot, but I'm functioning perfectly! How are you?"

    # Rule 3: Identity questions
    elif re.search(r'\b(name|who are you)\b', user_input):
        return "I am a simple rule-based chatbot written in Python."

    # Rule 4: Weather inquiries
    elif "weather" in user_input:
        return "I don't have access to the internet to check the live weather, but I hope it's sunny!"

    # Rule 5: Help prompt
    elif "help" in user_input:
        return "I can say hello, talk about my identity, or pretend to know the weather. Try asking me something!"

    # Fallback/Default Response: When the bot doesn't recognize the pattern
    else:
        return "I'm sorry, I don't understand that yet. My rules are still quite basic. Could you rephrase?"

def start_chat():
    print("🤖 Bot: Hi! I'm a simple chatbot. Type 'bye', 'quit', or 'exit' to end our chat.")
    print("-" * 50)
    
    # Create an infinite loop to keep the conversation going
    while True:
        # 1. Get user input
        user_input = input("👤 You: ")

        # 2. Check for exit commands to break the loop
        if user_input.lower() in ['bye', 'quit', 'exit']:
            print("🤖 Bot: Goodbye! Have a great day!")
            break

        # 3. Get the bot's response and print it
        response = get_bot_response(user_input)
        print(f"🤖 Bot: {response}")

# This ensures the script runs when executed directly
if __name__ == "__main__":
    start_chat()
