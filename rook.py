
class Rook:
    def __init__(self,x,y,sl,team):
        self.name = 'Rook'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team

    def req(self,sx,sy,dx,dy,board):
            if  ( dx==sx or dy==sy ) :
                return True
            else:
                return False


