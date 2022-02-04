import turtle

class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0,0)
        self.ball.dx = 0.5
        self.ball.dy = 0.5
    
    def move(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1
        
        elif self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball.dy *= -1                    

        if self.ball.xcor() > 390:
            self.ball.setx(390)
            self.ball.dx *= -1
            
        elif self.ball.xcor() < -390:
            self.ball.setx(-390)
            self.ball.dy *= -1   
