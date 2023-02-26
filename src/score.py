import tkinter as tk

import config


# Class for count points of user
class User():
	def __init__(self):
		self.score = 0

	def point_to_user(self):
		self.score += 1
		return self.score

# Class for picts Score game
class Score(tk.Frame):
	__result = "{} : {}"

	def __init__(self, root):
		super().__init__(root, width=config.HEADER_WIDTH, height=config.HEADER_HEIGHT, bg="black")
		self.root = root
		self.label = tk.Label(self, text=self.__result.format(0, 0),
									fg="white", 
									bg="black", 
									font=("FS Pro", 44))

		self.label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

		self.user1 = User()
		self.user2 = User()

	# Method change score, if some user have 5 or more points he is win
	def change_score(self, user):
		"""
		Add one point to user and check if user won
		"""
		score = user.point_to_user()
		if score >= 5:
			if user == self.user1:
				text = "Left User Won"
			else:
				text = "Right User Won"
			self.label["text"] = text
			self.root.game.end_of_game()
		else:
			self.label["text"] = self.__result.format(self.user1.score, self.user2.score)