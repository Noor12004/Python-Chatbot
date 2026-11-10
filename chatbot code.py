import random

class Chatbot:
    def __init__(self):
        self.greetings = [
            "Hello!", "Hi there!", "Greetings!", "Howdy!", "Hey!"
        ]
        self.jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you get if you cross a snowman and a vampire? Frostbite."
        ]

    def get_greeting(self):
        return random.choice(self.greetings)

    def respond(self, user_input):
        user_input = user_input.lower()
        if user_input in ["how are you?", "what's your name?"]:
            return self.handle_specific_questions(user_input)
        elif user_input == "who created you?":
            return "I was created by a student."
        elif user_input == "tell me a joke":
            return random.choice(self.jokes)
        else:
            return "I'm not sure how to respond to that."

    def handle_specific_questions(self, user_input):
        responses = {
            "how are you?": "I'm just a bunch of code, but I'm here to help you!",
            "what's your name?": "I'm your friendly chatbot."
        }
        return responses.get(user_input, "I'm not sure how to respond to that.")

if __name__ == "__main__":
    bot = Chatbot()
    print(bot.get_greeting())
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = bot.respond(user_input)
        print(f"Chatbot: {response}")
