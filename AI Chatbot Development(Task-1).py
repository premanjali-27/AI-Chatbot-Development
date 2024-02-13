import random

# Define responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks for asking!", "I'm doing well, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!"]
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return "I'm sorry, I didn't understand that."

# Main loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    else:
        print("Chatbot:", chatbot_response(user_input))