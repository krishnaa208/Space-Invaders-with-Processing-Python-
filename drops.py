class Drop:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.r=8
        self.toDelete = 0
    
    def show(self):
        fill(200)
        ellipse(self.x,self.y,self.r*2,self.r*2)
    
    def move(self):
        noStroke()
        self.y = self.y - 3
        
    def hits(self,flower):
        d = dist(self.x,self.y,flower.x,flower.y)
        
        if d < self.r + flower.r :
            return True
        else :
            return False
        
    def evaporate(self):
        self.toDelete = 1
        
        
        