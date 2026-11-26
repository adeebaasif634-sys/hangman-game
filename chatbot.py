def chatbot():
    print("Chatbot: Hello! I am your basic chatbot. Type 'bye' to exit.")

    while True:
        # User se input lena aur lowercase mein convert karna
        user_input = input("You: ").strip().lower()

        # Conditions check karna
        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break  # Loop ko khatam karne ke liye
        else:
            print("Chatbot: Sorry, I don't understand that.")


# Function ko call karna
if __name__ == "__main__":
    chatbot()