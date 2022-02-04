from Paddle import Paddle
from Screen import Screen
from Ball import Ball

class Pong:
    def __init__(self) -> None:

        screen = Screen()
        ball = Ball()

        paddle_left = Paddle("red",-350)
        paddle_right = Paddle("blue", 350)     
        
        screen.wn.onkeypress(paddle_left.moveup, "w" )
        screen.wn.onkeypress(paddle_left.movedown, "s" )
        screen.wn.onkeypress(paddle_right.moveup, "Up")
        screen.wn.onkeypress(paddle_right.movedown, "Down")
          
        while True:
                screen.wn.update()                
                ball.move()



if __name__ == "__main__":
    Pong()




