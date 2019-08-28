class Condition:

    def range(x,y):
        if x < 0 and y < 0 :
            return False
        if x > 7 and y > 7 :
            return False

    def if_figure(board,x,y):
        return board[x][y].sl == '.'

    def same_team(x1,y1,x2,y2,board):
        if board[x1][y1].team == board[x2][y2].team:
            return True
        else:
            return False

    def s_choice(board):
        while True:
            try:
                print('give x and y')
                x = int(input("x:"))
                y = int(input("y:"))
            except:
                print('Coordinates can only be integers')
            if Condition.range(x,y):
                print('Coordinates are out of range')
            elif Condition.if_figure(board,x,y):
                print('Square chosen by you is empty')
            else:
                return x,y
                break

    def d_choice(board):
        while True:
            try:
                print('give x and y')
                x=int(input())
                y=int(input())
            except:
                print('Coordinates can only be integers')
            if Condition.range(x,y):
                print('Coordinates are out of range')
            else:
                return x,y
                break

    def kill(x1,y1,x2,y2,board):
        if board[x1][y1].team == 'white' and board[x2][y2].team == 'black':
            return True
        elif board[x1][y1].team == 'black' and board[x2][y2].team == 'white':
            return True
        else:
            return False

    def Pawnkill(x1,y1,x2,y2,board):
        if board[x1][y1].team == 'white' and board[x2][y2].team == 'black' and board[x1][y1].name == 'Pawn':
            return True
        elif board[x1][y1].team == 'black' and board[x2][y2].team == 'white'and board[x1][y1].name == 'Pawn':
            return True
        else:
            return False


    def solid(x1,y1,x2,y2,board):
        if board[x1][y1].name=='Rook':
            if x2>x1:
                for i in range(x1+1,x2):
                    if board[i][y1].sl != '.':
                        return False
                        break
            elif x2<x1:
                for i in range(x2+1,x1):
                    if board[i][y1].sl != '.':
                        return False
                        break
            elif y2>y1:
                for j in range(y1+1,y2):
                    if board[x1][j].sl != '.':
                        return False
                        break
            elif y2<y1:
                for j in range(y2+1,y1):
                    if board[x1][j].sl != '.':
                        return False
                        break
            else:
                return True


        elif board[x1][y1].name=='Bishop':
            if x2>x1 and y2>y1:
                for i in range(x1+1,x2):
                    for j in range(y1+1,y2):
                        if board[i][j].sl != '.':
                            return False
                            break
            elif x2<x1 and y2<y1:
                for i in range(x2+1,x1):
                    for j in range(y2+1,y1):
                        if board[i][j].sl != '.':
                            return False
                            break
            elif x2<x1 and y2>y1:
                for i in range(x2+1,x1):
                    for j in range(y1+1,y2):
                        if board[i][j].sl != '.':
                            return False
                            break
            elif x2>x1 and y2<y1:
                for i in range(x1+1,x2):
                    for j in range(y2+1,y1):
                        if board[i][j].sl != '.':
                            return False
                            break
            else:
                return True

        elif board[x1][y1].name=='Queen':
            if x2>x1 and y2>y1:
                for i in range(x1+1,x2):
                    for j in range(y1+1,y2):
                        if board[i][j].sl != '.':
                            return False
                            break
            elif x2<x1 and y2<y1:
                for i in range(x2+1,x1):
                    for j in range(y2+1,y1):
                        if board[i][j].sl != '.':
                            return False
                            break
            elif x2<x1 and y2>y1:
                for i in range(x2+1,x1):
                    for j in range(y1+1,y2):
                        if board[i][j].sl != '.':
                            return False
                            break
            elif x2>x1 and y2<y1:
                for i in range(x1+1,x2):
                    for j in range(y2+1,y1):
                        if board[i][j].sl != '.':
                            return False
                            break
            elif x2>x1:
                for i in range(x1+1,x2):
                    if board[i][y1].sl != '.':
                        return False
                        break
            elif x2<x1:
                for i in range(x2+1,x1):
                    if board[i][y1].sl != '.':
                        return False
                        break
            elif y2>y1:
                for j in range(y1+1,y2):
                    if board[x1][j].sl != '.':
                        return False
                        break
            elif y2<y1:
                for j in range(y2+1,y1):
                    if board[x1][j].sl != '.':
                        return False
                        break

            else:
                return True



        else:
            return True

