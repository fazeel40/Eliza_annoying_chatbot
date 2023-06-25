import nltk
from nltk.chat.util import Chat, reflections
from nltk.chat import eliza

# Initialize the chatbot
pairs = eliza.pairs
chatbot = Chat(pairs, reflections)

# Generate responses
def generate_response(input):
    response = chatbot.respond(input)
    return response

# Main loop
print("Hello, I am Chatbot. How can I assist you today?")
while True:
    user_input = input("You: ")
    response = generate_response(user_input)
    print("Chatbot:", response)
    if user_input.lower() == "bye":
        break
