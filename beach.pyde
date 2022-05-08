add_library('minim')    # add minim audio library

import random    # import random number generator function 

def setup():    # define function setup to initialize and define program vaiables
    timer = True
    timer2 = None
    n = 0
    x = 0
    xx = -2000
    X = -2000
    sun = 0
    cloud = 0
    moon = 0
    night = 2000
    day_cloud = 0
    cloudnight = 2000
    nightcloud = 0
    rain = []

    
    
    global beach_song,timer,n,x,X, daytime, nighttime, sun,cloud,moon,timer2,xx,night,day_cloud,mex,mey,me,cloudnight,nightcloud,r,g,b
    global rain
    for i in range(1000):    # randomize confetti 
        rain.append(Drop(random.randint(1,2000), random.randint(-500,-50)))
    
    size(2000,1325)
    
    
        
    # loads beach song mp3 audio file from minim library 
    minim=Minim(this)
    beach_song = minim.loadFile("beach_song.mp3")
    
    
    # loads background image files for daytime and nighttime background
    daytime = loadImage("beach.jpg")
    nighttime = loadImage("beach night.jpg")
    me = loadImage("me.jpg")
    
    
    copy(daytime, x, 0, 2000, 1325, 0, 0, 2000, 1325)    #sets image to background
    image(me,1550,50)    #adds picture of my face 

# animation routine for confetti 
class Drop():
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.n = 0
        self.yspeed = random.randint(5,10)
        self._length_= random.randint(10,20)
        
    def fall(self):
        self.y += self.yspeed
        if self.y >= height-200:
            self.y = 1325-19
            self.y = random.randint(-200,-100)
        
    def show(self):
        strokeWeight(6)
        stroke(random.randint(0,256),random.randint(0,256),random.randint(0,256))
        line(self.x,self.y,self.x,self.y+self._length_)
        

    
# create function to manage daytime clouds and sun are in a stationary postion on the screen
def daycloudsfixed():
    fill(255,255,0)
    ellipse(1600,100,200,200)
    image(me,1550+day_cloud,50)
    fill(255,255,255)
    ellipse(1050+day_cloud,200,100,100)
    ellipse(1000+day_cloud,200,100,100)
    ellipse(950+day_cloud,250,100,100)
    ellipse(1000+day_cloud,250,100,100)
    ellipse(1050+day_cloud,250,100,100)
    ellipse(1100+day_cloud,250,100,100)
        
    ellipse(800+day_cloud,300,100,100)
    ellipse(750+day_cloud,300,100,100)
    ellipse(700+day_cloud,350,100,100)
    ellipse(800+day_cloud,350,100,100)
    ellipse(750+day_cloud,350,100,100)
    ellipse(850+day_cloud,350,100,100)
    ellipse(650+day_cloud,350,100,100)
    ellipse(600+day_cloud,350,100,100)
    ellipse(700+day_cloud,300,100,100)
    
    ellipse(1150+day_cloud,400,100,100)
    ellipse(1100+day_cloud,400,100,100)
    ellipse(1050+day_cloud,450,100,100)
    ellipse(1150+day_cloud,450,100,100)
    ellipse(1100+day_cloud,450,100,100)
    ellipse(1200+day_cloud,450,100,100)
  
# create function to manage daytime clouds and sun are moving across the screen
def daycloudsmoving():
    fill(255,255,0)
    ellipse(1600+sun,100,200,200)
    image(me,1550+sun+day_cloud,50)
    fill(255,255,255)
    ellipse(1050+day_cloud+cloud,200,100,100)
    ellipse(1000+day_cloud+cloud,200,100,100)
    ellipse(950+day_cloud+cloud,250,100,100)
    ellipse(1000+day_cloud+cloud,250,100,100)
    ellipse(1050+day_cloud+cloud,250,100,100)
    ellipse(1100+day_cloud+cloud,250,100,100)
        
    ellipse(800+day_cloud+cloud,300,100,100)
    ellipse(750+day_cloud+cloud,300,100,100)
    ellipse(700+day_cloud+cloud,350,100,100)
    ellipse(800+day_cloud+cloud,350,100,100)
    ellipse(750+day_cloud+cloud,350,100,100)
    ellipse(850+day_cloud+cloud,350,100,100)
    ellipse(650+day_cloud+cloud,350,100,100)
    ellipse(600+day_cloud+cloud,350,100,100)
    ellipse(700+day_cloud+cloud,300,100,100)
    
    ellipse(1150+day_cloud+cloud,400,100,100)
    ellipse(1100+day_cloud+cloud,400,100,100)
    ellipse(1050+day_cloud+cloud,450,100,100)
    ellipse(1150+day_cloud+cloud,450,100,100)
    ellipse(1100+day_cloud+cloud,450,100,100)
    ellipse(1200+day_cloud+cloud,450,100,100)
    
# create function to manage nighttime clouds and moon to move across the screen
def nightcloudsmoving():
    fill(220,220,220)
    ellipse(2400+moon,100,200,200)
    image(me,2350+moon,50)
    fill(128,128,128)
    ellipse(1050+night+cloudnight,200,100,100)
    ellipse(1000+night+cloudnight,200,100,100)
    ellipse(950+night+cloudnight,250,100,100)
    ellipse(1000+night+cloudnight,250,100,100)
    ellipse(1050+night+cloudnight,250,100,100)
    ellipse(1100+night+cloudnight,250,100,100)
        
    ellipse(800+night+cloudnight,300,100,100)
    ellipse(750+night+cloudnight,300,100,100)
    ellipse(700+night+cloudnight,350,100,100)
    ellipse(800+night+cloudnight,350,100,100)
    ellipse(750+night+cloudnight,350,100,100)
    ellipse(850+night+cloudnight,350,100,100)
    ellipse(650+night+cloudnight,350,100,100)
    ellipse(600+night+cloudnight,350,100,100)
    ellipse(700+night+cloudnight,300,100,100)
    
    ellipse(1150+night+cloudnight,400,100,100)
    ellipse(1100+night+cloudnight,400,100,100)
    ellipse(1050+night+cloudnight,450,100,100)
    ellipse(1150+night+cloudnight,450,100,100)
    ellipse(1100+night+cloudnight,450,100,100)
    ellipse(1200+night+cloudnight,450,100,100)
    
# create function to manage nighttime clouds and moon in a stationary position on the screen    
def nightcloudsfixed(): 
    fill(220,220,220)
    ellipse(400,100,200,200)
    image(me,350,50) 
    fill(128,128,128)
    ellipse(1050+night,200,100,100)
    ellipse(1000+night,200,100,100)
    ellipse(950+night,250,100,100)
    ellipse(1000+night,250,100,100)
    ellipse(1050+night,250,100,100)
    ellipse(1100+night,250,100,100)
        
    ellipse(800+night,300,100,100)
    ellipse(750+night,300,100,100)
    ellipse(700+night,350,100,100)
    ellipse(800+night,350,100,100)
    ellipse(750+night,350,100,100)
    ellipse(850+night,350,100,100)
    ellipse(650+night,350,100,100)
    ellipse(600+night,350,100,100)
    ellipse(700+night,300,100,100)
    
    ellipse(1150+night,400,100,100)
    ellipse(1100+night,400,100,100)
    ellipse(1050+night,450,100,100)
    ellipse(1150+night,450,100,100)
    ellipse(1100+night,450,100,100)
    ellipse(1200+night,450,100,100)
   
# routine that drops the confetti on the image   
drop = Drop(1000/2,0)    
      
# function that renders the complete image on the screen     
def draw():
    global daytime,timer,n,x,X,sun,moon,cloud,timer2,xx,night,day_cloud,mex,mey,me,reset_cloud,cloudnight,nightcloud
    
    noStroke()
    
    # timer 1 pauses the different images for theirty seconds 
    if timer == True:
        
        for i in range(1,220):
            n += 0.001
            if n >= 150:
                n = 0
                timer = False
                X = -2000
                x = 0
                
    # when timer is true the initial image stops moving and the new image is set to the background
    if timer == True:
        image(daytime,0,0)
    
    # when timer is not active the background moves
    if timer == False:
        # this code moves the daytime and nighttime backgrounds at a set speed
        x += 5
        X += 5
        
        copy(daytime, x, 0, 2000, 1325, 0, 0, 2000, 1325)    #moves daytime image
        
        copy(nighttime, X, 0, 2000, 1325, 0, 0, 2000, 1325)   #moves nighttime image
        
    # when the position of the nighttime image is 0 the timer is set to zero and timer 2 is set to true and the psition of the nighttime image is reset
    if X == 0:
        timer = None
        timer2 = True
        X = -2000
        
    # timer 2 pauses the different images for theirty seconds 
    if timer2 == True:
        for i in range(1,220):
            n += 0.001
            print(n)
            if n >= 50:
                n = 0
                timer2 = False
                
    # when timer 2 is true the initial image stops moving and the new image is set to the background
    if timer2 == True:
        night = 0
        copy(nighttime, X+2000, 0, 2000, 1325, 0, 0, 2000, 1325)    # moves nighttime image 
       
    # when timer 2 is not active the background moves
    if timer2 == False:
        # this code moves the background at a set speed
        xx += 5
        X += 5
        
       
        #moves nighttime image
        copy(nighttime, X+2000, 0, 2000, 1325, 0, 0, 2000, 1325)
       
        #moves daytime image
        copy(daytime, xx, 0, 2000, 1325, 0, 0, 2000, 1325)
        

    # this section checks if clouds, sun, and moon should be moving or stationary and their starting position 
    if xx == 0:
        timer2 = None
        timer = True
        xx = -2000
        X = -2000
        
    if timer == True:
        moon = 0
        daycloudsfixed()
        if nightcloud != 1:
            cloudnight = 0
        if nightcloud == 1:
            cloudnight = 2000
            fill(255,255,0)
            textSize(100)
            text("Summer at the beach!",400,663)
            for j in range(0, len(rain)):
                rain[j].fall()
                rain[j].show()
    if timer == False:
        cloudnight -= 5
        cloud -= 5
        sun -= 5
        moon -= 5
        nightcloudsmoving()
       
        daycloudsmoving()
    if timer2 == True:
        
        nightcloudsfixed()
        cloud = 2000
        cloudnight = 0
        sun = 2000
                
    if timer2 == False:
        cloud -= 5
        cloudnight -= 5
        sun -= 5
        moon -= 5
        nightcloudsmoving()
       
        daycloudsmoving()
        if nightcloud != 1:
            nightcloud += 1
        
  
# function that stops, plays, and repeats the song audio file
def keyPressed():
    global beach_song
    if key == 'p' or key == "P":
        beach_song.play()
    elif key == 's' or key == "S":
        beach_song.pause()
    elif key == 'r' or key == "R":
        beach_song.rewind()
