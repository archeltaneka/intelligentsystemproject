import os
from PIL import Image
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'MyBot',
    trainer='chatterbot.trainers.ListTrainer'
)
bot.set_trainer(ListTrainer)

for _file in os.listdir('conv_list'):
    conversations = open('conv_list/' + _file, 'r').readlines()
    bot.train(conversations)

while True:
    try:
        req = input("Enter something: ")
        if req == "show negative words":
            img = Image.open('./src/negativewords.png')
            img.show()
        elif req == "show positive words":
            img = Image.open('./src/positivewords.png')
            img.show()
        elif req == "top 10 positive tags":
            img = Image.open('./src/top10positivetags.png')
            img.show()
        elif req == "top 10 negative tags":
            img = Image.open('./src/top10negativetags.png')
            img.show()
        else:
            bot_response = bot.get_response(req)
            print("Bot: ", bot_response)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
