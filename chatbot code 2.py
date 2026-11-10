import random # Importing the random module to add randomness to chatbot responses

#Defdining the chatbot class
class Chatbot:
    def __init__(self):
        #A list of possible greeting the chatbot can use to start a coversation
        self.greetings = [
            "Hello! How can I help you today :) ?",
            "Hey! How's it going?",
            "Greetings! How can I assist you?"
        ]
        self.jokes = [
            "What does a house wear? Address!",
            "How does NASA organize a party? They planet",
            "You know why you never see elephants hiding up in trees? Because they're really good at it.",
            "How come teddy bears never want to eat anything? Because they're always stuffed."
        ]

    def greet(self):
        return random.choice(self.greetings)
    
    def respond(self, user_input):
        # Convert input always to lowercase to handle case-insensitive matching
        user_input = user_input.lower()

        if user_input in ["hi", "hello", "hey"]:
            return self.greet()
        elif user_input == "how are you?":
            return "I'm just a bunch of code, but I'm here to help you!"
        elif user_input == "what's your name?":
            return "I'm your friendly Python chatbot!"
        elif user_input == "who created you?":
            return "I was created by a student of software engineering."
        elif user_input in ["tell me a joke","tell me another joke"]:
            return random.choice(self.jokes)
        else:
            return "I'm not sure how to respond to that."

# Immediately creates an instance of the Chatbot class
bot = Chatbot()
print(bot.greet()) #display an initial greeting when the program starts

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye! Have a great day!")
        break #breaks the loop to end the chat
    response = bot.respond(user_input)
    print(f"Chatbot: {response}") #using f so that the value of response is included into the response string
