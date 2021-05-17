#import spacy, a module used by chatterbot
#spaCy is a NLP library in python
import spacy
spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')


#import dependancies
#ChatterBot is a Python library that generates automated responses to a user's input
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


#creating an instance of class ChatBot

#BestMatch helps Alpha select a proper response from the given list of responses
mybot = ChatBot(name='Alpha', read_only = True, logic_adapters = ['chatterbot.logic.BestMatch'])
