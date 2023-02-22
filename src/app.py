import tkinter as tk
import config
from .score import Score
from .game_filed import GameField


class App(tk.Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# Title Choice speed
		self.title_speed = tk.Label(text="Choice speed for ball: ", bg="black", fg="white")
		
		# Varibale for choice speed
		self.selected = tk.StringVar()
		self.selected.set(30)

		# RadioButtons choice speed
		self.speed_one = tk.Radiobutton(text="1", value=30, variable=self.selected)
		self.speed_two = tk.Radiobutton(text="2", value=20, variable=self.selected)
		self.speed_tree = tk.Radiobutton(text="3", value=10, variable=self.selected)

		# Button Start
		self.start = tk.Button(text="START", width=30, height=3, borderwidth=5,command=self.start_game)


		# Place all objects
		self.title_speed.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
		self.speed_one.place(relx=0.4, rely=0.2, anchor=tk.CENTER)
		self.speed_two.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
		self.speed_tree.place(relx=0.6, rely=0.2, anchor=tk.CENTER)
		self.start.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


	# fucntion initialize all objects and start game
	def start_game(self):
		self.score = Score(self)
		self.game = GameField(self)
		self.score.pack(side=tk.TOP)
		self.game.pack()
		self.game.start_game(self.selected.get())

	# function start app
	def run(self):
		self.mainloop()

		



