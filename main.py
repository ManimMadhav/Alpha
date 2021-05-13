#import dependancies
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#creating an instance of class ChatBot

mybot = ChatBot(name='Alpha', read_only = True, logic_adapters = ['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'])

#training the bot
#initially training the bot to a certain set of responses
social_talk = ['Hello.',
              'How are you?',
              'how do you do?',
              'hi there',
              'i/m okay',
              'i/m doing well',
              'i/m feeling awesome',
              'i was made by a human',
              'glad to hear from you!',
              'hope all is well and good',
              'stay safe from covid-19',
              'glad to hear this!',
              'idk if you guessed this, but i/m a bot!']

#feeding the list of strings to ListTrainer
list_train = ListTrainer(mybot)
list_train.train(social_talk)

string = input("Enter what you want to say to that bot:")
print(bot.get_response(string))
