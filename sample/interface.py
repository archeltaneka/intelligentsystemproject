from tkinter import *
import tkinter.scrolledtext as st


root = Tk()  # main window of the GUI
user = StringVar()  # define user as string

# Rules for the ChatBot
ask = ["hi", "hello"]
hi = ["hi", "hello", "Hello too"]
error = ["sorry, i don't know", "what u said?"]


class ChatBotGUI(Frame):

    def __init__(self, *args, **kwargs):
        """
        Create & set window variables.
        """
        Frame.__init__(self, *args, **kwargs)

        self.pack()
        root.title("ChatBot GUI")
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

        if question in ask:
            self.conversation.insert(END, "Human: " + question + "\nChatBot: " + "Success" + "\n")
        else:
            self.conversation.insert(END, "Human: " + question + "\nChatBot: " + "Fail" + "\n")

        self.conversation['state'] = 'disabled'


gui = ChatBotGUI(root)
gui.mainloop()  # keeps the GUI open
