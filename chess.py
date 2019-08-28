import sys

from pip._vendor.distlib.compat import raw_input

from chess_board import Chess_Board

try :
    a=Chess_Board()
    a.display()
    while True:
        try:
            a.move()
            a.display()
        except KeyboardInterrupt :
            print("Exit")
            sys.exit()
        except:
            print("Something went wrong. Please check your move")

except KeyboardInterrupt :
    print("Exiting")
    exit()