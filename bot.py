import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import pyttsx3
import json


# Initialize the pyttsx3 engine



class chatbot:
    def __init__(self, root):
        self.root = root

        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 190)

        # Window icon config
        icon_img = Image.open(r'others\logo.png')
        icon_img_open = ImageTk.PhotoImage(icon_img)

        # Window config
        self.root.title("PyChatBot")
        self.root.configure(bg='light blue')
        self.root.iconphoto(True, icon_img_open)
        self.root.geometry("500x550")

        # main img
        cover_img = Image.open(r'others\bot.png')
        cover_img_config = ImageTk.PhotoImage(cover_img)

        # main img label
        cover_img_label = tk.Label(root, image=cover_img_config, bg='light blue')
        cover_img_label.image = cover_img_config
        cover_img_label.grid(row=1, column=2)

        # pre define texts
        self.predefine_text = ['game', 'google', 'google search']

        # icons/UI
        self.bot_message = tk.Label(self.root, text='BOT : ', background='#FFFF99', font=(15))
        self.bot_message.grid(row=2, column=2, columnspan=2)

        self.user_input = tk.Entry(self.root, width=50)
        self.user_input.grid(row=3, column=2)

        submit_button = tk.Button(self.root, text="Submit", command=self.read_user_input, width=30, bg='blue', font=('', 12, 'bold'))
        submit_button.grid(row=4, column=2)

    # main matching function
    def match_most_related_word(self, sentence, words):
        res = [all([k in s for k in words]) for s in sentence]
        return [sentence[i] for i in range(0, len(res)) if res[i]]

    # read file and return keys
    def read_file(self):
        try:
            file = open(r'others\dialogues.txt', 'r+')
            self.json_file = json.loads(file.read())
            keys = list(self.json_file.keys())
            return keys
        except:
            print("ERROR IN OPENING .TXT FILE")

    # read user input and check in txt file
    def read_user_input(self):
        words = self.user_input.get()  
        split_words = words.split()
        list_of_words = self.read_file()
        if list_of_words:
            for word in split_words:
                check_word = self.match_most_related_word(list_of_words, word)

            check_word_value = check_word[0]   
            bot_reply = self.json_file[check_word_value]  
            self.bot_message.config(text="BOT : "+bot_reply)
            self.engine.say(bot_reply)
            self.engine.runAndWait() 


root = tk.Tk()
bot = chatbot(root)
root.mainloop()
