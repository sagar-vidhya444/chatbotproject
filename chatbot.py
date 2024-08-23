import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you.",]
    ],
    [
        r"how are you?",
        ["I'm doing good, thank you!", "I'm great, how about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay", "No problem",]
    ],
    [
        r"I am (.*) (good|well|okay|fine)",
        ["Nice to hear that!", "Alright, great!",]
    ],
    [
        r"(.*) age?",
        ["I'm ageless!",]
    ],
    [
        r"(.*) created?",
        ["I was created by a programmer.",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am a virtual being, I exist everywhere.']
    ],
    [
        r"how can I (.*)",
        ["You can try asking me specific questions.",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! Have a nice day.",]
    ],
[
        r"please",
        ["don't say please",]
    ],
    [
        r"(.*)",
        ["Sorry, I don't understand. Can you please rephrase?",]
    ],
]

# Create a chatbot
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Hi, I am your chatbot. How can I help you?")
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        print("Goodbye! Have a nice day.")
        break
    response = chatbot.respond(user_input)
    print(response)