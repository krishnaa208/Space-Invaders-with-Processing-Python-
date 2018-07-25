class Gift:
    
    def __init__(self,x,y,dir):
        self.x = x -30*dir 
        self.y = y
        self.r = 20
        self.alter = True
        self.poison = False
        if random(2) < 1 :
            self.poison = True
        
    def update(self):
        self.y = self.y+1
        
    def show(self):
        fill(255)
        if self.alter :
            self.alter = False
            rect(self.x,self.y,self.r,self.r)
        else :
            self.alter = True
            if self.poison :
                fill('#ff7070')
            else :
                fill('#90c56b')
            rect(self.x,self.y,self.r+10,self.r+10)
    
    def hits(self,ship):
        d = dist(self.x,self.y,ship.x,ship.y)
        if d < self.r + ship.r   :
            return True
        else :
            return False