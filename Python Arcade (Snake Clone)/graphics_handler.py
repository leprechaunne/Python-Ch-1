"""Used for drawing and handling UI independtly so the graphics may be quickly changed."""
from graphics import *
from math import floor

#these variables are static, and should be changed to customize the window and grid
window_width 	= 500 	#Px. Obviously must be greater than zero.
window_height 	= 500 	#Px. Should probably also be bigger than the grid_size
grid_size		= 10  	#Px. Defines the length of the sides of the square created in a grid
						#### Should be greater than 2, because the snake uses borders.
#To understand this grid, the origin is the upper left pixel. 
#The left column is 0 and the right column is max_width
#Same logic for y, though it is counter intuitive for an increasing y to be lower on the board
grid_x_max		= floor(window_width / grid_size) 
grid_y_max 		= floor(window_height / grid_size)
play_area_grid	= [[1, 1], [grid_x_max - 1, grid_y_max - 1]] #play area excludes the outermost tiles


def create_window():
	"""create game window"""
	win = GraphWin("Python", window_width, window_height)
	win.setBackground("black")
	return win

#################   Clearing Win  	###############################
def teardown_all(win):
	"""undraws all objects in the window"""
	for obj in win.items:
		obj.undraw()


#################	Title Screen 	################################

def generate_title_screen(win):
	"""Creates a basic title screen"""
	title = Text(Point(250, 175), "PYTHON IN PYTHON")
	title.setSize(36)
	title.setTextColor("white")

	subtitle = Text(Point(250,175+36), "PRESS ENTER TO CONTINUE")
	subtitle.setSize(10)
	subtitle.setTextColor("white")

	title.draw(win)
	subtitle.draw(win)

	flag = False
	while not flag:
		k = win.getKey()
		# print(k)
		if k in 'Return':
			flag = True

	#Next scene
	teardown_all(win)


################	Title Screen 	################################

def generate_game_board(win):
	""" draws the border, TODO (score, time) """

	#draw boundary
	##get coordinates of LAST ACCEPTABLE points
	p1 = grid_to_coords(play_area_grid[0][0], play_area_grid[0][1])
	p2 = grid_to_coords(play_area_grid[1][0], play_area_grid[1][1])
	##modify these points to be the OoB border
	p1 = [p1[0] - 1, p1[1] - 1]
	p2 = [p2[0] + 1, p2[1] + 1]
	##convert to type Point
	corner1 = Point(p1[0], p1[1])
	corner2 = Point(p2[0], p2[1])
	##use graphics' API to draw boundary
	out_of_bounds = Rectangle(corner1, corner2)
	out_of_bounds.setWidth(1)
	out_of_bounds.setOutline("white")
	out_of_bounds.draw(win)





##############	Secondary Definitions #########################

def grid_to_coords(x, y):
	#check for out_of_grid exception
	p1 = play_area_grid[0]
	p2 = play_area_grid[1]
	#check for failure first
	if not ( (x in [p1[0], p2[0]]) or (y in [p1[1], p2[1]]) ):
		return False
	else:
		#now convert
		x_coord = x * grid_size #for example, a snake at 1,1 for a 10px grid would be at 10, 10 
		y_coord = y * grid_size		#this line of reasoning works because the first pixel is 0,0
		return [x_coord, y_coord]


def get_center_grid(win):
	"""give the grid square (not px) of the middle of the board"""
	x = floor(grid_x_max / 2)
	y = floor(grid_y_max / 2)
	return [x, y]

def draw_square_from_grid(win, grid_space):
	pass
