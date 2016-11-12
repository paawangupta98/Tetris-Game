from  block import *
from  board import *
import random, time, pygame, sys
from pygame.locals import *

BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
GREEN       = (  0, 155,   0)
BLUE        = (  0,   0, 155)
YELLOW      = (155, 155,   0)
NEWBLUE     = (  0,  87, 255)
COLORS      = (     BLUE,      GREEN,      RED,      YELLOW) # A array for colors
S_shape = [['.....',
             '.....',
             '..OO.',
             '.OO..',
             '.....'],
            ['.....',
             '..O..',
             '..OO.',
             '...O.',
             '.....']]

Z_shape = [['.....',
             '.....',
             '.OO..',
             '..OO.',
             '.....'],
            ['.....',
             '..O..',
             '.OO..',
             '.O...',
             '.....']]

I_shape = [['..O..',
             '..O..',
             '..O..',
             '..O..',
             '.....'],
            ['.....',
             '.....',
             'OOOO.',
             '.....',
             '.....']]

O_shape = [['.....',
             '.....',
             '.OO..',
             '.OO..',
             '.....']]

J_shape = [['.....',
            '.O...',
            '.OOO.',
            '.....',
            '.....'],
            ['.....',
             '..OO.',
             '..O..',
             '..O..',
             '.....'],
            ['.....',
             '.....',
             '.OOO.',
             '...O.',
             '.....'],
            ['.....',
             '..O..',
             '..O..',
             '.OO..',
             '.....']]

L_shape = [['.....',
             '...O.',
             '.OOO.',
             '.....',
             '.....'],
            ['.....',
             '..O..',
             '..O..',
             '..OO.',
             '.....'],
            ['.....',
             '.....',
             '.OOO.',
             '.O...',
             '.....'],
            ['.....',
             '.OO..',
             '..O..',
             '..O..',
             '.....']]

T_shape = [['.....',
             '..O..',
             '.OOO.',
             '.....',
             '.....'],
            ['.....',
             '..O..',
             '..OO.',
             '..O..',
             '.....'],
            ['.....',
             '.....',
             '.OOO.',
             '..O..',
             '.....'],
            ['.....',
             '..O..',
             '.OO..',
             '..O..',
             '.....']]

tetris_shape = {'S': S_shape,                                                   # A array for the Shapes
          'Z': Z_shape,
          'J': J_shape,
          'L': L_shape,
          'I': I_shape,
          'O': O_shape,
          'T': T_shape}


class gameplay(board , block):
    def __init__(self):
        pygame.init()                                                           #For initialising the pygame
        self.displayarea = pygame.display.set_mode((720, 750))
        pygame.display.set_caption('Tetris')
        self.lastFallTime = time.time()
        self.fallFreq = 0.7                                                     # A variable for speed
        self.score=0                                                            # A variable for score
        self.level=1                                                            # A variable for level
    def main(self):
        myfont3 = pygame.font.Font('pixele.otf', 45)
        score12 = self.runGame()
        pygame.draw.rect(self.displayarea, BLACK, (0, 0, 720, 750))
        scoreSurf3 = myfont3.render('GAME IS OVER', True, NEWBLUE)
        scoreRect3 = scoreSurf3.get_rect()
        scoreRect3.topleft = (200, 100)
        self.displayarea.blit(scoreSurf3, scoreRect3)                           # For displaying text "Game is OVER"
        scoreSurf4 = myfont3.render('SCORE IS %s' % score12 , True, NEWBLUE)
        scoreRect4 = scoreSurf4.get_rect()
        scoreRect4.topleft = (200, 200)
        self.displayarea.blit(scoreSurf4, scoreRect4)                           # For displaying text "Score"
        pygame.display.update()
        print "GAME ENDED"
        print "Your Score" , score12
        pygame.time.delay(2000)                                                 # For delaying the time
        sys.exit()

    def runGame(self):
        myfont = pygame.font.Font('pixele.otf', 20)
        myfont1 = pygame.font.Font('pixele.otf', 35)
        board1 = board(30,32)                                                   # Declaring a new Board
        fallingPiece = block(tetris_shape , COLORS)                             # Declaring a block to be allowed to fall in the gameplay
        while True:                                                             # A loop
                if fallingPiece == None:                                        # If the block is not there we take a new block
                    fallingPiece = block(tetris_shape  ,COLORS )
                    if not board1.checkpiecepos(fallingPiece , tetris_shape):
                        return self.score
                    self.score += 10*self.level
                self.checkForQuit()                                             # Checking for unconditional Closing of Game
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if (event.key == K_LEFT or event.key == K_a) and board1.checkpiecepos(fallingPiece, tetris_shape , adjx=-1 ):
                            fallingPiece.moveleft(board1 , tetris_shape)
                        elif (event.key == K_RIGHT or event.key == K_d) and board1.checkpiecepos(fallingPiece, tetris_shape , adjx=1):
                            fallingPiece.moveright(board1 , tetris_shape)
                        elif (event.key == K_UP or event.key == K_w):
                            fallingPiece.rotate(tetris_shape , board1)
                        elif (event.key == K_q):
                            print "GAME ENDED"
                            print "Your Score" , self.score
                            pygame.quit()
                            sys.exit()
                        elif event.key==K_SPACE:                                # if space is entered the block is checked in the following rows where it could be placed
                            for i in range(1, 32):
                                if not board1.checkpiecepos(fallingPiece,tetris_shape, adjy=i):
                                    break
                            fallingPiece.y += i - 1
                if time.time() - self.lastFallTime > self.fallFreq:             # if it is time to fall allow the block to fall
                    if not board1.checkpiecepos(fallingPiece, tetris_shape , adjy=1): # if the block has no more moves to go down update score if any row can be removed and make the fallingPiece null
                        board1.fillpiecepos(tetris_shape , fallingPiece)
                        self.score += 100*self.removerow(board1.newboard)*(int(self.level/5)+1)
                        fallingPiece = None

                    else:
                        fallingPiece.y += 1
                        self.lastFallTime = time.time()
                if self.score-200*(self.level-1)*(self.level-1)>100*self.level*self.level:                # if it is time to increase level increase level
                    self.fallFreq = self.fallFreq-0.07
                    self.level+=1
                self.displayarea.fill(BLACK)
                board1.drawboard(self.displayarea, COLORS)
                scoreSurf = myfont.render('Score: %s' % self.score, True, RED)
                scoreRect = scoreSurf.get_rect()
                scoreRect.topleft = (500, 20)
                scoreSurf1 = myfont.render('Level: %s' % self.level, True, BLUE)
                scoreRect1 = scoreSurf1.get_rect()
                scoreRect1.topleft = (500, 50)
                scoreSurf2 = myfont1.render('TETRIS', True, NEWBLUE)
                scoreRect2 = scoreSurf2.get_rect()
                scoreRect2.topleft = (260, 20)
                self.displayarea.blit(scoreSurf, scoreRect)                     # Display "TETRIS"
                self.displayarea.blit(scoreSurf1, scoreRect1)                   # Display "Score"
                self.displayarea.blit(scoreSurf2, scoreRect2)                   # Display "Level"
                if fallingPiece != None:
                    fallingPiece.drawpiece(tetris_shape,self.displayarea ,COLORS )
                pygame.display.update()
    def iscomplete(self, board , y):                                            # to check if a row is full or not
        for x in range(30):
            if board[x][y] == '.':
                return False
        return True

    def removerow(self , board):                                                # to remove full rows and return their count
        cnt=0
        y = 31
        while y>=0:
            if self.iscomplete(board,y):
                for k in range(y , 0 , -1):
                    for x in range(30):
                        board[x][k] = board[x][k-1]
                for x in range(30):
                    board[x][0]='.'
                cnt +=1
            else:
                y-=1
        return cnt

    def checkForQuit(self):                                                     # A function for checking the unconditional Closing of the gameplay
        for event in pygame.event.get(QUIT):
            print "GAME ENDED"
            print "Your Score" , self.score
            pygame.quit()
            sys.exit()

newgame =gameplay()                                                             # Making A new object of Gameplay
newgame.main()                                                                  # Running the Main function , i.e , the Game
