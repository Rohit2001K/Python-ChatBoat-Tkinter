import tkinter as tk
import random

class MatchNumbers:
    def __init__(self, root):
        self.root = root
        self.root.title("Match The Numbers")
        self.root.geometry('550x600')

        self.matching_numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
        random.shuffle(self.matching_numbers)

        self.attempts = 0
        self.selected_indices = []
        self.button_map = {}

        self.msg = tk.Label(root, text='Match The 2 Numbers', background='light blue')

        self.buttons = []
        for i in range(16):
            btn = tk.Button(root, text=' ', height=6, width=12, 
                            command=lambda b=i: self.button_click(b), background='yellow' if i % 2 == 0 else 'light blue')
            self.buttons.append(btn)

        self.msg.grid(row=0, column=2)
        for i, button in enumerate(self.buttons):
            row = i // 4 + 1
            col = i % 4
            button.grid(row=row, column=col, padx=10, pady=10)

        #restart game button
        reset_button=tk.Button(self.root,text='Restart',command=self.restart_game,background='light blue',width=15)
        reset_button.grid(row=9,column=2)

    def button_click(self, n):
        button = self.buttons[n]
        if button['text'] == ' ' and self.attempts < 2:
            button['text'] = self.matching_numbers[n]
            self.selected_indices.append(n)
            self.button_map[button] = self.matching_numbers[n]
            self.attempts += 1

        if self.attempts == 2:
            if self.matching_numbers[self.selected_indices[0]] == self.matching_numbers[self.selected_indices[1]]:
                self.attempts = 0
                self.selected_indices = []
                self.button_map = {}
                self.msg.config(text="Correct Match")
            else:
                self.msg.config(text="Oops wrong match")
                self.root.after(500, self.reset_buttons)

    def reset_buttons(self):
        for button in self.button_map:
            button['text'] = ' '
        self.attempts = 0
        self.selected_indices = []
        self.button_map = {}

    def restart_game(self):
        random.shuffle(self.matching_numbers)
        for button in self.buttons:
            button['text'] = ' '
        self.attempts = 0
        self.selected_indices = []
        self.button_map = {}

root = tk.Tk()
game = MatchNumbers(root)
root.mainloop()
