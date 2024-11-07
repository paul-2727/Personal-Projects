from pieces import Pieces
import random
class Board():
    def __init__(self, size,prob):
        self.size = size
        self.prob=prob
        self.lost=False
        self.NumClicked = 0
        self.NoBomb = 0
        self.SetBoard()
    def Clear(self):
        self.lost=False
        self.NumClicked = 0
        self.NoBomb = 0
        self.SetBoard()
    def SetBoard(self):
        self.board=[]
        for row in range(self.size[0]):
            row=[]
            for col in range(self.size[1]):
                is_bombastic= random.random() < self.prob
                if(not is_bombastic):
                    self.NoBomb+=1
                piece=Pieces(is_bombastic)
                row.append(piece)
            self.board.append(row)
        self.Neighbors()
    def Neighbors(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.GetPiece((row, col))
                neighbors = self.NeighborsList((row, col))
                piece.Neighbors(neighbors)
    def NeighborsList(self,value):
        neighbors = []
        for row in range (value[0]-1,value[0]+2):
            for col in range(value[1]-1, value[1]+2):
                outofbounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                same = row == value[0] and col == value[1]
                if(same or outofbounds):
                    continue
                neighbors.append(self.GetPiece((row,col)))
        return neighbors
    def GetSize(self):
        return self.size
    def GetPiece(self,value):
        return self.board[value[0]][value[1]]
    def HandleClick(self,Pieces, flag,):
        if Pieces.ReturnClicked() or (Pieces.ReturnFlag() and not flag):
            return
        if flag:
            Pieces.ToggleFlag()
            return
        Pieces.HandleClick()
        if(Pieces.ReturnBomb()):
            self.lost=True
            return
        self.NumClicked+=1
        if(Pieces.GetNumBlock()!=0):
            return
        for neighbor in Pieces.ReturnNeighbors():
            if(not neighbor.ReturnBomb() and not neighbor.ReturnClicked()):
                self.HandleClick(neighbor,False)
    def CheckWon(self):
        for row in self.board:
            for Pieces in row:
                if not Pieces.ReturnBomb() and not Pieces.ReturnClicked():
                    return False
    def ReturnLost(self):
        return self.lost
    def ReturnWin(self):
        return self.NoBomb==self.NumClicked
