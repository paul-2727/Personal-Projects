class Pieces():
    def __init__(self,is_bombastic):
        self.is_bombastic = is_bombastic
        self.clicked = False
        self.flag = False
        
    def ReturnBomb(self):
        return self.is_bombastic
    
    def ReturnClicked(self):
        return self.clicked
    
    def ReturnFlag(self):
        return self.flag
    def HandleClick(self):
        self.clicked=True 
    def Neighbors(self,neighbors):
        self.neighbors =neighbors
        self.SetNumBlock()
    def SetNumBlock(self):
        self.numBlock=0
        for piece in self.neighbors:
            if(piece.ReturnBomb()):
                self.numBlock+=1
    def GetNumBlock(self):
        return self.numBlock
    def ToggleFlag(self):
        self.flag=not self.flag
    def ReturnNeighbors(self):
        return self.neighbors