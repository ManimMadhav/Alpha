#after training the bot
#return an output to the user

string = input("Enter what you want to say to that bot:")

#use get_response function to feed an input to Alpha
print(bot.get_response(string))
