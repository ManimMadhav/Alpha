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
bot = ChatBot(name='Alpha', read_only = True, logic_adapters = ['chatterbot.logic.BestMatch'])



# training the bot

# initially training the bot to a certain set of responses
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
               'stay safe',
               'glad to hear this!',
               'i/m a bot!']




# feeding the list of strings to ListTrainer
list_train = ListTrainer(bot)
list_train.train(social_talk)


#after training the bot
#return an output to the user
#use get_response function to feed an input to Alpha and consequently return an output

print(bot.get_response("Hi"))
