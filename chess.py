from chess_board import Chess_Board

a=Chess_Board()
a.display()
while True:
    try:
        a.move()
        a.display()
    except:
        print("Something went wrong. Please check your move")