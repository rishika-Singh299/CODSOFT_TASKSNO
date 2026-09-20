# CODSOFT AI Internship
# Task 1: Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    
    if user_input in ["hello", "hi", "hey", "hii"]:
        return "Hello! How can I help you?"

  
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    
    elif "rishika" in user_input or "who are you" in user_input:
        return "I'm a simple Rule-Based AI Chatbot."

    
    elif "help" in user_input:
        return "Sure! You can ask me about my name, time, or say hello."

    
    elif "internship" in user_input:
        return "This chatbot is created as Task 1 of the CODSOFT AI Internship."
 elif "thank" in user_input:
        return "You're welcome!"

    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that. Please try another question."


# Main chatbot loop
print("================================")
print("     Rule-Based AI Chatbot")
print("================================")
print("Type 'bye' to exit the chatbot.\n")

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)
    print("Bot:", response)

    if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
        break
