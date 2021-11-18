import pygame
from sudokuSolverAlgo import *
from chooseLevel import *
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
L_GREEN = (150, 255, 150)
RED = (255, 0, 0)
L_RED = (255, 204, 203)
GRAY = (60, 60, 60)
L_GRAY = (220, 220, 220)
YELLOW = (255, 255, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = HEIGHT = 50

# This sets the margin between each cell
MARGIN = 5
numbers_1to9 = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8,
                pygame.K_9]

# Set the width and height of the screen [width, height]
size = (500, 500)
# screen = pygame.display.set_mode(size)
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)

# pygame.display.set_caption("Sudoku King")

# Loop until the user clicks the close button.
done = False


def cheatingAllTheWay():
    for row in range(len(Board)):
        for column in range(len(Board[row])):
            Board[row][column] = solvedBoard[row][column]
            addNumToBoard(Board[row][column], row, column, L_GREEN)
            time.sleep(0.05)
            pygame.display.flip()
    finish()


def addNumToBoard(number, row, column, color):
    addNewRect(row, column, WHITE, 5)
    addNewRect(row, column, color, None)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(number), True, BLACK, )
    textRect = text.get_rect()  # get_rect() -> Returns a new rectangle covering the entire surface.
    textRect.center = ((MARGIN + WIDTH) * column + MARGIN + WIDTH / 2, (MARGIN + HEIGHT) * row + MARGIN + WIDTH / 2)
    screen.blit(text, textRect)
    drawTheBorder()


def finish():
    if solvedBoard == Board:
        print("good")
    else:
        print("not good")


def addNewRect(row, col, color, width):
    rectSize = pygame.Rect((MARGIN + WIDTH) * col + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH,
                           HEIGHT)
    if width is not None:
        pygame.draw.rect(screen, color, rectSize, width)  # coloring only the border
    else:
        pygame.draw.rect(screen, color, rectSize)  # coloring the whole rectangle


def flickering(timeFlickering, color):  # flickering with color on-off
    addNewRect(row, column, color, 5)
    pygame.display.flip()
    time.sleep(timeFlickering)
    addNewRect(row, column, WHITE, 5)
    pygame.display.flip()
    time.sleep(timeFlickering)
    addNewRect(row, column, color, 5)
    pygame.display.flip()
    time.sleep(timeFlickering)
    addNewRect(row, column, WHITE, 5)
    pygame.display.flip()


def drawTheBorder():
    dif = 500 // 9
    for i in range(10):
        thick = 5
        pygame.draw.line(screen, GRAY, (0, i * dif + 2), (500, i * dif + 2), thick)
        pygame.draw.line(screen, GRAY, (i * dif + 2, 0), (i * dif + 2, 500), thick)
    for i in range(10):
        if i % 3 == 0:
            thick = 8
            pygame.draw.line(screen, BLACK, (0, i * dif), (500, i * dif), thick)
            pygame.draw.line(screen, BLACK, (i * dif, 0), (i * dif, 500), thick)


def drawInitBoard():
    # printBoard(solvedBoard)
    for row in range(len(Board)):
        for column in range(len(Board[row])):
            color = L_GRAY
            if Board[row][column] == 0:  # if we want to change to background of the empty cells
                color = WHITE
                # ----- drawing the rect ------
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
            # show nothing if the number is 0
            font = pygame.font.Font('freesansbold.ttf', 32)
            if Board[row][column] == 0:
                text = font.render(" ", True, BLACK, )  # render(text, anti-alias[True], color, background=None)
            else:
                text = font.render(str(Board[row][column]), True, BLACK, )

            textRect = text.get_rect()  # get_rect() -> Returns a new rectangle covering the entire surface.
            textRect.center = (
                (MARGIN + WIDTH) * column + MARGIN + WIDTH / 2, (MARGIN + HEIGHT) * row + MARGIN + WIDTH / 2)
            screen.blit(text, textRect)
            drawTheBorder()


# -------- Main Program Loop -----------
if __name__ == "__main__":
    flag1 = True

    while flag1:
        level = chooseLevel()
        if level == 1 or level == 2 or level == 3:
            print(level)
            flag1 = False
    pygame.display.set_caption("Sudoku King1")
    screen = pygame.display.set_mode(size)

    sol = mainSolver(level)  # first at all the script solve the sudoku by itself

    print("solveBoard")
    printBoard(sol)

    # ------ draw the board ------
    pygame.init()
    screen.fill(BLACK)
    drawInitBoard()
    readyForInput = False
    key = None
    while not done:
        # --- Main event loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key in numbers_1to9:
                    key = chr(event.key)
                if event.key == pygame.K_RETURN:
                    finish()
                if event.key == pygame.K_c:
                    cheatingAllTheWay()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # ------ if clicked on a cell get his row and column ------
                if readyForInput is True:
                    addNewRect(row, column, WHITE, None)
                    drawTheBorder()
                    readyForInput = False

                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (WIDTH + MARGIN)
                # ------ checking if it is a empty (0 inside) ------
                if Board[row][column] == 0:
                    # ------ coloring the border of the clicked cell ----- #TODO YELLOW
                   
                    addNewRect(row, column, YELLOW, 5)
                    readyForInput = True
                    # ------ now only wait for input from the user -----

        if readyForInput and key is not None:
            # ------ checking if the key is good at it's place ------
            if int(key) == sol[row][column]:
                Board[row][column] = key
                flickering(0.1, GREEN)  # flickering at a 0.2 seconds with the color green
                addNumToBoard(key, row, column, L_GREEN)
            else:
                flickering(0.1, RED)  # flickering at a 0.2 seconds with the color red
                addNumToBoard(key, row, column, L_RED)

            # -----------------------------------------------
            drawTheBorder()
            readyForInput = False

        key = None
        pygame.display.flip()
        pygame.display.update()


# Close the window and quit.
pygame.quit()
