import random

class Flower:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y 
        self.r = 30
        self.xdir = 1
        self.toDelete = 0
        self.intensity = '#90c56b'
        
        
    def show(self):
        fill(self.intensity)
        ellipse(self.x,self.y,self.r*2,self.r*2)
        
    def grow(self):
        self.r += 2
        
    def move(self):
        self.x = self.x + self.xdir
        
    
    def shift(self):
        self.xdir = self.xdir * -1
        self.y  = self.y + self.r
        
    def explode(self):
        if self.r > 40 and self.r < 45:
            self.intensity = '#e6c573'
        elif self.r > 45 and self.r < 55:
            self.intensity = '#ff6363'            
        elif self.r > 55 :
            self.toDelete = 1
            
    
    
        