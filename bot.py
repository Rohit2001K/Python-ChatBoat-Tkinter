import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import pyttsx3
import json
from tkinter import END
from pywhatkit import search
from tkinter.ttk import *
import subprocess
import os

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
        self.root.geometry("600x650")

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

        # Make submit_button an attribute of the class
        self.submit_button = tk.Button(self.root, text="Submit", command=self.read_user_input, width=30, bg='blue', font=('', 12, 'bold'))
        self.submit_button.grid(row=4, column=2)

    # main matching function
    def match_most_related_word(self, sentence, word):
        res = [word in s for s in sentence]
        if any(res):
            return [sentence[i] for i in range(len(res)) if res[i]]
        else:
            return False

    # read file and return keys
    def read_file(self):
        try:
            file = open(r'others\dialogues.txt', 'r+')
            self.json_file = json.loads(file.read())
            keys = list(self.json_file.keys())
            return keys
        except:
            print("ERROR IN OPENING .TXT FILE")

    # google search
    def perform_google_search(self, event=None):
        search_query = self.user_input.get()
        if search_query:
            search(search_query)  
            self.bot_message.config(text=f"BOT: Searching Google for '{search_query}'...")  
            self.user_input.delete(0, END)
            self.reset_bot()  # Reset bot after search

    def search_for_google(self):
        self.user_input.bind("<Return>", self.perform_google_search)
        self.submit_button.config(command=self.perform_google_search)

    def reset_bot(self):
        self.bot_message.config(text="BOT : How can I assist you today?")
        self.user_input.delete(0, END)
        self.user_input.unbind("<Return>")  
        self.submit_button.config(command=self.read_user_input)  

    # game selection
    def game_start(self, game):
        if game == 'Fighting Badguys':
            self.open_game_from_path('games/fighting game/game.py')
            self.option_button.forget()
            self.option.forget()
            self.submit_button.grid(row=4, column=2)

        elif game == 'Rock Paper Scissors':
            print("THE IS ROCK PAPER TEST")
        elif game == 'Match the Number':
            print("THE IS MATCH THE NUMBER TEST")

    def open_game_from_path(self, game_path):
        try:
            if os.path.exists(game_path):  
                subprocess.Popen(['python', game_path]) 
            else:
                raise FileNotFoundError(f"Game file not found: {game_path}")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Could not open the game. Error: {str(e)}")

    def read_user_input(self):
        words = self.user_input.get()
        split_words = words.split()
        list_of_words = self.read_file()

        if list_of_words:
            found_match = False
            for word in split_words:
                check_word = self.match_most_related_word(list_of_words, word)

                if check_word:
                    found_match = True
                    check_word_value = check_word[0]
                    bot_reply = self.json_file[check_word_value]
                    self.bot_message.config(text="BOT: " + bot_reply)
                    self.user_input.delete(0, END)
                    self.engine.runAndWait()
                    break
                else:
                    check_word = self.match_most_related_word(self.predefine_text, word)
                    if check_word:
                        found_match = True
                        if check_word[0] == "google":
                            bot_reply = "What would you like to search on Google? Please type below!"
                            self.bot_message.config(text="BOT: " + bot_reply)
                            self.user_input.delete(0, END)
                            self.search_for_google() 
                            break
                        elif check_word[0] == 'game':
                            bot_reply = "Please select the game!"
                            self.bot_message.config(text="BOT: " + bot_reply)
                            self.user_input.delete(0, END)
                            self.option = Combobox(self.root)
                            self.option['values'] = ('Fighting Badguys', "Rock Paper Scissors", "Match the Number")
                            self.option.grid(row=4, column=2)
                            self.submit_button.forget()
                            self.option_button = tk.Button(self.root, text="Select Game", command=lambda: self.game_start(self.option.get()), width=30, bg='blue', font=('', 12, 'bold'))
                            self.option_button.grid(row=6, column=2)
                            break

            if not found_match:
                print("WAIT")
        else:
            print("NO FILE FOUND")
            self.bot_message.config(text="BOT: Error - No file found.")

root = tk.Tk()
bot = chatbot(root)
root.mainloop()
