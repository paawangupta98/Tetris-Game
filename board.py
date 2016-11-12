import numpy
import pygame
from block import *
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
class board:
	def __init__(self , cols , rows):
		self.cols=cols															# No. of columns of the board
		self.rows=rows															# No. of Rows of the Board
		board = []
		for i in range(cols):
		        board.append(['.'] * rows)
		self.newboard = board
	def checkpiecepos(self , piece ,tetris_shape ,  adjx=0 , adjy=0):			# A function for checking the block to be correctly placed
		for x in range(5):
			for y in range(5):
				yt = y + piece.gety() + adjy
				xt = x + piece.getx() + adjx
				if yt<0 or tetris_shape[piece.getshape()][piece.getrot()][y][x]=='.':
					continue
				if not (xt>=0 and xt<30 and yt<32):
					return False
				if self.newboard[xt][yt] != '.':
					return False
		return True
	def fillpiecepos(self , tetris_shape , piece):								# A function for adding the piece permantly on the Board
		for x in range(5):
			for y in range(5):
				if tetris_shape[piece.getshape()][piece.getrot()][y][x] != '.':
					self.newboard[x + piece.getx()][y + piece.gety()] = piece.getcolor()
	def drawboard(self , displayarea, COLORS):									# A function to draw the Game Board
		pygame.draw.rect(displayarea, RED, (160, 100, 488, 518), 5)
		pygame.draw.rect(displayarea, BLACK, (160, 107, 480, 510))
	        for x in range(30):
                    for y in range(32):
						if self.newboard[x][y] == '.':
							a=0
						else:
							px, py = (160 + (x * 16)), (100 + (y * 16))
							pygame.draw.rect(displayarea,COLORS[ self.newboard[x][y]], (px + 1, py + 1,15,15))
