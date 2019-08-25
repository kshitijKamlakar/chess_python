from empty import Empty
from rook import Rook
from knight import Knight
from queen import Queen
from pawn import Pawn
from bishop import Bishop
from king import King
from condition import Condition
from number import Number
class Chess_Board:
    def __init__(self):
        self.board = [[Empty(x='',y='',sl='.',team='')]*9 for _ in range(9)]
        self.board[0][0] = Rook(x=0,y=0,sl='r',team='black')
        self.board[0][1] = Knight(x=0,y=1,sl='n',team='black')
        self.board[0][2] = Bishop(x=0,y=2,sl='b',team='black')
        self.board[0][3] = Queen(x=0,y=3,sl='q',team='black')
        self.board[0][4] = King(x=0,y=4,sl='k',team='black')
        self.board[0][5] = Bishop(x=0,y=5,sl='b',team='black')
        self.board[0][6] = Knight(x=0,y=6,sl='n',team='black')
        self.board[0][7] = Rook(x=0,y=7,sl='r',team='black')
        self.board[1][0] = Pawn(x=1,y=0,sl='p',team='black')
        self.board[1][1] = Pawn(x=1,y=1,sl='p',team='black')
        self.board[1][2] = Pawn(x=1,y=2,sl='p',team='black')
        self.board[1][3] = Pawn(x=1,y=3,sl='p',team='black')
        self.board[1][4] = Pawn(x=1,y=4,sl='p',team='black')
        self.board[1][5] = Pawn(x=1,y=5,sl='p',team='black')
        self.board[1][6] = Pawn(x=1,y=6,sl='p',team='black')
        self.board[1][7] = Pawn(x=1,y=7,sl='p',team='black')
        self.board[7][0] = Rook(x=7,y=0,sl='R',team='white')
        self.board[7][1] = Knight(x=7,y=1,sl='N',team='white')
        self.board[7][2] = Bishop(x=7,y=2,sl='B',team='white')
        self.board[7][3] = Queen(x=7,y=3,sl='Q',team='white')
        self.board[7][4] = King(x=7,y=4,sl='K',team='white')
        self.board[7][5] = Bishop(x=7,y=5,sl='B',team='white')
        self.board[7][6] = Knight(x=7,y=6,sl='N',team='white')
        self.board[7][7] = Rook(x=7,y=7,sl='R',team='white')
        self.board[6][0] = Pawn(x=3,y=0,sl='P',team='white')
        self.board[6][1] = Pawn(x=6,y=1,sl='P',team='white')
        self.board[6][2] = Pawn(x=6,y=2,sl='P',team='white')
        self.board[6][3] = Pawn(x=6,y=3,sl='P',team='white')
        self.board[6][4] = Pawn(x=6,y=4,sl='P',team='white')
        self.board[6][5] = Pawn(x=6,y=5,sl='P',team='white')
        self.board[6][6] = Pawn(x=6,y=6,sl='P',team='white')
        self.board[6][7] = Pawn(x=6,y=7,sl='P',team='white')
        for i in range(9):
            self.board[i][8 ]= Number(sl=i)
        for j in range(9):
            self.board[8][j] = Number(sl=j)

    def display(self):
        for i in range(9):
            for j in range(9):
                print (self.board[i][j].sl, end=' ')
            print()



    def move(self):
        while True:
            print('Give a position of figure')
            sx,sy=Condition.s_choice(self.board)
            print(self.board[sx][sy].name)
            print('Now choose a destnation')
            dx,dy=Condition.d_choice(self.board)
            mark_same=Condition.same_team(sx,sy,dx,dy,self.board)
            mark_kill=Condition.kill(sx,sy,dx,dy,self.board)
            mark_Pawnkill=Condition.Pawnkill(sx,sy,dx,dy,self.board)
            mark_solid=Condition.solid(sx,sy,dx,dy,self.board)
            mark_move=self.board[sx][sy].req(sx,sy,dx,dy,self.board)
            if mark_solid==False:
                print('Figures are not ghosts')

            elif (mark_Pawnkill == True and abs(dx-sx) == abs(dy-sy) and mark_same == False):
                self.board[dx][dy] = self.board[sx][sy]
                self.board[dx][dy].x = dx
                self.board[dx][dy].y = dy
                self.board[sx][sy] = Empty(x='',y='',sl='.',team='')
                return self.board
                break

            elif (mark_move == True and mark_Pawnkill == False and (mark_kill == True or mark_same == False)):
                self.board[dx][dy] = self.board[sx][sy]
                self.board[dx][dy].x = dx
                self.board[dx][dy].y = dy
                self.board[sx][sy] = Empty(x='',y='',sl='.',team='')
                return self.board
                break
            else:
                print('Figure can not move here, try again')
                continue
