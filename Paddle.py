from turtle import Turtle

class Paddle:
     
    def __init__(self, color, position):
        self.paddle = Turtle()
        self.paddle.speed(0)      
        self.paddle.shape("square")   
        self.paddle.color(color)
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(position,0)
       

    def moveup(self):
        y = self.paddle.ycor()
        y +=20
        self.paddle.sety(y)

    def movedown(self):
        y = self.paddle.ycor()
        y -=20
        self.paddle.sety(y)



