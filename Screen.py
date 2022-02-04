import turtle
class Screen:
    def __init__ (self):
        self.wn = turtle.Screen()
        self.wn.title("PONG")
        self.wn.bgcolor("black")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)
        self.wn.listen()   

