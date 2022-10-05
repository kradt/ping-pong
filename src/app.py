import config
import tkinter as tk
from .score import Score
from .game_filed import GameField


class App(tk.Tk):
	def __init__(self):
		super().__init__()

		self.score = Score(self)
		self.score.pack(side=tk.TOP)
		self.game = GameField(self)
		self.game.pack()
		self.binds_all_events()
		
	
	def binds_all_events(self):
		self.bind("<Down>", lambda _: self.game.right_stick.move_down())
		self.bind("<Up>", lambda _: self.game.right_stick.move_up())
		self.bind("<KeyPress-s>", lambda _: self.game.left_stick.move_down())
		self.bind("<KeyPress-w>", lambda _: self.game.left_stick.move_up())
		self.bind("<Return>", lambda _: self.game.start_game())




