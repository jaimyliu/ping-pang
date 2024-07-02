import pygame

class Paddle:
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.color = color
        self.up = 5
        self.score = 0
    def update(self,up,height):
        if up:
            self.y -= self.up
        else:
            self.y += self.up
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > height:
            self.y = height - self.height
        
    def draw(self,window):
        pygame.draw.rect(window,self.color,(self.x,self.y,self.width,self.height))