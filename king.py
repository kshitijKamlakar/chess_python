class King:
    def __init__(self,x,y,sl,team):
        self.name = 'King'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team

    def req(self,sx,sy,dx,dy,board):
            if  abs(dx-sx) < 2 and abs(dy-sy) <  2 :
                return True
            else:
                return False

