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
        self.user_paper=ImageTk.PhotoImage(user_paper_img)

        bot_paper_img=Image.open(r'games\rock paper\images\bot_paper.png')
        self.bot_paper=ImageTk.PhotoImage(bot_paper_img)

        #stone
        user_stone_img=Image.open(r'games\rock paper\images\user_stone.png')
        self.user_stone=ImageTk.PhotoImage(user_stone_img)

        bot_stone_img=Image.open(r'games\rock paper\images\bot_stone.png')
        self.bot_stone=ImageTk.PhotoImage(bot_stone_img)

        #sc 
        user_sc_img=Image.open(r'games\rock paper\images\user_sc.jpg')
        self.user_sc=ImageTk.PhotoImage(user_sc_img)

        bot_sc_img=Image.open(r'games\rock paper\images\bot_sc.png')
        self.bot_sc=ImageTk.PhotoImage(bot_sc_img)

        #main UI
        user_indication=Label(root,font=50,text="You",bg="black",fg="white").grid(row=0,column=3)
        computer_indication=Label(root,font=50,text="Bot",bg="black",fg="white").grid(row=0,column=1)

        self.msg=Label(root,font=50,bg="black",fg="white",text="RPS GAME")
        self.msg.grid(row=1,column=2)

        #user default option
        self.user=tkinter.Label(root,image=self.user_stone,bg="black")
        self.user.image=self.user_stone
        self.user.grid(row=1,column=4)

        #bot default option
        self.bot=tkinter.Label(root,image=self.bot_stone,bg="black")
        self.bot.image=self.bot_stone
        self.bot.grid(row=1,column=0)

        #score
        self.user_score=Label(root,text=0,font=100,fg="white",bg="black")
        self.user_score.grid(row=1,column=3)

        self.bot_score=Label(root,text=0,font=100,fg="white",bg="black")
        self.bot_score.grid(row=1,column=1)
        
        #user buttons
        rock=Button(root,width=20,height=2,text="ROCK",bg="gray",fg="white",command=lambda:self.game_choices("rock"))
        rock.grid(row=2,column=1)
        paper=Button(root,width=20,height=2,text="Paper",bg="white",fg="black",command=lambda:self.game_choices("paper"))
        paper.grid(row=2,column=2)
        sc=Button(root,width=20,height=2,text="Scissor",bg="yellow",fg="black",command=lambda:self.game_choices("sc"))
        sc.grid(row=2,column=3)

    #functions

    #updating messages
    def update_msg(self,msg):
        self.msg.config(text=msg)
        
    #update user socre
    def update_user_score(self):
        score=int(self.user_score['text'])
        score+=1
        self.user_score["text"]=str(score)

    #update bot socre
    def update_bot_score(self):
        score=int(self.bot_score['text'])
        score+=1
        self.bot_score["text"]=str(score)

    #main functon
    def game_logic(self,user_input,bot_input):
        if user_input == bot_input:
            self.update_msg(f'It\'s a TIE!')

        # Check for Rock choice
        elif user_input == 'rock':
            if bot_input == 'sc':
                self.update_msg(f'Bot loses!')
                self.update_user_score()
            else:
                self.update_msg(f'Bot wins!') 
                self.update_bot_score()
        
        # Check for Paper choice
        elif user_input == 'paper':
            if bot_input == 'sc':
                self.update_msg(f'Bot wins!')
                self.update_bot_score()
            else:
                self.update_msg(f'You win!')
                self.update_user_score()
        
        # Check for Scissors choice
        elif user_input == 'sc':
            if bot_input == 'rock':
                self.update_msg(f'Bot wins!')
                self.update_bot_score()
            else:
                self.update_msg(f'You win!') 
                self.update_user_score()
    
        else:
            self.update_msg('Invalid input! Please choose Rock, Paper, or Scissors.')

    #bot choices/ user
    def game_choices(self,user_choose):
        bot_choices=['rock','paper','sc'] 
        bot_choose=bot_choices[randint(0,2)]
        # bot images updation
        if bot_choose=="sc":
            self.bot.config(image=self.bot_sc)
        elif bot_choose=="rock":
            self.bot.config(image=self.bot_stone)    
        else:
            self.bot.config(image=self.bot_paper) 

        #user image updations
        if user_choose=="sc":
            self.user.config(image=self.user_sc)
        elif user_choose=="rock":
            self.user.config(image=self.user_stone)    
        elif user_choose=='paper':
            self.user.config(image=self.user_paper)    

        #calling main game logic function    
        self.game_logic(user_choose, bot_choose)


root = tkinter.Tk()
games=game(root)
root.mainloop()
