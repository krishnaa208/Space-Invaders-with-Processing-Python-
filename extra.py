class Extra:
    
    def __init__(self,x,y):
        self.r=8
        self.xr=x+self.r*3
        self.xl=x-self.r*3
        self.y=y
        self.toDelete = 0
    
    def show(self):
        fill(200)
        rect(self.xr,self.y,self.r,self.r)
        rect(self.xl,self.y,self.r,self.r)
         
    def move(self):
        noStroke()
        self.y = self.y - 3
        
    def hits(self,flower):
        d1 = dist(self.xr,self.y,flower.x,flower.y)
        d2 = dist(self.xl,self.y,flower.x,flower.y)
        
        if d1 < self.r + flower.r or d2 < self.r + flower.r  :
            
            return True
        else :
            return False
        
    def evaporate(self):
        self.toDelete = 1
        
        
        