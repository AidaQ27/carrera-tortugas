import turtle

class Circuito():
    corredores = []
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.screen = turtle.Screen()
        
        