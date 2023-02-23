import tkinter as tk
import config
from .score import Score
from .game_filed import GameField


class Settings(tk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs, bg="black")
		# Title Choice speed
		self.title_speed = tk.Label(text="Choice speed for ball: ", bg="black", fg="white")
		
		# Varibale for choice speed
		self.selected = tk.StringVar()
		self.selected.set(30)

		# RadioButtons choice speed
		self.speed_one = tk.Radiobutton(text="1", value=30, variable=self.selected)
		self.speed_two = tk.Radiobutton(text="2", value=20, variable=self.selected)
		self.speed_tree = tk.Radiobutton(text="3", value=10, variable=self.selected)

		# Place all objects
		self.title_speed.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
		self.speed_one.place(relx=0.4, rely=0.2, anchor=tk.CENTER)
		self.speed_two.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
		self.speed_tree.place(relx=0.6, rely=0.2, anchor=tk.CENTER)

	def destroy(self):
		self.title_speed.destroy()
		self.speed_one.destroy()
		self.speed_two.destroy()
		self.speed_tree.destroy()


class App(tk.Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.create_settings()
		
	# Create frame with feature of choice speed
	def create_settings(self):
		"""
		Use in __init__ and in repeat_game_methood
		"""
		self.settings_frame = Settings(width=200, height=100)
		self.settings_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
		# Button for start game
		self.start = tk.Button(self.settings_frame, text="START", width=30, height=3, borderwidth=5, command=self.init_game)
		self.start.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

	# Delete frame with settings
	def destroy_settings(self):
		"""
		Use in start_game methood
		"""
		self.settings_frame.destroy()
		self.start.destroy()

	# Method for repeat game
	def repeat_game(self):
		"""
		Use in GameField Object when game was ended
		"""
		# remove interface for repeat game
		self.game.repeat_label.destroy()
		self.game.button_repeat.destroy()
		self.game.button_exit.destroy()
		# Remove game canvas
		self.game.destroy()
		# Remove Score frame 
		self.score.destroy()
		self.create_settings()
	
	# Method delete settings frame and init gamefield and score frame
	def init_game(self):
		self.destroy_settings()
		self.score = Score(self)
		self.game = GameField(self)
		# Place all objects
		self.score.pack(side=tk.TOP)
		self.game.pack()
		# Create all objects as ball and stick and start move ball
		self.game.start_game(speed=self.settings_frame.selected.get())

	# function start loop for app
	def run(self):
		self.mainloop()

		



