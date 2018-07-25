 

class Ship:
    
    def __init__(self):
        self.x = width/2
        self.y = height
        self.H = 50
        self.W = 50
        self.r = 50
        self.dir = 0
        self.P = self.W/2
        self.modified = False
    
    def show(self):
        fill(255)
        rectMode(CENTER)
        noStroke()
        rect(self.x,self.y,self.W,self.H-40)
        rect(self.x,self.y,self.W-10,self.H-30)
        rect(self.x,self.y,self.W-20,self.H)
        rect(self.x+self.P,self.y,10,self.H-15)
        rect(self.x-self.P,self.y,10,self.H-15)
        
    def move(self):
        if self.x > 10 and self.dir < 0 :
            self.x = self.x + self.dir*4
        if self.x < width-10 and self.dir > 0 :
            self.x = self.x + self.dir*4
    
    def setdir(self,dir):
        self.dir = dir