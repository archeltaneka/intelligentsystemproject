from tkinter import *
import tkinter.scrolledtext as st
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
from PIL import Image

root = Tk()  # main window of the GUI
user = StringVar()  # define user as string

# Rules for the ChatBot
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


class ChatBotGUI(Frame):

    def __init__(self, *args, **kwargs):
        """
        Create & set window variables.
        """
        Frame.__init__(self, *args, **kwargs)

        self.pack()
        root.title("ChatBot GUI")
        self.configure(background='grey')
        self.make_widgets()

    def make_widgets(self):
        """
        Content of the root window
        """
        # Query Button
        self.btn_query = Button(self, text="Get Response", command=self.get_response)
        self.btn_query.grid(column=0, row=0, sticky='nesw', padx=5, pady=5)

        # Text Box
        self.txt_query = Entry(self, textvariable=user)
        self.txt_query.grid(column=1, row=0, sticky='nesw', padx=5, pady=5)

        # Display Following Text
        self.lbl_conversation = Label(self, anchor=CENTER, text='Conversation')
        self.lbl_conversation.grid(column=0, row=1, columnspan=2, sticky='nesw', padx=5, pady=5)

        # Conversation Box
        self.conversation = st.ScrolledText(self, state='disabled')
        self.conversation.grid(column=0, row=2, columnspan=2, sticky='nesw', padx=5, pady=5)

    def get_response(self):
        """
        Get a response from the ChatBot and display it.
        """
        question = user.get()

        self.conversation['state'] = 'normal'

        # check for user input
        if any(word in question.lower() for word in NEG_WORDS):
            self.conversation.insert(END, "Human: " + question + "\nChatBot: " + "Opening..." + "\n")
            img = Image.open('./src/negativewords.png')
            img.show()
        elif any(word in question.lower() for word in POS_WORDS):
            self.conversation.insert(END, "Human: " + question + "\nChatBot: " + "Opening..." + "\n")
            img = Image.open('./src/positivewords.png')
            img.show()
        elif any(word in question.lower() for word in POS_TAGS):
            self.conversation.insert(END, "Human: " + question + "\nChatBot: " + "Opening..." + "\n")
            img = Image.open('./src/top10positivetags.png')
            img.show()
        elif any(word in question.lower() for word in NEG_TAGS):
            self.conversation.insert(END, "Human: " + question + "\nChatBot: " + "Opening..." + "\n")
            img = Image.open('./src/top10negativetags.png')
            img.show()
        else:
            bot_response = bot.get_response(question)
            self.conversation.insert(END, "Human: " + question + "\nChatBot: " + str(bot_response) + "\n")
        # if question in ask:
        #     self.conversation.insert(END, "Human: " + question + "\nChatBot: " + "Success" + "\n")
        # else:
        #     self.conversation.insert(END, "Human: " + question + "\nChatBot: " + "Fail" + "\n")

        self.conversation['state'] = 'disabled'


gui = ChatBotGUI(root)
gui.mainloop()  # keeps the GUI open
