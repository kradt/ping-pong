import tkinter as tk
import random

import config 


# Mixin for get cooord of gived item
class MixinCoords:
	def __init__(self, item):
		self.item = item

	@property
	def coords(self):
		return self.canvas.coords(self.item)


class Ball(MixinCoords):
	def __init__(self, canvas, ball, speed):
		super().__init__(ball)
		self.canvas = canvas
		self.speed = speed
		self.ball = ball
		self.left = canvas.left_stick
		self.right = canvas.right_stick
		self.score = canvas.root.score
		self.is_moving = True

	# Method move left manage all road ball
	def move_left(self, x=0):
		"""
		if ball hit on stick method call move_to_route
		else method call change_score before call move_right
		"""
		if not self.is_moving:
			return
		if int(self.left.coords[0]) == int(self.coords[0]):
			if self.hit_on_racket(self.left):
				self.move_to_route(self.left, self.move_right)
				return
			self.score.change_score(self.right.user)
			self.move_right()
			return
		self.move_controll(self.move_left, x, -10)

	# Method move right manage all road ball
	def move_right(self, x=0):
		"""
		if ball hit on stick method call move_to_route
		else method call change_score before call move_left
		"""
		if not self.is_moving:
			return
		if int(self.right.coords[2]) == int(self.coords[2]):
			if self.hit_on_racket(self.right):
				self.move_to_route(self.right, self.move_left)
				return
			self.score.change_score(self.left.user)
			self.move_left()
			return
		self.move_controll(self.move_right, x, 10)

	# Methood start move to another side for y
	def move_controll(self, func, x=0, y=0):
		coord = self.coords[1]
		self.canvas.move(self.ball, y, x)

		deviation = 5
		if coord >= config.FIELD_HEIGHT-45:
			deviation = -deviation
		elif coord >= 10:
			deviation = x
		self.canvas.after(self.speed, lambda: func(deviation))

	# Method start move ball to another side for x
	def move_to_route(self, stick, func, deviation=0):
		coords_s = stick.coords
		coords_b = self.coords

		if coords_b[1] <= coords_s[1] and coords_b[3] <= coords_s[3]:
			deviation = -5
		elif coords_b[1] >= coords_s[1] and coords_b[3] >= coords_s[3]:
			deviation = 5
		func(deviation)

	# Method check if ball was hitted on stick
	def hit_on_racket(self, stick):
		y = self.coords[1]
		coords = stick.coords
		if coords[1]-30 < y < coords[3]+30:
			return True
		return False

	# Method stop starting move methoods
	def stop(self):
		self.is_moving = False

	def __del__(self):
		self.canvas.delete(self.ball)


class Stick(MixinCoords):
	def __init__(self, canvas, stick, user):
		super().__init__(stick)
		self.canvas = canvas
		self.stick = stick
		self.user = user

	# Method move stick to up 
	def move_up(self):
		self.canvas.move(self.stick, 0, -10)
		self.canvas.after(20)

	# Method move stick to down
	def move_down(self):
		self.canvas.move(self.stick, 0, 10)
		self.canvas.after(20)

	def __del__(self):
		self.canvas.delete(self.stick)
	