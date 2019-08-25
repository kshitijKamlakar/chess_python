

class Bishop:
    def __init__(self,x,y,sl,team):
        self.name = 'Bishop'
        self.x = x
        self.y = y
        self.sl = sl
        self.team = team

    def req(self,sx,sy,dx,dy,board):
            if  (abs(dx - sx)==abs(dy - sy)) :
                return True
            else:
                return False
