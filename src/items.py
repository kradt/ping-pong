import config 
import random

class MixinCoords:
	def __init__(self, item):
		self.item = item

	@property
	def coords(self):
		return self.canvas.coords(self.item)


class Ball(MixinCoords):
	def __init__(self, canvas, ball):
		super().__init__(ball)
		self.canvas = canvas
		self.ball = ball
		self.left = canvas.left_stick
		self.right = canvas.right_stick
		self.score = canvas.root.score

	def move_left(self, x=0):
		if int(self.left.coords[0]) == int(self.coords[0]):
			if self.hit_on_racket(self.left):
				self.move_to_route(self.left, self.move_right)
				return
			self.score.change_score(self.right.user)
			self.move_right()
			return
		self.move_controll(self.move_left, x, -10)

	def move_right(self, x=0):
		if int(self.right.coords[2]) == int(self.coords[2]):
			if self.hit_on_racket(self.right):
				self.move_to_route(self.right, self.move_left)
				return
			self.score.change_score(self.left.user)
			self.move_left()
			return
		self.move_controll(self.move_right, x, 10)

	def move_controll(self, func, x=0, y=0):
		'''
		Контролируем направления движущегося мяча
		Принимает функцию движения и координаты
		'''
		coord = self.coords[1]
		deviation = random.randint(1, 5)

		self.canvas.move(self.ball, y, x)
		if coord >= config.FIELD_HEIGHT-45:
			deviation = -deviation
		elif coord >= 10:
			deviation = x
		self.canvas.after(40, lambda: func(deviation))

	def move_to_route(self, stick, func, deviation=0):
		'''
		Сверяем координати ракетки и координаты места на ракетке об которое ударился мяч
		Относительно этого меняем маршрут движения по x 
		'''
		coords_s = stick.coords
		coords_b = self.coords
		r = random.randint(1, 5)

		if coords_b[1] <= coords_s[1] and coords_b[3] <= coords_s[3]:
			deviation = -r
		elif coords_b[1] >= coords_s[1] and coords_b[3] >= coords_s[3]:
			deviation = r
		func(deviation)

	def hit_on_racket(self, stick):
		'''
		Проверяем стукнулся ли мяч об ракетку
		'''
		y = self.coords[1]
		coords = stick.coords
		if coords[1]-30 < y < coords[3]+30:
			return True
		return False


class Stick(MixinCoords):
	def __init__(self, canvas, stick, user):
		super().__init__(stick)
		self.canvas = canvas
		self.stick = stick
		self.user = user

	def move_up(self):
		self.canvas.move(self.stick, 0, -10)
		self.canvas.after(20)

	def move_down(self):
		self.canvas.move(self.stick, 0, 10)
		self.canvas.after(20)

	