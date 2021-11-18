import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
L_GREEN = (150, 255, 150)
RED = (255, 0, 0)
L_RED = (255, 204, 203)
GRAY = (80, 80, 80)
YELLOW = (255, 255, 0)
#
pygame.init()
X = 300
Y = 200
size = (X, Y)
window = pygame.display.set_mode(size)
font = pygame.font.Font('freesansbold.ttf', 25)



def drawButton(left, top, color, textInButton):
    rectSize = pygame.Rect(left, top, 60, 30)
    pygame.draw.rect(window, color, rectSize)  # left, top, width, height
    pygame.draw.rect(window, BLACK, rectSize, 3)
    fontButton = pygame.font.Font('freesansbold.ttf', 20)
    textButton = fontButton.render(textInButton, True, BLACK, )
    textRectButton = textButton.get_rect()
    textRectButton.center = (left + 30, top + 15)
    window.blit(textButton, textRectButton)


def chooseLevel():
    level = 0
    text = font.render('choose difficulty level', True, BLACK, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2 - 40)

    pygame.display.set_caption("Sudoku King")

    done = True
    while done:
        window.fill(WHITE)
        window.blit(text, textRect)
        drawButton(40, 100, GRAY, "1")
        drawButton(120, 100, GRAY, "2")
        drawButton(200, 100, GRAY, "3")
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print("Click ", pos)
                if (40 <= pos[0] <= 100) and (100 <= pos[1] <= 130):
                    level = 1
                if (120 <= pos[0] <= 180) and (100 <= pos[1] <= 130):
                    level = 2
                if (200 <= pos[0] <= 260) and (100 <= pos[1] <= 130):
                    level = 3
                if level != 0:
                    # print(level)
                    pygame.quit()
                    return level

            # Draws the surface object to the screen.
            pygame.display.update()


# chooseLevel()
