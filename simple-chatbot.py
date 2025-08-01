print("Simple Chatbot (type 'exit' to quit)\n")
while True:
    user_input = input("You: ").strip().lower()
    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello!")
    elif user_input == "bye":
        print("Bot: Goodbye!")
    elif user_input == "how are you":
        print("Bot: I'm just a bot, but I'm doing fine!")
    elif user_input == "what is your name":
        print("Bot: I'm a simple chatbot.")
    elif user_input == "exit":
        print("Bot: Chat ended.")
        break
    else:
        print("Bot: Sorry, I don't understand that.") 
