#defining chatbot
def bot():
        print("Hi, I'm the chatbot you built") 

bot()

#training chat with provided list social_talk
chat = Chat(social_talk, reflections)

#converse function triggers the conversation
chat.converse()
if __name__ == "__main__":
    bot()
