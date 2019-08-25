class Knight:
    def __init__(self,x,y,sl,team):
        self.name = 'Knight'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team

    def req(self,sx,sy,dx,dy,board):
            if  (abs(dx - sx)**2+abs(dy - sy)**2 == 5) :
                return True
            else:
                return False
