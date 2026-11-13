import pygame
import os
from sys import exit

pygame.init()
screen= pygame.display.set_mode((512,512))
pygame.display.set_caption("X si 0")
clock=pygame.time.Clock()
usb_drive_path='D:\\' #Modifica linia asta la scoala
image_dir = os.path.join(usb_drive_path, 'x si 0', 'Graphics')
board = pygame.image.load(os.path.join(image_dir, 'board.png'))
x_image = pygame.image.load(os.path.join(image_dir, 'x.png'))
o_image = pygame.image.load(os.path.join(image_dir, '0.png'))
victorie_x = pygame.image.load(os.path.join(image_dir, 'X_castiga.png'))
victorie_o = pygame.image.load(os.path.join(image_dir, 'O_castiga.png'))
game_board =   [[None, None, None],
                [None, None, None],
                [None, None, None]]
player=0
winner=None
gameover=True
def restart():
    global game_board, player, gameover,winner
    gameover = True
    game_board = [[None, None, None],
                [None, None, None],
                [None, None, None]]
    player = 0
    winner=None
    screen.blit(board, (0, 0))
def check_winner(game_board):
    for row in game_board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    
    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] and game_board[0][col] is not None:
            return game_board[0][col]
    
    if game_board[0][0] == game_board[1][1] == game_board[2][2] and game_board[0][0] is not None:
        return game_board[0][0]
    if game_board[0][2] == game_board[1][1] == game_board[2][0] and game_board[0][2] is not None:
        return game_board[0][2]

    return None

while gameover:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row= pos[1]//(board.get_height()//3)
            col= pos[0]//(board.get_width()//3)
            if game_board[row][col] is None:
                game_board[row][col]= player
                x = col * (board.get_width() // 3) + board.get_width() // 6
                y = row * (board.get_height() // 3) + board.get_height() // 6
                if player == 0:
                    screen.blit(x_image, (x - x_image.get_width() // 2, y - x_image.get_height() // 2))
                else:
                    screen.blit(o_image, (x - o_image.get_width() // 2, y - o_image.get_height() // 2))
                player = 1 - player
                
                winner = check_winner(game_board)
                if winner is not None:
                    if (winner == 0):
                        screen.blit(victorie_x, (0, 0))
                    if (winner == 1):
                        screen.blit(victorie_o, (0, 0))
                    pygame.display.update()
                    pygame.time.delay(1000) 
                    restart()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            restart()
    screen.blit(board, (0, 0))
    
    for row in range(3):
        for col in range (3):
            if game_board[row][col]==0:
                x = col * (board.get_width() // 3) + board.get_width() // 6
                y = row * (board.get_height() // 3) + board.get_height() // 6
                screen.blit(x_image, (x - x_image.get_width() // 2, y - x_image.get_height() // 2))
            elif game_board[row][col]==1:
                x = col * (board.get_width() // 3) + board.get_width() // 6
                y = row * (board.get_height() // 3) + board.get_height() // 6
                screen.blit(o_image, (x - o_image.get_width() // 2, y - o_image.get_height() // 2))
        
    pygame.display.update()
    clock.tick(60)
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            restart()
    winner = check_winner(game_board)
    if(winner==0):
        screen.blit(victorie_x,(0,0))
    if(winner==1):
        screen.blit(victorie_o,(0,0))
    pygame.display.update()
    clock.tick(60)