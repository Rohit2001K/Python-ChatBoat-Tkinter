import tkinter
from tkinter import *
from PIL import Image , ImageTk
from random import randint
import os


class game:
    def __init__(self,root):
        self.root = root
        self.root.title("Rock Paper")
        self.root.configure(background="black")
        self.root.geometry("1150x500")
    
        #opening images

        #paper
        user_paper_img=Image.open(r'games\rock paper\images\user_paper.png')
        user_paper=ImageTk.PhotoImage(user_paper_img)

        bot_paper_img=Image.open(r'games\rock paper\images\bot_paper.png')
        bot_paper=ImageTk.PhotoImage(bot_paper_img)

        #stone
        user_stone_img=Image.open(r'games\rock paper\images\user_stone.png')
        user_stone=ImageTk.PhotoImage(user_stone_img)

        bot_stone_img=Image.open(r'games\rock paper\images\bot_stone.png')
        bot_stone=ImageTk.PhotoImage(bot_stone_img)

        #sc 
        user_sc_img=Image.open(r'games\rock paper\images\user_sc.jpg')
        user_sc=ImageTk.PhotoImage(user_sc_img)

        bot_sc_img=Image.open(r'games\rock paper\images\bot_sc.png')
        bot_sc=ImageTk.PhotoImage(bot_sc_img)

        #main UI
        user_indication=Label(root,font=50,text="You",bg="black",fg="white").grid(row=0,column=3)
        computer_indication=Label(root,font=50,text="Bot",bg="black",fg="white").grid(row=0,column=1)

        self.msg=Label(root,font=50,bg="black",fg="white",text="RPS GAME").grid(row=1,column=2)

        #user default option
        user=tkinter.Label(root,image=user_stone,bg="black")
        user.image=user_stone
        user.grid(row=1,column=4)

        #bot default option
        bot=tkinter.Label(root,image=bot_stone,bg="black")
        bot.image=bot_stone
        bot.grid(row=1,column=0)

        #score
        user_score=Label(root,text=0,font=100,fg="white",bg="black")
        user_score.grid(row=1,column=3)

        bot_score=Label(root,text=0,font=100,fg="white",bg="black")
        bot_score.grid(row=1,column=1)
        
        #user buttons
        rock=Button(root,width=20,height=2,text="ROCK",bg="gray",fg="white",command='').grid(row=2,column=1)
        paper=Button(root,width=20,height=2,text="Paper",bg="white",fg="black",command='').grid(row=2,column=2)
        sc=Button(root,width=20,height=2,text="Scissor",bg="yellow",fg="black",command='').grid(row=2,column=3)

        #functions

        #updated messages
        def update_msg(x):
            self.msg.config(text=x)

root = tkinter.Tk()
games=game(root)
root.mainloop()
