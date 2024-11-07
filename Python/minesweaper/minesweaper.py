import pygame
from game import Game 
from board import Board
height=9
length=9
size=(height,length)
prob = 0.1
def matrix_area(height, length):
    area = height * length
    return area
NumberBombs=round( matrix_area(height, length) * prob)
board= Board(size,prob)
screensize=(810,810)
game=Game(board,screensize)
game.run()