import pygame, sys, time
from constants import *
from random import *
from math import *
from pygame.locals import *

board = 4
points = 0
score = 2
r = [2, 4]
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("bensound-hipjazz.mp3")
pygame.mixer.music.play(-1, 0.0)
display = pygame.display.set_mode((400, 500), 0, 32)
pygame.display.set_caption("2048")
myfont = pygame.font.SysFont("monospace", 40)
endfont = pygame.font.SysFont("monospace",20)
scorefont = pygame.font.SysFont("monospace", 30)
matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
undomat = []

def main(loaded=False):
    if not loaded:
        placeRandom()
        placeRandom()
    printmatrix()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                close()

            if check() == True:
                if event.type == KEYDOWN:
                    if arrow(event.key):
                        rotations = getrotations(event.key)
                        addtoundo()
                        for i in range(0, rotations):
                            rotateclockwise()

                        if canmove():
                            movetiles()
                            mergetiles()
                            placeRandom()

                        for j in range(0, (4 - rotations) % 4):
                            rotateclockwise()
                        printmatrix()
            else:
                gameover()
            if event.type == KEYDOWN:
                    global board
                    if event.key == pygame.K_r:
                        reset()
                    if 50 < event.key and 56 > event.key:
                        board = i.key - 48
                        reset()
                    if event.key == pygame.K_s:

                        savegame()
                    elif event.key == pygame.K_l:
                        loadgame()

                    elif event.key == pygame.K_u:
                        undo()
                    elif event.key == pygame.K_q:
                        close()
                    elif event.key == pygame.K_h:
                        highscore()
        pygame.display.update()


def canmove():
    for i in range(0, board):
        for j in range(1, board):
            if (matrix[i][j - 1] == 0 and matrix[i][j] > 0):
                return True
            elif (matrix[i][j - 1] == matrix[i][j]) and matrix[i][j - 1] != 0:
                return True
    return False


def movetiles():
    for i in range(0, board):
        for j in range(0, board - 1):
            while (matrix[i][j] == 0 and sum(matrix[i][j:]) > 0):
                for k in range(j, board - 1):
                    matrix[i][k] = matrix[i][k + 1]
                matrix[i][board - 1] = 0


def mergetiles():
    global points
    for i in range(0, board):
        for j in range(0, board - 1):
            if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != 0:
                matrix[i][j] = matrix[i][j] * 2
                matrix[i][j + 1] = 0
                points += matrix[i][j]
                movetiles()


def placeRandom():
    c = 0
    for i in range(0, board):
        for j in range(0, board):
            if matrix[i][j] == 0:
                c += 1
    k = floor(random() * board * board)
    while (matrix[floor(k / board)][k % board] != 0):
        k = floor(random() * board * board)
    matrix[floor(k / board)][k % board] = choice(r)


def printmatrix():
    display.fill(BLACK)
    global points
    global board
    for i in range(0, board):
        for j in range(0, board):
            pygame.draw.rect(display, getColor(matrix[i][j]),
                             (i * (400 / board), j * (400 / board) + 100, 400 / board, 400 / board))
            label = myfont.render(str(matrix[i][j]), 1, (255, 255, 255))
            label2 = scorefont.render("YourScore:" + str(points), 1, (255, 255, 255))
            display.blit(label, (i * (400 / board) + 30, j * (400 / board) + 130))
            display.blit(label2, (10, 20))


def check():
    for i in range(0, board ** 2):
        if matrix[floor(i / board)][i % board] == 0:
            return True
    for i in range(0, board):
        for j in range(0, board - 1):
            if matrix[i][j] == matrix[i][j + 1]:
                return True
            elif matrix[j][i] == matrix[j + 1][i]:
                return True
    return False


def convert():
    mat = []
    for i in range(0, board ** 2):
        mat.append(matrix[floor(i / board)][i % board])
    mat.append(points)
    return mat


def addtoundo():
    undomat.append(convert())


def rotateclockwise():
    for i in range(0, int(board / 2)):
        for j in range(i, int(board - i - 1)):
            temp1 = matrix[i][j]
            temp2 = matrix[board - 1 - j][i]
            temp3 = matrix[board - 1 - i][board - 1 - j]
            temp4 = matrix[j][board - 1 - i]

            matrix[board - 1 - j][i] = temp1
            matrix[board - 1 - i][board - 1 - j] = temp2
            matrix[j][board - 1 - i] = temp3
            matrix[i][j] = temp4


def gameover():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("15 - 1-Down.mp3")
    pygame.mixer.music.play(0, 0.0)
    pygame.mixer.music.stop()
    global points
    display.fill(BLACK)
    label = scorefont.render("Game Over", 1, (255, 255, 255))
    label2 = scorefont.render("Score : " + str(points), 1, (255, 255, 255))
    label3 = endfont.render("Press R to Play Again ", 1, (255, 255, 255))
    label4 = endfont.render("Press H to view Scores ", 1, (255, 255, 255))
    label5 = endfont.render("Press Q to Quit ", 1, (255, 255, 255))
    display.blit(label, (50, 50))
    display.blit(label2, (50, 100))
    display.blit(label3 , (50, 200))
    display.blit(label4, (50, 300))
    display.blit(label5, (50, 400))

def reset():
    global points
    global matrix
    points = 0
    display.fill(BLACK)
    for i in range(0, board):
        for j in range(0, board):
            matrix[i][j] = 0
    main()


def savegame():
    f = open("savedata", "w")

    line1 = " ".join([str(matrix[floor(x / board)][x % board]) for x in range(0, board ** 2)])
    f.write(line1 + "\n")
    f.write(str(board) + "\n")
    f.write(str(board))
    f.close()


def undo():
    if len(undomat) > 0:
        mat = undomat.pop()

        for i in range(0, board ** 2):
            matrix[floor(i / board)][i % board] = mat[i]
        global points
        points = mat[board ** 2]

        printmatrix()


def loadgame():
    global points
    global board
    global matrix

    f = open("savedata", "r")

    mat = (f.readline()).split(' ', board ** 2)
    board = int(f.readline())
    points = int(f.readline())

    for i in range(0, board ** 2):
        matrix[floor(i / board)][i % board] = int(mat[i])

    f.close()

    main(True)


def arrow(k):
    return (k == pygame.K_UP or k == pygame.K_DOWN or k == pygame.K_LEFT or k == pygame.K_RIGHT)


def getrotations(k):
    if k == pygame.K_UP:
        return 0
    elif k == pygame.K_DOWN:
        return 2
    elif k == pygame.K_LEFT:
        return 1
    elif k == pygame.K_RIGHT:
        return 3
def close():
    global points
    from store import saving
    from record import fn,ln,age
    #print(fn,ln,age)
    saving(fn, ln, age, points)
    pygame.quit()
    sys.exit()

def highscore():
   from highscores import high
   high()