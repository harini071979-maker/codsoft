def chatbot():
    print("Hi! I'm a chatbot. Type 'bye' to exit.")
    while True:
        user = input("You: ").lower()
        if user == "hello":
            print("Bot: Hello!")
        elif user == "bye":
            print("Bot: Bye!")
            break
        else:
            print("Bot: I don't understand.")

chatbot()
