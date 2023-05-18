import sys
import time

import numpy as np
from alpha_beta import *
from gui import *
from minmax import *
from windows_gui import *
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROWS = 6
COLS = 7
SQUARE = 80

AI1 = 0
AI2 = 1

width = COLS * SQUARE
height = (ROWS + 1) * SQUARE
size = (width, height)

def initBoard():
    board = np.zeros((ROWS, COLS))
    return board

def printBoard(board):
    print(np.flip(board, 0))
#
# AI1_Level="aaa"
# AI2_Level="bbb"
def main():
    main_window.mainloop()
    print(AI1_Option+" "+AI2_Option+'     llllllllllll')
    #print(AI1_Level+" "+AI2_Level+'     mmmmmmmmmmmmmmm')


    board = initBoard()
    printBoard(board)
    gameOver = False
    pygame.init()
    screen = pygame.display.set_mode(size)
    drawBoard(board)
    pygame.display.update()
    font = pygame.font.SysFont("monospace", 40)
    turn = random.randint(AI1, AI2)

    while not gameOver:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if turn == AI1 and not gameOver:

            if AI1_Option == "MinMax":
                col, minimax_score = minimax(board, 5, True)
            elif AI1_Option == "AlphaBeta":

                # if AI1_Level == "Easy":
                #     AI1_Level=2
                # elif AI1_Level == "Medium":
                #     AI1_Level=4
                # else:
                #     AI1_Level=5

                col, minimax_score = AlphaBeta(board, 5, -math.inf, math.inf, True)
            else:
                col = random.randint(0, 6)

            if isValidLocation(board, col):
                row = nextRow(board, col)
                putPiece(board, row, col, AI1_PIECE)

                if isWin(board, AI1_PIECE):
                    label = font.render("Player 1 wins!!", 1, RED)
                    screen.blit(label, (40, 10))
                    gameOver = True

                printBoard(board)
                drawBoard(board)
                turn += 1
                turn = turn % 2
                time.sleep(1)

        if turn == AI2 and not gameOver:
            if AI2_Option == "MinMax":
                col, minimax_score = minimax(board, 5, True)
            elif AI2_Option == "AlphaBeta":

                # if AI2_Level == "Easy":
                #     AI2_Level=2
                # elif AI2_Level == "Medium":
                #     AI2_Level=4
                # else:
                #     AI2_Level=5

                col, minimax_score = AlphaBeta(board, 5, -math.inf, math.inf, True)
            else:
                col = random.randint(0, 6)

            if isValidLocation(board, col):
                row = nextRow(board, col)
                putPiece(board, row, col, AI2_PIECE)

                if isWin(board, AI2_PIECE):
                    label = font.render("Player 2 wins!!", 1, YELLOW)
                    screen.blit(label, (40, 10))
                    gameOver = True

                printBoard(board)
                drawBoard(board)

                turn += 1
                turn = turn % 2

        if gameOver:
            pygame.time.wait(3000)


main()
