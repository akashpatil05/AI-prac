# Advanced Customer Support Chatbot using Python and NLTK

import nltk
from nltk.chat.util import Chat, reflections

# Question and Answer Patterns
pairs = [

    [
        r"hi|hello|hey",
        ["Hello! Welcome to TechStore Support 😊",
         "Hi there! How can I assist you today?"]
    ],

    [
        r"my name is (.*)",
        ["Hello %1! Nice to meet you 😊"]
    ],

    [
        r"how are you ?",
        ["I am doing great! What about you?"]
    ],

    [
        r"i am fine",
        ["Glad to hear that! How can I help you today?"]
    ],

    [
        r"what is your name ?",
        ["I am SmartBot, your virtual customer assistant 🤖"]
    ],

    [
        r"(.*) product",
        ["We provide laptops, smartphones, smartwatches, and headphones."]
    ],

    [
        r"(.*) price",
        ["Our product prices start from Rs. 5000 onwards."]
    ],

    [
        r"(.*) order status",
        ["Please share your Order ID to check the status."]
    ],

    [
        r"(.*) delivery",
        ["Delivery usually takes 3 to 5 business days."]
    ],

    [
        r"(.*) payment",
        ["We accept UPI, Credit Card, Debit Card, and Cash on Delivery."]
    ],

    [
        r"(.*) refund",
        ["Refund will be processed within 7 working days."]
    ],

    [
        r"(.*) contact",
        ["You can contact us at support@techstore.com"]
    ],

    [
        r"(.*) thanks|thank you",
        ["You're welcome 😊",
         "Happy to help you!"]
    ],

    [
        r"bye|quit",
        ["Thank you for visiting TechStore. Have a great day 😊"]
    ],

    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you try again?"]
    ]
]

# Chatbot Function
def start_chat():
    print("=" * 50)
    print("      TECHSTORE CUSTOMER SUPPORT BOT")
    print("=" * 50)
    print("Type 'bye' to exit the chatbot.\n")

    chatbot = Chat(pairs, reflections)
    chatbot.converse()

# Main Program
if __name__ == "__main__":
    start_chat()