# Simon Orr
# May 12 2020
# SimonOrrUltimateTicTacToe.py
# This program is a game composed of nine tic-tac-toe boards arranged in a 3 × 3 grid. Players take turns playing in the smaller tic-tac-toe boards until one of them wins in the larger tic-tac-toe board.

# import the necessary modules for later use
import pygame
import sys
import random
#initialize pygame
pygame.init()
# set the size for the surface (screen)
screen = pygame.display.set_mode((1000, 1000), pygame.DOUBLEBUF)
# width and height of the screen for later use
width = screen.get_width()
height = screen.get_height()
# set the caption for the screen
pygame.display.set_caption("Simon Orr - Ultimate Tic Tac Toe")
# define colours you will be using
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
PURPLE = (218,112,214)
INDIGO = (75,0,130)
CYAN = (0,255,255)
SOFTGREEN = (79,135,104)
PURPLEICE = (75,38,101)
SOFTPURPLE = (135,50,171)
AQUA = (54,141,184)
LIGHTBLUE = (155,209,229)
LIGHTCYAN = (202,255,230)
BLUEICE = (30, 241, 255)
DARKPURPLE = (66, 4, 61)
MAROON = (128, 0, 0)
GRAY = (169, 169, 169)
# initialize variables
endX = width/2
endY = height/3
restX = width/2
restY = (height / 3) * 2
main = False
n = 0
run = 0
startRun = 0
turn = 1
start = True
selected = False # this variable is to determine whether or not a game is selected
sSelected = False # this variable is to determine whether or not a spot in any game is selected
randomStart = True
end = False
tie = False
p1Win = False
p2Win = False
sWin = False
instructions = False

initX = 1
initY = 1

initSX = 3
initSY = 3

sX = 3
sY = 3

winner = 0
endRun = 0

moves = 0
# instructions variables
instmX = width/2 
inst2mX = width/2 
instmY = height - 400
inst2mY = height - 300
inst3mY = height - 200
restartmY = height- 100
restartmX = width/2
# text variables

colours = [BLUEICE, DARKPURPLE]
restcolour = random.choice(colours)
fontEnd = pygame.font.SysFont("8-Bit-Madness", 60)
textEnd = fontEnd.render("8-Bit-Madness", True, random.choice(colours))

sColours = [AQUA, RED, PURPLEICE, SOFTGREEN, INDIGO, CYAN]
startColour = random.choice(sColours)
fontStart = pygame.font.SysFont("Impact", 60)
textStart = fontStart.render("Ultimate Tic Tac Toe", True, startColour)

clickIcolour = random.choice(colours)
fontClickI = pygame.font.SysFont("8-Bit-Madness", 40)
textClickI = fontClickI.render("8-Bit-Madness", True, startColour)

extraColour = random.choice(colours)
fontExtra = pygame.font.SysFont("8-Bit-Madness", 25)
textExtra = fontExtra.render("8-Bit-Madness", True, extraColour)

fontExtra2 = pygame.font.SysFont("8-Bit-Madness", 20)

diffcolour = random.choice(colours)
fontDiff = pygame.font.SysFont("Raleway Bold", 40)
textDiff = fontClickI.render("dejavusansmono", True, startColour)

instcolour = random.choice(colours)
fontInst = pygame.font.SysFont("Raleway Bold", 40)
textInst = fontClickI.render("dejavusansmono", True, startColour)

instcolour2 = random.choice(colours)
fontInst2 = pygame.font.SysFont("Raleway Bold", 30)
textInst2 = fontClickI.render("dejavusansmono", True, startColour)

restartcolour = random.choice(colours)
fontRestart = pygame.font.SysFont("dehjavusansmono", 20)
textRestart = fontClickI.render("dejavusansmono", True, startColour)

instX = width / 2
instY = (height / 3 * 2) - height/9 - 50
instColour = AQUA
startX = width / 2
startY = height / 3 - height/9
playX = width / 2 + 25
playY = height - height/9 - 50
diffX = height - 800
diffY = height / 3 + 50

# set largegrid variable for later use
largegrid = []

# for loop to make the matrix seen in game
for i in range(9):
    jj = []
    for j in range(9):
        jj.append(None)
    largegrid.append(jj)
        


screen.fill(BLACK)
# define functions
def drawGrid(bWidth, bHeight, colour): # function to draw white big grid
    pygame.draw.line(screen, colour, [0, bHeight/3], [bWidth,bHeight/3], 10)
    pygame.draw.line(screen, colour, [0, bHeight-(bHeight/3)], [bWidth,bHeight-(bHeight/3)], 10)
    pygame.draw.line(screen, colour, [bWidth/3, bHeight], [bWidth/3,0], 10)
    pygame.draw.line(screen, colour, [bWidth-(bWidth/3), bHeight], [bWidth-(bWidth/3),0], 10)
    pygame.display.flip()
def exit(): # exit game
    pygame.quit()
    sys.exit()

def grayblock(x, y, colour, a): # function to draw blocks the size of external game spaces with a customizable opaqueness and colour
    w = int(width /3)
    h = int(height / 3)
    r = pygame.Surface((w, h))
    r.set_alpha(a)
    r.fill(colour)
    screen.blit(r, (x * w, y * h))

def sGrayBlock(x, y): # function to draw blocks the size of internal game spaces
    sW = int(width / 9)
    sH = int(height / 9)
    sR = pygame.Surface((sW, sH))
    sR.set_alpha(3)
    sR.fill(SOFTPURPLE)
    screen.blit(sR, (x * sW, y * sH))

def drawPlayer(x, y): # draw the black tile that indicates where the player is
    w = int(width / 9)
    h = int(height / 9)
    initialX = x * w
    initialY = y * h
    sR = pygame.Surface((w, h))
    sR.set_alpha(255)
    sR.fill(BLACK)
    screen.blit(sR, (x * w, y * h))
def drawscreen(): # setup main screen
    screen.fill((0, 0, 0))
    pygame.display.flip()
    for i in range(0, width, int(width/9)):
        pygame.draw.line(screen, SOFTPURPLE, [i,0], [i,height], 10)
    for i in range(0, height, int(height/9)):
        pygame.draw.line(screen, SOFTPURPLE, [0,i], [width,i], 10)
def drawSmallGrid(): # draw purple grid lines for internal games
    for i in range(0, width, int(width/9)):
        pygame.draw.line(screen, SOFTPURPLE, [i,0], [i,height], 10)
    for i in range(0, height, int(height/9)):
        pygame.draw.line(screen, SOFTPURPLE, [0,i], [width,i], 10)
def drawMatrix(): # draw all 
    w = int(width / 9)
    h = int(height / 9)
    for i in range(9):
        for j in range(9):
            if largegrid[i][j] is not None:
                ccolor = BLACK
                if largegrid[i][j] == 1:
                    ccolor = RED
                elif largegrid[i][j] == 2:
                    ccolor = WHITE
                sR = pygame.Surface((w, h))
                sR.fill(ccolor)
                screen.blit(sR, (i * w, j * h))

def restart(): # restart the game 
    exec(open(__file__).read())

wonGrid = [] # setup wonGrid for later use
for i in range(3): # create the wonGrid in a 9x9 for later use
    wonGrid.append([None, None, None])

def checkIfWin(r, c, p): # use the variables given from the user, wonGrid and largeGrid to check if the player won in the internal grids
    for i in range(3):
        if largegrid[r + i][c] == p and largegrid[r + i][c + 1] == p and largegrid[r + i][c + 2] == p:
            wonGrid[int(r/3)][int(c/3)] = p
        if largegrid[r + 0][c + i] == p and largegrid[r + 1][c + i] == p and largegrid[r + 2][c + i] == p:
            wonGrid[int(r/3)][int(c/3)] = p
    if largegrid[r][c] == p and largegrid[r + 1][c + 1] == p and largegrid[r + 2][c + 2] == p:
        wonGrid[int(r/3)][int(c/3)] = p
    if largegrid[r][c + 2] == p and largegrid[r + 1][c + 1] == p and largegrid[r + 2][c] == p:
        wonGrid[int(r/3)][int(c/3)] = p

def checkBigWin(): # check if either player won the external game
    # returns 1 if red won (large case), returns 2 if white won (large case), returns 0 if no one won
    for p in range(1, 3): # check 1 & 2
        for i in range(3):
            if wonGrid[i][0] == p and wonGrid[i][1] == p and wonGrid[i][2] == p:
                return p
            if wonGrid[0][i] == p and wonGrid[1][i] == p and wonGrid[2][i] == p:
                return p
        if wonGrid[0][0] == p and wonGrid[1][1] == p and wonGrid[2][2] == p:
            return p
        if wonGrid[0][2] == p and wonGrid[1][1] == p and wonGrid[2][0] == p:
            return p
    return 0

while start:
    # create the visuals for the start screen
    if startRun == 0:
        screen.fill(BLACK)
        drawGrid(width, height, WHITE)
    startRun += 1
    # render the text
    textStart = fontStart.render("Ultimate Tic Tac Toe", True, startColour)
    startRect = textStart.get_rect(center=(startX, startY))
    screen.blit(textStart, startRect)
    textClickI = fontClickI.render("Click [I] for Instructions", True, clickIcolour)
    clickIRect = textClickI.get_rect(center=(instX, instY))
    screen.blit(textClickI, clickIRect)

    textEnter = fontClickI.render("Click Enter to Play", True, SOFTGREEN)
    enterRect = textClickI.get_rect(center=(playX, playY))
    screen.blit(textEnter, enterRect)
    for event in pygame.event.get(): # check for any events (i.e key press, mouse click etc.)
        if event.type ==pygame.QUIT: # check to see if it was "x" at top right of screen
            exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_i:
                start = False
                instructions = True
            if event.key == pygame.K_RETURN:
                turn = random.choice([1,2])
                main = True
                start = False
    # display start screen visuals
    pygame.display.flip()

while instructions: # instructions page (explain to the user how to play)
    screen.fill(BLACK) 
    # create the visuals
    pygame.draw.rect(screen, clickIcolour, (0, 0, 1000, 180) ,0) # create a light blue rectangle for visuals
    textStart = fontStart.render("Instructions", True, startColour)
    textInfo2 = fontExtra.render("To start, click play. Then move with the arrows on your keyboard on any spot on one of the external games.", True, extraColour)
    textDiff = fontExtra.render("Click enter to select an external game and then you can move your arrow keys to where you want to mark.", True, diffcolour)
    textInstruction1 = fontExtra.render("Clicking enter will also mark the space that you want on the internal game.", True, instcolour)
    textInstruction2 = fontExtra.render("Where you move on the internal game determines what internal game your opponent has to play in on the external games", True, instcolour2)
    textInstruction3 = fontExtra2.render("You can score an internal game or win an external game by placing 3 of your marks in a horizontal, vertical, or diagonal row.", True, startColour)
    textRestart = fontRestart.render("R to go back to menu and to restart at any moment in the game. Q to quit the game", True, restartcolour)
    diffRect = textDiff.get_rect(center=(diffX + 300, diffY))
    startRect = textStart.get_rect(center=(startX, startY))
    infoRect = textInfo2.get_rect(center=(instX, instY - 200))
    instRect = textInstruction1.get_rect(center=(instmX, instmY))
    instRect2 = textInstruction2.get_rect(center=(inst2mX, inst2mY))
    instRect3 = textInstruction3.get_rect(center=(inst2mX, inst3mY))
    restartRect = textRestart.get_rect(center=(restartmX, restartmY))
    screen.blit(textStart, startRect)
    screen.blit(textInfo2, infoRect)
    screen.blit(textDiff, diffRect)
    screen.blit(textInstruction1, instRect)
    screen.blit(textInstruction2, instRect2)
    screen.blit(textInstruction3, instRect3)
    screen.blit(textRestart, restartRect)
    for event in pygame.event.get(): # check for any events (i.e key press, mouse click etc.)
        if event.type ==pygame.QUIT: # check to see if it was "x" at top right of screen
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
    # bring the visuals to the screen
    pygame.display.flip()
while main:
    if run == 0:
        drawscreen() # setup screen
    run += 1
    for event in pygame.event.get(): # check for any events (i.e key press, mouse click etc.)
        if event.type == pygame.QUIT: # check to see if it was "x" at top right of screen
            exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                if not selected:
                    # move the player's position right 1 external grid space
                    initX += 1
                    initSX += 3
                    if initX > 2:
                        initX = 2
                        initSX = 6
                    grayblock(initX, initY, BLACK, 255)
                    drawSmallGrid()
                if selected and not sSelected:
                    # move in the internal (small) grids
                    sX += 1
                    if sX > initSX + 2:
                        sX -= 1
                    if sX > 8:
                        sX = 8
                    drawPlayer(sX, sY)
            if event.key == pygame.K_LEFT: 
                if not selected:
                    # move the player's position left 1 external grid space
                    initX -= 1
                    initSX -= 3
                    if initX < 0 or initSX < 0:
                        initX = 0
                        initSX = 0
                    grayblock(initX, initY, BLACK, 255)
                    drawSmallGrid()
                if selected and not sSelected:
                    # move in the internal (small) grids
                    if sX >= initSX:
                        sX -= 1
                    if sX < initSX:
                        sX = initSX
                    drawPlayer(sX, sY)
            if event.key == pygame.K_UP:
                #n -= 3
                if not selected:
                    # move the player's position up 1 external grid space
                    initY -= 1 
                    initSY -= 3
                    if initY < 0:
                        initY = 0
                        initSY = 0
                    grayblock(initX, initY, BLACK, 255)
                    drawSmallGrid()
                if selected and not sSelected:
                    # move in the internal (small) grids
                    sY -= 1
                    if sY < 0:
                        sY = 0
                    if sY < initSY:
                        sY = initSY
                    drawPlayer(sX, sY)
            if event.key == pygame.K_DOWN:
                # move the player's positon down 1 external grid space 
                if not selected:
                    initY += 1
                    initSY += 3
                    if initY > 2:
                        initY = 2
                        initSY = 6
                    grayblock(initX, initY, BLACK, 255)
                    drawSmallGrid()
                if selected and not sSelected: 
                    # move in the internal (small) grids
                    sY += 1
                    if sY > 8:
                        sY = 8
                    if sY > initSY + 2:
                        sY = initSY + 2
                    drawPlayer(sX, sY)
            if event.key == pygame.K_RETURN:
                if selected:
                    moves += 1
                    checkinitY = sY - initY * 3
                    checkinitX = sX - initX * 3
                    # checks to see whether the external game has been won before moving to internal game
                    if wonGrid[checkinitX][checkinitY] == None: 
                        largegrid[sX][sY] = turn
                        sSelected = True
                        if turn == 1:
                            turn = 2
                            sSelected = False
                        elif turn == 2:
                            turn = 1
                            sSelected = False
                        initY = sY - initY * 3
                        initX = sX - initX * 3
                        grayblock(initX, initY, BLACK, 255)
                        initSX = initX * 3
                        initSY = initY * 3
                        sX = initSX
                        sY = initSY
                        for p in range(1, 3): # check if the player won by going through all of the win cases
                            for r in range(0, 9, 3):
                                for c in range(0, 9, 3):
                                    checkIfWin(r, c, p)
                        winner = checkBigWin()
                        if winner != 0:
                            endMessage = "player " + str(winner) + " won"
                            print(endMessage)
                            main = False
                            end = True
                        if moves == 81 and winner != 1 and winner != 2:
                            tie = True
                    else:
                        # in the grid 
                        largegrid[sX][sY] = turn
                        if turn == 1:
                            turn = 2
                        elif turn == 2:
                            turn = 1
                        sSelected = False
                else:
                    sX = initSX
                    sY = initSY
                    selected = True
            if event.key == pygame.K_q:
                main = False
    # create translucent gray blocks 
    for nX in range (3):
        for nY in range(3):
            if (nX, nY) != (initX, initY):
                grayblock(nX, nY, GRAY, 4)
    # create small blocks inside the external games
    for snX in range(initSX, initSX + 3):
        for snY in range(initSY, initSY + 3):
            if selected:
                if (snX,snY) == (initX, initY):
                    grayblock(snX, snY, GRAY, 4)
                if (snX, snY) != (sX, sY):
                    # if (snX and snY > sX) and (snX and snY < sX + 3 + 1): 
                    sGrayBlock(snX, snY)  
                    
    drawMatrix()
    drawSmallGrid()

    drawGrid(width, height, WHITE)
    
while end:
    # displaying end scren
    screen.fill(PURPLEICE)
    # declare end cases
    if winner == 1:
        endRun += 1
        if endRun == 1:
            screen.fill(RED)
            drawGrid(width, height, WHITE)
            textEnd = fontEnd.render(str("GAME OVER PLAYER 1 WINS"), True, BLUE)
            textRest = fontEnd.render(str("PRESS R TO RESTART"), True, BLUE)
            endRect = textEnd.get_rect(center=(endX, endY - 20))
            restRect = textRest.get_rect(center=(restX, restY - 20))
            screen.blit(textEnd, endRect)
            screen.blit(textRest, restRect)
            pygame.display.flip()
    if winner == 2:
        endRun += 1
        if endRun == 1:
            screen.fill(BLUE)
            drawGrid(width, height, WHITE)
            textEnd = fontEnd.render(str("GAME OVER PLAYER 2 WINS"), True, RED)
            textRest = fontEnd.render(str("PRESS R TO RESTART"), True, RED)
            endRect = textEnd.get_rect(center=(endX, endY - 20))
            restRect = textRest.get_rect(center=(restX, restY - 20))
            screen.blit(textEnd, endRect)
            screen.blit(textRest, restRect)
            pygame.display.flip()
    if tie:
        endRun += 1
        if endRun == 1:
            screen.fill(WHITE)
            drawGrid(width, height, WHITE)
            textEnd = fontEnd.render(str("TIE"), True, BLUE)
            textRest = fontEnd.render(str("PRESS R TO RESTART"), True, BLUE)
            endRect = textEnd.get_rect(center=(endX, endY - 20))
            restRect = textRest.get_rect(center=(restX, restY - 20))
            screen.blit(textEnd, endRect)
            screen.blit(textRest, restRect)
            pygame.display.flip()
    for event in pygame.event.get(): # check for any events (i.e key press, mouse click etc.)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                restart()
        if event.type == pygame.QUIT: # check to see if it was "x" at top right of screen
            exit() # call the exit function to quit pygame and exit the program (i.e. close everything down)

# quit game
pygame.quit()
sys.exit()