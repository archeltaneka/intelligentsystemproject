import os
from PIL import Image
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

NEG_WORDS = ["show negative words", "negative words"]
POS_WORDS = ["show positive words", "positive words"]
POS_TAGS = ["positive tags", "10 positive tags", "top positive tags", "top 10 positive tags"]
NEG_TAGS = ["negative tags", "10 negative tags", "top negative tags", "top 10 negative tags"]

# create a new bot with specified trainer
bot = ChatBot(
    'MyBot',
    trainer='chatterbot.trainers.ListTrainer'
)
bot.set_trainer(ListTrainer)

# gather knowledge for the bot
for _file in os.listdir('conv_list'):
    conversations = open('conv_list/' + _file, 'r').readlines()
    bot.train(conversations)

# user input and bot responses
while True:
    try:
        req = input("Enter something: ")
        if any(word in req.lower() for word in NEG_WORDS):
            img = Image.open('./src/negativewords.png')
            img.show()
        elif any(word in req.lower() for word in POS_WORDS):
            img = Image.open('./src/positivewords.png')
            img.show()
        elif any(word in req.lower() for word in POS_TAGS):
            img = Image.open('./src/top10positivetags.png')
            img.show()
        elif any(word in req.lower() for word in NEG_TAGS):
            img = Image.open('./src/top10negativetags.png')
            img.show()
        else:
            bot_response = bot.get_response(req)
            print("Bot: ", bot_response)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
