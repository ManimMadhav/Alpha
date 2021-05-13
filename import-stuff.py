#import dependancies
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#creating an instance of class ChatBot

#BestMatch helps Alpha select a proper response from the given list of responses
mybot = ChatBot(name='Alpha', read_only = True, logic_adapters = ['chatterbot.logic.BestMatch'])
