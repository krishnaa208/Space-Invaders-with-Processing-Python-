from ship import Ship
from flowers import Flower
from drops import Drop
from extra import Extra
from gift import Gift
#---------------------------------------------------Initial Set---------------------------------------------------#
global totalGifts


def setup():
    
    size(800,500)
    frameRate(40)
 
    global gift
    global ship
    global gift
    global flowers
    global drops
    global extra
    global total
    global totalGifts
    totalGifts = 0
    total = 10
    gift = []
    extra = []
    flowers = []
    drops = []
    for i in range(0,total):
        flowers.append(Flower(i*80+80,60))
    
    ship = Ship()
    
#---------------------------------------------------Game Over---------------------------------------------------#
def Stop(string):
    noLoop()
    background(51)
    textAlign(CENTER);
    text(string,width/2,height/2);

#---------------------------------------------------Game Rendering---------------------------------------------------#
def draw():
    
    background(51)
    score = total-len(flowers)
    text("Score : "+str(score),width/2,10);
    ship.show()   #Rendering Ship
    ship.move()
    
    
    
    for i in drops:
        i.show()
        i.move()
        for j in flowers:
           if i.hits(j) : 
               print("Hitting")
               i.evaporate()
               j.grow() 
    
    if ship.modified :
        for i in extra:
            i.show()
            i.move()
            for j in flowers:
                if i.hits(j) : 
                    print("Hitting")
                    i.evaporate()
                    j.grow() 
    
    for i in range(len(drops)-1,-1,-1):
        if drops[i].toDelete :
            drops.remove(drops[i])
            print("removed")
    
    for i in range(len(extra)-1,-1,-1):
        if extra[i].toDelete :
            extra.remove(extra[i])
            print("removed")
    
    global totalGifts        
    for i in range(len(flowers)-1,-1,-1):
        if flowers[i].toDelete :
            if random(1) < 0.5 :
                    if totalGifts < 5 :
                        gift.append(Gift(flowers[i].x,flowers[i].y,flowers [i].xdir))
                        totalGifts = totalGifts+1
            flowers.remove(flowers[i])                   
            print("removed")
        
    for i in gift:
        i.show()
        i.update()
        if i.hits(ship) :
            gift.remove(i)
            if i.poison :
                if ship.modified :
                    ship.modified = False
                else :
                    Stop("Game Over")
            else :
                ship.modified = True    
    
    right = False
    for i in flowers:
        if i.y + i.r >= height :
            print("Game Over")
            Stop("Game Over")
            
        i.show()
        i.move() 
        i.explode()
        if i.x > width or i.x < 0:
            right = True
    if right :
        for i in flowers :
            i.shift()
        
    if score == total :
        Stop("Level Completed")

#---------------------------------------------------Key Events---------------------------------------------------#


def keyPressed():
    if keyCode == RIGHT :
        ship.setdir(1);
    elif keyCode == LEFT :
        ship.setdir(-1);
        
    if key == ' ':
        drops.append(Drop(ship.x,height-35))
        if ship.modified :
            extra.append(Extra(ship.x ,height-35))
  

def keyReleased():
    if key != ' ':
        ship.setdir(0)