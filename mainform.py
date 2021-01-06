import random
import tkinter as tk
from tkinter import messagebox


class MainForm:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Game")
        self.root.geometry(f"200x100+300+300")
        self.root.resizable(False, False)
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        btn_1 = tk.Button(self.root, text="Press me")
        btn_1.bind("<Motion>", self.btn_1_move)
        btn_1.bind("<Button-1>", self.btn_1_click)
        btn_1.bind("<Return>", self.btn_1_click)
        btn_1.bind("<space>", self.btn_1_click)
        btn_1.pack(padx=20, pady=20, expand=1, fill=tk.BOTH)

    def move_form(self):
        new_x = random.randint(1, self.screen_width - 200)
        new_y = random.randint(1, self.screen_height - 200)
        self.root.geometry(f"+{new_x}+{new_y}")

    def btn_1_click(self, event):
        messagebox.showinfo("", "You WIN!!!")
        self.root.destroy()

    def btn_1_move(self, event):
        self.move_form()


if __name__ == '__main__':
    pass
