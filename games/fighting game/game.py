import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from basic import player, enemy

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Fighting Kid")
        self.root.geometry("900x550")
        self.player = player()
        self.enemy_level=1
        self.enemy = enemy(self.enemy_level)

        # User states showcase 

        self.user_hp = Label(self.root, text=f"Your HP : {self.player.hp}", font=('Helvetica', 14), bg='green', fg='black',width=20)
        self.user_hp.grid(row=0, column=1, padx=10, pady=10)

        self.user_power = Label(self.root, text=f"Your Power : {self.player.power}", font=('Helvetica', 14), bg='light blue', fg='black',width=20)
        self.user_power.grid(row=1, column=1, padx=10, pady=10)

        self.iteam_msg = Label(self.root, text=f"You Get : Nothing", font=('Helvetica', 14), bg='Yellow', fg='black')
        self.iteam_msg.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

        # Button for user action
        self.user_punch_button = Button(self.root, text='Punch (-10 Power)', bg='pink', fg='black', width=20, height=2, command=self.user_punch)
        self.user_punch_button.grid(row=4, column=1, padx=10, pady=10)

        self.user_kick_button= Button(self.root, text='Kick (-10 Power)',bg='pink', fg='black', width=20, height=2, command=self.user_kick)
        self.user_kick_button.grid(row=4, column=2, padx=10, pady=10)
        # User icon
        try:
            uicon = Image.open(r'games\fighting game\images\placeholder_user.jpg')
            uicon = uicon.resize((300, 300))
            self.user_icon = ImageTk.PhotoImage(uicon)
            self.user_icon_label = Label(self.root, image=self.user_icon)
            self.user_icon_label.grid(row=2, column=1, padx=10, pady=10)
            self.root.iconphoto(True, self.user_icon)
        except:
            self.user_icon_error = Label(self.root, text=f"Error in loading user_icon", bg='red', fg='black')
            self.user_icon_error.grid(row=1, column=3)



        # Enemy showcase
        self.enemy_hp = Label(self.root, text=f"Enemy HP: {self.enemy.hp}", font=('Helvetica', 14), bg='Red', fg='black', width=20)
        self.enemy_hp.grid(row=1, column=15)

        # Enemy icon
        try:
            eicon = Image.open(r'games\fighting game\images\placeholder_enemy.png')
            eicon = eicon.resize((300, 300))
            self.enemy_icon = ImageTk.PhotoImage(eicon)
            self.enemy_icon_label = Label(self.root, image=self.enemy_icon)
            self.enemy_icon_label.grid(row=2, column=15, padx=10, pady=10)
            self.root.iconphoto(True, self.enemy_icon)
        except:
            self.enemy_icon_error = Label(self.root, text=f"Error in loading enemy_icon", bg='red', fg='black')
            self.enemy_icon_error.grid(row=2, column=15)

    def update_game(self):
        self.user_hp.config(text=f"Your HP : {self.player.hp}")
        self.user_power.config(text=f"Your Power : {self.player.power}")
        self.enemy_hp.config(text=f"Enemy HP: {self.enemy.hp}")


#User Kick and Punch
    def user_punch(self):
        self.player.punch(self.enemy)
        if self.player.punch(self.enemy)==False:
            action = self.enemy.attack(self.player)
            self.iteam_msg.config(text=f"Not Enough Power, Enemy Hit You : {action}")
        action = self.enemy.attack(self.player)
        self.iteam_msg.config(text=f"You Get : {action}")
        self.update_game()
        self.win_lose()


    def user_kick(self):
        self.player.kick(self.enemy)
        if self.player.kick(self.enemy)==False:
            action = self.enemy.attack(self.player)
            self.iteam_msg.config(text=f"Not Enough Power, Enemy Hit You : {action}")
        action = self.enemy.attack(self.player)
        self.iteam_msg.config(text=f"You Get : {action}")
        self.update_game()
        self.win_lose()


#checking game for winner and loser (HP)

    def win_lose(self):
        if self.player.hp_checker()==False:
            self.iteam_msg.config(text=f"You Lose :(")
            self.user_punch_button.config(state=tk.DISABLED,bg='red',fg='white')
            self.user_kick_button.config(state=tk.DISABLED,bg='red',fg='white')
        elif self.enemy.hp_checker()==False:
            self.iteam_msg.config(text=f"You Win ,Enemy Getting Stronger now(Iteams Drop Rate -)")
            self.enemy_levelup()



    def enemy_levelup(self):
        self.enemy_level+=1
        self.enemy=enemy(self.enemy_level)
        self.update_game()
        


root = tk.Tk()
game = Game(root)
root.mainloop()
