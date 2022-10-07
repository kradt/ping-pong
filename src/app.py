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
		self.bind_events()

	def bind_events(self):
		self.bind("<Return>", lambda _: self.game.start_game())




