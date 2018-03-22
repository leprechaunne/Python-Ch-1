from math import floor
from random import randint
from graphics import *
from interface import *
import settings



class Coordinate():
	""" Simple storage of x,y coordinates to simplify position records"""
	def __init__(self, x, y):
		self.x = x
		self.y = y





class Snake():
	"""User controlled object that consists of squares.
	
	Color can be passed with Snake(color)
	Snake's main properties are its location_list, length, and score."""

	# color 				- the color of the blocks drawn by the snake
	# length 				- how many blocks the snake is made of
	# score					- each snake is applied one-per-player, so the easiest mode of storage is in snake
	# grid_position_record	- queue of grid coords
	# position_record 		- use this file's Coordinate class 
	#if the directions become heavily used, you can make a dictionary to go from
		#number to its corollary constant

	direction_dict = {
		"up": 0,
		"right": 1,
		"down": 2,
		"left": 3
	}



	class SnakeSegment():

		def __init__(self, x, y, color="green"):
			#draw first square
			p1 = Point(x, y)
			p2 = Point(p1.getX() + 1, p1.getY() + 1)
			head = Rectangle(p1, p2)
			head.setFill(color)
			head.setOutline("black")
			head.setWidth(1)


			head.draw(settings.win)
			self.rectangle = head
			settings.entity_grid[y][x] = self

		
	def __init__(self, color="green"):
		self.color = color
		self.length = 1
		self.score = 0
		self.direction = randint(0,3)
		#spawn in middle of grid
		middle_square = floor(settings.grid_cells_per_side / 2)
		self.grid_position_record = [Coordinate(middle_square, middle_square)]
		settings.entity_grid[middle_square][middle_square] = self.SnakeSegment(middle_square, middle_square, self.color)


	def move(self):
		delta_x, delta_y = 0, 0

		# print(self.direction)

		if self.direction == self.direction_dict["up"]:
			delta_y = 1
			#print("moving")
		elif self.direction == self.direction_dict["down"]:
			delta_y = -1
			#print("moving")
		elif self.direction == self.direction_dict["left"]:
			delta_x = -1
			#print("moving")
		elif self.direction == self.direction_dict["right"]:
			delta_x = 1
			#print("moving")


		x = self.grid_position_record[0].x
		y = self.grid_position_record[0].y
		next_x = x + delta_x
		next_y = y + delta_y
		collision = type(settings.entity_grid[next_y][next_x])
		# print(collision)
		# print(f"[{x},{y}], [{next_x}, {next_y}]")


		if collision == type(False):
			print(type(settings.entity_grid[y][x]))
			try:
				#undraw previous segment
				settings.entity_grid[y][x].rectangle.undraw()
			except Exception:
				print(Exception)
			#draw new segment and replace
			new_head = self.SnakeSegment(next_x, next_y)
			position = Coordinate(next_x, next_y)
			#replace last one
			self.grid_position_record[self.length - 1] = position

		# elif collision == type(Apple()):
			# pass