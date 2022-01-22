import tkinter as tk
from Interface.Styling import *


class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title = "O meu programa"
        self.configure(bg=BG_COLOR)

        #LEFT FRAME
        self._left_frame = tk.Frame(self, bg=BG_COLOR)
        self._left_frame.pack(side=tk.LEFT)

        self._txt1_label= tk.Label(self._left_frame, text="Texto Esquerda",bg = BG_COLOR)
        self._txt1_label.grid(row=0, column =0)


        #RIGHT FRAME
        self._right_frame = tk.Frame(self, bg=BG_COLOR)
        self._right_frame.pack(side=tk.LEFT)

        self._txt2_label = tk.Label(self._right_frame, text="Texto Esquerda", bg=BG_COLOR)
        self._txt2_label.grid(row=0, column=0)
