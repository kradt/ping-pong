import config
import tkinter as tk
from .items import Stick, Ball
from functools import lru_cache


class GameField(tk.Canvas):
	__left_x_coords = (20, 20)
	__right_x_coors = (config.FIELD_WIDTH-20, config.FIELD_WIDTH-20)

	def __init__(self, root):
		super().__init__(root, bg="black", width=config.FIELD_WIDTH, height=config.FIELD_HEIGHT)
		self.root = root
		self.start = tk.Label(text='Чтобы начать нажми ENTER', bg="black", fg="white")
		self.start.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

	@lru_cache()
	def start_game(self):
		'''
		Инициализируем обьекты ракеток и мяча
		Выполняеться после нажатия на кнопку ENTER
		'''
		self.start.destroy()
		self.left_stick = self.__create_stick(self.__left_x_coords)
		self.left_stick = Stick(self, self.left_stick, self.root.score.user1)

		self.right_stick = self.__create_stick(self.__right_x_coors)
		self.right_stick = Stick(self, self.right_stick, self.root.score.user2)

		self.ball = self.__create_ball()
		self.ball = Ball(self, self.ball)
		self.bind_events()
		self.ball.move_left()
	
	def __create_ball(self):
		x1 = int(self["width"]) / 2 - 20
		x2 = int(self["width"]) / 2 + 20
		y1 = int(self["height"]) / 2 + 20
		y2 = int(self["height"]) / 2 - 20
		return self.create_oval(x1, y1, x2, y2, fill="white")

	def __create_stick(self, x: tuple):
		y = self.get_height_of_stick()
		return self.create_line(x[0], y[0], x[1], y[1], fill="white", width=5)

	def bind_events(self):
		self.root.bind("<Down>", lambda _: self.right_stick.move_down())
		self.root.bind("<Up>", lambda _: self.right_stick.move_up())
		self.root.bind(("<s>"), lambda _: self.left_stick.move_down())
		self.root.bind(("<w>"), lambda _: self.left_stick.move_up())

	@staticmethod
	def get_height_of_stick():
		y1 = config.FIELD_HEIGHT / 3
		y2 =  config.FIELD_HEIGHT - y1
		return y1, y2


