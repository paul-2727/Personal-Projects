import pygame
import os
import time
from time import sleep
class Game():
    def __init__(self, board, screensize):
        self.image_dir = os.path.abspath("minesweaper\Grafics")
        self.board = board
        self.screensize = screensize
        self.overlay_image=pygame.image.load(os.path.join(self.image_dir, 'win.png'))
        self.piecesize = self.screensize[0] // self.board.GetSize()[1], self.screensize[1] // self.board.GetSize()[0]
        self.LoadImages()
        self.StartTime=time.time()
        self.over=False
    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screensize)
        self.start()
        running=True
        while running:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    RightClick = pygame.mouse.get_pressed()[2]
                    self.Click(position, RightClick)
                if event.type==pygame.MOUSEBUTTONDOWN and self.over==True:
                    self.restart()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        self.restart()
            if not self.over:
                self.draw()
            pygame.display.flip()
            if self.board.ReturnWin():
                self.over=True
                self.end()
            if self.board.ReturnLost():
                self.over=True
                self.lost()
        pygame.quit()
    def end(self):
        self.EndTime = time.time()
        win_image = pygame.image.load(os.path.join(self.image_dir, 'win.png'))
        win_image = pygame.transform.scale(win_image, self.screensize)
        self.screen.blit(win_image, (0, 0))
        pygame.display.flip()
    def lost(self):
        self.EndTime=time.time()
        lose_image = pygame.image.load(os.path.join(self.image_dir, 'lose.png'))
        lose_image = pygame.transform.scale(lose_image, self.screensize)
        self.screen.blit(lose_image, (0, 0))
        pygame.display.flip()
    def start(self):
        self.StartTime = time.time()
        start_image = pygame.image.load(os.path.join(self.image_dir, 'start.png'))
        start_image = pygame.transform.scale(start_image, self.screensize)
        self.screen.blit(start_image, (0, 0))
        pygame.display.flip()
        waiting_for_start = True
        while waiting_for_start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    waiting_for_start = False
    def restart(self):
        self.board.Clear()
        self.StartTime=time.time()
        self.over=False
        self.screen.fill((0,0,0))
        pygame.display.flip()
        self.LoadImages()
    def ReturnTimeTaken(self):
        return self.EndTime - self.StartTime
    def draw(self):
        topleft = (0, 0)
        for row in range(self.board.GetSize()[0]):
            for col in range(self.board.GetSize()[1]):
                piece = self.board.GetPiece((row, col))
                image = self.GetImage(piece)
                self.screen.blit(image, topleft)
                topleft = topleft[0] + self.piecesize[0], topleft[1]
            topleft = (0, topleft[1] + self.piecesize[1])
    def LoadImages(self):
        self.images = {}
        for filename in os.listdir("minesweaper\Grafics"):
            if not filename.endswith(".png"):
                continue
            image = pygame.image.load(os.path.join("minesweaper\Grafics", filename))
            image = pygame.transform.scale(image, self.piecesize)
            self.images[filename.split(".")[0]] = image
    def GetImage(self, piece):
        if piece.ReturnClicked():
            string = "explosion" if piece.ReturnBomb() else str(piece.GetNumBlock())
        else:
            string = "flag" if piece.ReturnFlag() else "block gol"
        return self.images[string]
    def Click(self, position, RightClick):
        if(self.board.ReturnLost()):
            return
        index = position[1] // self.piecesize[1], position[0] // self.piecesize[0]
        self.board.HandleClick( self.board.GetPiece(index), RightClick)