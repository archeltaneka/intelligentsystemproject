import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('MyBot')
bot.set_trainer(ListTrainer)

for _file in os.listdir('conv_list'):
    conversations = open('conv_list/' + _file, 'r').readlines()
    bot.train(conversations)

while True:
    try:
        req = input("Enter something: ")
        bot_response = bot.get_response(req)
        print("Bot: ", bot_response)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
