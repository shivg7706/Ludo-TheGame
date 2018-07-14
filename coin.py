import tkinter as tk
from PIL import ImageTk, Image

from settings import *

class Coin:

    def __init__(self, master, x, y, color, coin_index):
        self.canvas = master
        self.curr_x = x
        self.curr_y = y
        self.home_x = x
        self.home_y = y
        self.color = color
        self.coin_index = coin_index
        self.coin = ImageTk.PhotoImage(Image.open('./assets/' + color + '.gif'))
        self.img =  self.canvas.create_image(x, y, anchor=tk.NW, image=self.coin)

