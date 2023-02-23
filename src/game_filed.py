import tkinter as tk
from functools import lru_cache

import config
from .items import Stick, Ball



class GameField(tk.Canvas):
	__left_x_coords = (20, 20)
	__right_x_coors = (config.FIELD_WIDTH-20, config.FIELD_WIDTH-20)

	def __init__(self, root):
		super().__init__(root, bg="black", width=config.FIELD_WIDTH, height=config.FIELD_HEIGHT)
		self.root = root

	# Init all game objects and start move ball to left
	def start_game(self, speed):
		"""
		Use in App object in init_game methood
		"""
		self.speed = speed
		# Create left stick and his object for handle his move
		self.left_stick = self.__create_stick(self.__left_x_coords)
		self.left_stick = Stick(self, self.left_stick, self.root.score.user1)
		# Create right stick and his object for handle his move
		self.right_stick = self.__create_stick(self.__right_x_coors)
		self.right_stick = Stick(self, self.right_stick, self.root.score.user2)
		# Create ball and his object for handle his move
		self.ball = self.__create_ball()
		self.ball = Ball(self, self.ball, self.speed)
		# bind all keys for manage all objects
		self.bind_events()
		# start move methood
		self.ball.move_left()
	
	# Method create oval as Ball from size of gamefield
	def __create_ball(self):
		x1 = int(self["width"]) / 2 - 20
		x2 = int(self["width"]) / 2 + 20
		y1 = int(self["height"]) / 2 + 20
		y2 = int(self["height"]) / 2 - 20
		return self.create_oval(x1, y1, x2, y2, fill="white")

	# Method create line as stick from class coords of side gamefield and height of stick
	def __create_stick(self, x: tuple):
		y = self.get_height_of_stick()
		return self.create_line(x[0], y[0], x[1], y[1], fill="white", width=5)

	# Method bind all keys for use objects methood
	def bind_events(self):
		self.root.bind("<Down>", lambda _: self.right_stick.move_down())
		self.root.bind("<Up>", lambda _: self.right_stick.move_up())
		self.root.bind(("<s>"), lambda _: self.left_stick.move_down())
		self.root.bind(("<w>"), lambda _: self.left_stick.move_up())

	# Methood end of game remove all objects from canvas and add interface for start repeat game
	def end_of_game(self):
		self.ball.stop()
		del self.ball, self.left_stick, self.right_stick
		# text for buttons 
		self.repeat_label = tk.Label(text="Do u want to repeat? ", bg="black", fg="white")
		# Button yes or no 
		self.button_repeat = tk.Button(text="YES", command=self.root.repeat_game)
		self.button_exit = tk.Button(text="NO", command=self.root.destroy)
		# Place all objects
		self.repeat_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
		self.button_repeat.place(relx=0.45, rely=0.4, anchor=tk.CENTER)
		self.button_exit.place(relx=0.55, rely=0.4, anchor=tk.CENTER)

	@staticmethod
	def get_height_of_stick():
		y1 = config.FIELD_HEIGHT / 3
		y2 =  config.FIELD_HEIGHT - y1
		return y1, y2
