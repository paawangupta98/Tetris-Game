import random
import pygame
class block:
	def __init__(self , tetris_shape , COLORS):
		self.shape = random.choice(list(tetris_shape.keys()))					#Chooses a random shape
		self.rotation=random.randint(0, len(tetris_shape[self.shape]) - 1)		#Chooses a random rotation
		self.x = 15																#For the block to fall from the middle of the area
		self.y = -2
		self.color = random.randint(0, len(COLORS)-1)							#For the block to have a random color
	def rotate(self , tetris_shape , board1):									#A function for Rotating the Block
		self.rotation = (self.rotation + 1) % len(tetris_shape[self.shape])
		if not board1.checkpiecepos(self , tetris_shape):
			self.rotation = (self.rotation - 1) % len(tetris_shape[self.shape])
	def moveleft(self , board1 , tetris_shape):									#A function for moving the block left by one step
		if board1.checkpiecepos(self, tetris_shape , adjx=-1):
			self.x -= 1
	def moveright(self , board1 , tetris_shape):								#A function for moving the block right by one step
		if board1.checkpiecepos(self, tetris_shape , adjx=1):
			self.x += 1
	def getshape(self):
		return self.shape
	def getrot(self):
		return self.rotation
	def getx(self):
		return self.x
	def gety(self):
		return self.y
	def getcolor(self):
		return self.color
	def setx(self , xt):
		self.x = xt
	def sety(self , yt):
		self.y = yt
	def drawpiece(self , tetris_shape ,displayarea ,COLORS , px=None , py=None):#A funtion for drawing the Block on the board
		if px == None and py == None:
			px, py = (160 + (self.x * 16)), (100 + (self.y * 16))
			for x in range(5):
			    for y in range(5):
			        if tetris_shape[self.shape][self.rotation][y][x] != '.':
						if px==None and py==None:
							px , py = (160 ), (100 )
						pygame.draw.rect(displayarea, COLORS[self.color], (px + 1+ (x * 16), py + (y * 16)+ 1, 15,15))
