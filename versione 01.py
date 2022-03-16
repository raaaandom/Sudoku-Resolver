#Importing Libs
import numpy
import pygame
import win32gui
import win32api
from math import ceil, floor

#Window Creation
WINDOW_OFFSET = 2
WINDOW_WIDTH = 450 + WINDOW_OFFSET*2
WINDOW_HEIGHT = 450 + WINDOW_OFFSET*2
WINDOW_TITLE = "SudokuSolver"
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.NOFRAME)
pygame.display.set_caption(WINDOW_TITLE)

#Loading Images
BOARD_IMAGE = pygame.image.load("assets/grid/grid.png")

SYMBOL_IMAGE = numpy.empty(10,pygame.Surface)
SYMBOL_IMAGE[0] = pygame.image.load("assets/symbols/empty.png")
SYMBOL_IMAGE[1] = pygame.image.load("assets/symbols/1.png")
SYMBOL_IMAGE[2] = pygame.image.load("assets/symbols/2.png")
SYMBOL_IMAGE[3] = pygame.image.load("assets/symbols/3.png")
SYMBOL_IMAGE[4] = pygame.image.load("assets/symbols/4.png")
SYMBOL_IMAGE[5] = pygame.image.load("assets/symbols/5.png")
SYMBOL_IMAGE[6] = pygame.image.load("assets/symbols/6.png")
SYMBOL_IMAGE[7] = pygame.image.load("assets/symbols/7.png")
SYMBOL_IMAGE[8] = pygame.image.load("assets/symbols/8.png")
SYMBOL_IMAGE[9] = pygame.image.load("assets/symbols/9.png")

#RGB Init
rgb_on = False
board_color = [85,170,255]
color_fade_speed = 0.5
rgb_r_up = False
rgb_r_dw = True
rgb_g_up = True
rgb_g_dw = False
rgb_b_up = True
rgb_b_dw = False

#Window Move Init
hwnd = win32gui.FindWindow(None, WINDOW_TITLE)

#Function that returns a new empty board
def createBoard():
    board = [[0 for i in range(9)] for j in range(9)]
    return board

#Creating the main board
mainBoard = createBoard()

#Function that listens to events
def listenEvents():
    global running, rgb_on, mainBoard

    #Event Section
    for event in pygame.event.get():
        
        #Close Window
        if event.type == pygame.QUIT:
            running = False

    #Keyboard Section
    keysDown = pygame.key.get_pressed()

    #Move Window
    if(keysDown[pygame.K_SPACE]):
        global oldCursorPos
        cursorPos = win32api.GetCursorPos()
        windowPos = win32gui.GetWindowRect(hwnd)
        win32gui.MoveWindow(hwnd, windowPos[0] - (oldCursorPos[0] - cursorPos[0]), windowPos[1] - (oldCursorPos[1] - cursorPos[1]), WINDOW_WIDTH, WINDOW_HEIGHT, True)

    #RGB Mode
    if(keysDown[pygame.K_F1]):
        rgb_on = True

    #Set numbers
    if(keysDown[pygame.K_0]):
        mpos = pygame.mouse.get_pos()
        x = ( mpos[0] - WINDOW_OFFSET ) / 50 - 1
        y = ( mpos[1] - WINDOW_OFFSET ) / 50 - 1
        mainBoard[ceil(y)][ceil(x)] = 0
    if(keysDown[pygame.K_1]):
        mpos = pygame.mouse.get_pos()
        x = ( mpos[0] - WINDOW_OFFSET ) / 50 - 1
        y = ( mpos[1] - WINDOW_OFFSET ) / 50 - 1
        mainBoard[ceil(y)][ceil(x)] = 1
    if(keysDown[pygame.K_2]):
        mpos = pygame.mouse.get_pos()
        x = ( mpos[0] - WINDOW_OFFSET ) / 50 - 1
        y = ( mpos[1] - WINDOW_OFFSET ) / 50 - 1
        mainBoard[ceil(y)][ceil(x)] = 2
    if(keysDown[pygame.K_3]):
        mpos = pygame.mouse.get_pos()
        x = ( mpos[0] - WINDOW_OFFSET ) / 50 - 1
        y = ( mpos[1] - WINDOW_OFFSET ) / 50 - 1
        mainBoard[ceil(y)][ceil(x)] = 3
    if(keysDown[pygame.K_4]):
        mpos = pygame.mouse.get_pos()
        x = ( mpos[0] - WINDOW_OFFSET ) / 50 - 1
        y = ( mpos[1] - WINDOW_OFFSET ) / 50 - 1
        mainBoard[ceil(y)][ceil(x)] = 4
    if(keysDown[pygame.K_5]):
        mpos = pygame.mouse.get_pos()
        x = ( mpos[0] - WINDOW_OFFSET ) / 50 - 1
        y = ( mpos[1] - WINDOW_OFFSET ) / 50 - 1
        mainBoard[ceil(y)][ceil(x)] = 5
    if(keysDown[pygame.K_6]):
        mpos = pygame.mouse.get_pos()
        x = ( mpos[0] - WINDOW_OFFSET ) / 50 - 1
        y = ( mpos[1] - WINDOW_OFFSET ) / 50 - 1
        mainBoard[ceil(y)][ceil(x)] = 6
    if(keysDown[pygame.K_7]):
        mpos = pygame.mouse.get_pos()
        x = ( mpos[0] - WINDOW_OFFSET ) / 50 - 1
        y = ( mpos[1] - WINDOW_OFFSET ) / 50 - 1
        mainBoard[ceil(y)][ceil(x)] = 7
    if(keysDown[pygame.K_8]):
        mpos = pygame.mouse.get_pos()
        x = ( mpos[0] - WINDOW_OFFSET ) / 50 - 1
        y = ( mpos[1] - WINDOW_OFFSET ) / 50 - 1
        mainBoard[ceil(y)][ceil(x)] = 8
    if(keysDown[pygame.K_9]):
        mpos = pygame.mouse.get_pos()
        x = ( mpos[0] - WINDOW_OFFSET ) / 50 - 1
        y = ( mpos[1] - WINDOW_OFFSET ) / 50 - 1
        mainBoard[ceil(y)][ceil(x)] = 9

    #Variable that needs to be up to date
    oldCursorPos = win32api.GetCursorPos()

    #Compute board
    if(keysDown[pygame.K_RIGHT]):
        mainBoard = computeBoard(mainBoard)

#Function that renders the board
def renderBoard():
    window.fill(tuple(board_color))

    #RGB Color Changer
    if(rgb_on):
        global rgb_r_up, rgb_r_dw, rgb_g_up, rgb_g_dw, rgb_b_up, rgb_b_dw

        if(board_color[0] == 0):
           rgb_r_up = True
           rgb_r_dw = False
   
        if(board_color[1] == 0):
           rgb_g_up = True
           rgb_g_dw = False
   
        if(board_color[2] == 0):
           rgb_b_up = True
           rgb_b_dw = False
   
        if(board_color[0] == 255):
           rgb_r_up = False
           rgb_r_dw = True
   
        if(board_color[1] == 255):
           rgb_g_up = False
           rgb_g_dw = True
   
        if(board_color[2] == 255):
           rgb_b_up = False
           rgb_b_dw = True
       
        if(rgb_r_up): board_color[0] += color_fade_speed
        if(rgb_r_dw): board_color[0] -= color_fade_speed
        if(rgb_g_up): board_color[1] += color_fade_speed
        if(rgb_g_dw): board_color[1] -= color_fade_speed
        if(rgb_b_up): board_color[2] += color_fade_speed
        if(rgb_b_dw): board_color[2] -= color_fade_speed

    #Render Board
    window.blit(BOARD_IMAGE,(WINDOW_WIDTH/2-BOARD_IMAGE.get_width()/2, WINDOW_HEIGHT/2-BOARD_IMAGE.get_height()/2))

    #Render Numbers
    for y in range(9):
        for x in range(9):
            window.blit(SYMBOL_IMAGE[mainBoard[y][x]], (WINDOW_OFFSET + 50 * x, WINDOW_OFFSET + 50 * y))
  
    pygame.display.update()

#Function that elaborates the board content
def computeBoard(board = []):

    for y in range(9):
        for x in range(9):
            if(board[y][x] == 0):

                possibleEntries = [1,2,3,4,5,6,7,8,9]

                #Vertical check
                for y2 in range(9):
                    try:
                        possibleEntries.remove(board[y2][x])
                    except ValueError:
                        pass
                    
                #Horizzontal check
                for x2 in range(9):
                    try:
                        possibleEntries.remove(board[y][x2])
                    except ValueError:
                        pass
                    
                #Square Check
                xSquareIndex = floor(x/3)
                ySquareIndex = floor(y/3)
                xSquarePos = 3*xSquareIndex
                ySquarePos = 3*ySquareIndex
                for y2 in range(ySquarePos,ySquarePos+3):
                    for x2 in range(xSquarePos,xSquarePos+3):
                        try:
                            possibleEntries.remove(board[y2][x2])
                        except ValueError:
                            pass
                #Popping empty indexes
                for i in range(len(possibleEntries)):
                    if possibleEntries[i] == None:
                        possibleEntries.pop[i]

                #If only one value is possible set that
                if(len(possibleEntries) == 1):
                    board[y][x] = possibleEntries[0]

    return board

running = True
while running:

    listenEvents()
    renderBoard()

pygame.quit()