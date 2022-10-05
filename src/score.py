import tkinter as tk
import config


class User():
	def __init__(self):
		self.score = 0

	def point_to_user(self):
		self.score +=1


class Score(tk.Frame):
	__result = "{} : {}"

	def __init__(self, root):
		super().__init__(root, width=config.HEADER_WIDTH, height=config.HEADER_HEIGHT, bg="black")
		
		self.label = tk.Label(self, text=self.__result.format(0, 0),
									fg="white", 
									bg="black", 
									font=("FS Pro", 44))

		self.label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

		self.user1 = User()
		self.user2 = User()


	def change_score(self, user):
		'''
		Добавляем одно очко пользователю и сохраняем изминения
		'''
		user.point_to_user()
		self.label["text"] = self.__result.format(self.user1.score, self.user2.score)



