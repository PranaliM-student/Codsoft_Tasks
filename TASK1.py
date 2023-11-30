class RuleBasedChatbot:
    def __init__(self):
        self.responses = {
            "hello": "Hi there! How can I help you?",
            "how are you": "I'm just a computer program, but thanks for asking!",
            "bye": "Goodbye! Have a great day.",
            "thank you": "You're welcome!",
            "what's your name": "I'm a chatbot. You can call me Bot.",
            "who created you": "I was created by a programmer using Python.",
            "tell a joke": "Why don't scientists trust atoms? Because they make up everything!",
            "how old are you": "I don't have an age. I'm just a program.",
            "default": "I'm sorry, I don't understand. Can you please rephrase?",
        }

    def get_response(self, user_input):
        # Convert user input to lowercase for case-insensitive matching
        user_input = user_input.lower()

        # Check if there's a specific response for the user input
        response = self.responses.get(user_input, self.responses["default"])
        return response

def main():
    chatbot = RuleBasedChatbot()

    print("Rule-Based Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Rule-Based Chatbot: Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print("Rule-Based Chatbot:", response)

if __name__ == "__main__":
    main()
