# ============================================
# PROJECT 1: Rule-Based AI Chatbot
# Built for DecodeLabs Internship - Batch 2026
# ============================================

responses = {
    "hello": "Hi there! Welcome. How can I help you today?",
    "hi": "Hello! Great to have you here. What do you need?",
    "how are you": "I'm a bot, so I'm always at 100%! How can I assist?",
    "what is your name": "My name is DecoBot. Nice to meet you!",
    "what can you do": "I can answer your questions and have a basic conversation.",
    "help": "Try asking me: hello, how are you, what is your name, bye",
    "bye": "Goodbye! Have a wonderful day!",
    "thanks": "You're welcome! Happy to help.",
    "who created you": "I was built by an AI intern at DecodeLabs!",
    "good morning": "Good morning! Ready for a productive day?",
"tell me a joke": "Why do programmers prefer dark mode? Light attracts bugs!",
"who are you": "I am DecoBot, your rule-based AI assistant!",
"what is ai": "AI is the simulation of human intelligence by machines.",
}

def get_clean_input():
    raw_input_text = input("You: ")
    clean_input_text = raw_input_text.lower().strip()
    return clean_input_text

def get_response(clean_input_text):
    reply = responses.get(clean_input_text, "I don't understand that yet. Try typing 'help'.")
    return reply

def run_chatbot():
    print("=" * 40)
    print("  DecoBot is Online. Type 'exit' to quit.")
    print("=" * 40)
    while True:
        clean_input_text = get_clean_input()
        if clean_input_text == "exit":
            print("DecoBot: Shutting down. Goodbye!")
            break
        if clean_input_text == "":
            print("DecoBot: Please type something!")
            continue
        reply = get_response(clean_input_text)
        print(f"DecoBot: {reply}")

run_chatbot()