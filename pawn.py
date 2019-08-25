class Pawn:
    def __init__(self,x,y,sl,team):
        self.name = 'Pawn'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team
    def req(self,sx,sy,dx,dy,board):
            if board[sx][sy].team == "white" and dx-sx == -1:
                return True
            elif board[sx][sy].team == 'black' and dx-sx == 1:
                return True
            else:
                return False
