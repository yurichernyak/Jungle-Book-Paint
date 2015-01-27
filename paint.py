#-------------------------------#
# YURY CHERNYAK'S PAINT PROGRAM #
#-------------------------------#

#IMPORT ALL MODULES
from pygame import *
from math import *
from random import *
from pygame.locals import *
from datetime import datetime



# Tkinter
try:
    # For python 2
    from Tkinter import *
    from tkinter.filedialog import askopenfilename
    from tkinter.filedialog import asksaveasfilename
except:
    # For python 3
    from tkinter import *
    from tkinter.filedialog import askopenfilename
    from tkinter.filedialog import asksaveasfilename



root = Tk() 
root.withdraw()

#---------------------------------
# IMAGES 
background = image.load("images/background.jpg")
background = transform.scale(background,(1000,600))

pencil = image.load("images/pencil.png")
eraser = image.load("images/eraser.png")
spray = image.load("images/spray.png")
bucket = image.load("images/bucket.png")
brush = image.load("images/brush.png")
text = image.load("images/text.png")
rect = image.load("images/rect.png")        #filled rect
rect_empty = image.load("images/empty_rect.jpg")    #empty rect
ellipse = image.load("images/ellipse.png")
ellipse_empty = image.load("images/empty_ellipse.png")
polygon = image.load("images/polygon.png")
undo = image.load("images/undo.png")
redo = image.load("images/redo.png")

#transform.scale to resize images to properly fit
rect = transform.scale(rect,(30,45))
rect_empty = transform.scale(rect_empty,(30,45))
ellipse = transform.scale(ellipse,(30,45))
ellipse_empty = transform.scale(ellipse_empty,(30,45))
polygon = transform.scale(polygon,(48,55))
undo = transform.scale(undo,(40,40))
redo = transform.scale(redo,(40,40))

color_selector = image.load("images/color_selector.jpg")
color_selector = transform.scale(color_selector,(204,100))

stamp1 = image.load("images/stamp1.png")
stamp1 = transform.scale(stamp1,(60,60))
stamp2 = image.load("images/stamp2.png")
stamp2 = transform.scale(stamp2,(60,60))
stamp3 = image.load("images/stamp3.png")
stamp3 = transform.scale(stamp3,(60,60))
stamp4 = image.load("images/stamp4.png")
stamp4 = transform.scale(stamp4,(60,60))
stamp5 = image.load("images/stamp5.png")
stamp5 = transform.scale(stamp5,(60,60))
stamp6 = image.load("images/stamp6.png")
stamp6 = transform.scale(stamp6,(60,60))

delete = image.load("images/delete.png")    #clear screen button
save = image.load("images/save.png")
load = image.load("images/load.png")

music = image.load("images/music.png")
stop = image.load("images/stop.png")

bg1 = image.load("images/bg1.jpg")      #background
bg2 = image.load("images/bg2.jpg")
bg3 = image.load("images/bg3.jpg")

#---------------------------------------
# RECTANGLES

canvas = Rect(110,100,750,390)
pencil_rect = Rect(25,110,48,48)
eraser_rect = Rect(25,173,48,48)
spray_rect = Rect(25,236,48,48)
bucket_rect = Rect(25,299,48,48)
brush_rect = Rect(25,362,48,48)
text_rect = Rect(25,425,48,48)
undo_rect = Rect(90,45,40,40)
redo_rect = Rect(35,45,40,40) 
color_selector_rect = Rect(0,498,204,100)

stamp1_rect = Rect(220,510,50,50)
stamp2_rect = Rect(280,510,50,50)
stamp3_rect = Rect(350,510,50,50)
stamp4_rect = Rect(410,510,50,50)
stamp5_rect = Rect(470,510,50,50)
stamp6_rect = Rect(530,510,50,50)

delete_rect = Rect(900,100,48,48)
save_rect = Rect(900,160,48,48)
load_rect = Rect(900,220,48,48)

music_rect = Rect(900,280,48,48)
stop_rect = Rect(900,340,48,48)

rect_rect = Rect(925,400,30,45)
rect_empty_rect = Rect(890,400,30,45)
ellipse_rect = Rect(925,460,48,55)
ellipse_empty_rect = Rect(890,460,30,45)

polygon_rect = Rect(900,520,48,55)

bg1_rect = Rect(600,515,80,50)
bg2_rect = Rect(685,515,80,50)
bg3_rect = Rect(770,515,80,50)


init()      #Initialize pygame
screen = display.set_mode((1000,600))
display.set_caption("Yuri's Paint Program")
font = font.Font("fonts/font.ttf", 20)

screen.blit(background,(0,0))

#-------------------------------------
# VARIABLES
tool = "pencil"     #main initial tool is pencil
stamp = "stamp1"    #initial stamp
color = (0,0,0)     #initial color is black
size = 10           #initial size
 

#------------------------------------
#TIME & POSITION ON SCREEN

def time():
    #blitting the current date and time from datetime module as white numbers and the coordinte at 800,50
    screen.blit(font.render("%s"%str(datetime.now().strftime('%X %x')),True,(255,255,255)),(800,50))

def coordinates():
    #taking the current mouse position and displaying it out on screen, one for x and one for y-coordinate
    screen.blit(font.render("Position: %s"%str(mx)+",",True,(255,255,255)),(800,30))
    screen.blit(font.render("%s"%str(my),True,(255,255,255)),(940,30))


#---------------------------------------
# BLIT IMAGES
screen.blit(font.render("Jungle Book Paint",True,(255,255,255)),(382,50))       #blitting text on screen
screen.blit(font.render("Yuri Chernyak 2015",True,(255,255,255)),(370,80))
screen.blit(font.render("Copyrigh(c)Yuri2015",True,(255,0,0)),(760,575))

draw.rect(screen,(255,255,255),canvas)      #canvas rectangle
screen.blit(pencil,(25,110))
screen.blit(eraser,(25,173))
screen.blit(spray,(25,236))
screen.blit(bucket,(25,299))
screen.blit(brush,(25,362))
screen.blit(text,(25,425))
screen.blit(undo,(90,45))
screen.blit(redo,(35,45)) 
screen.blit(color_selector,(0,498))

screen.blit(stamp1,(220,510))
screen.blit(stamp2,(280,510))
screen.blit(stamp3,(350,510))
screen.blit(stamp4,(410,510))
screen.blit(stamp5,(470,510))
screen.blit(stamp6,(530,510))

screen.blit(delete,(900,100))
screen.blit(save,(900,160))
screen.blit(load,(900,220))

screen.blit(music,(900,280))
screen.blit(stop,(900,340))
screen.blit(rect,(925,400))
screen.blit(rect_empty,(890,400))
screen.blit(ellipse_empty,(890,460))
screen.blit(ellipse,(925,460))
screen.blit(polygon,(900,520))

screen.blit(transform.scale(bg1,(80,50)),(600,515))     #scaling the background images
screen.blit(transform.scale(bg2,(80,50)),(685,515))
screen.blit(transform.scale(bg3,(80,50)),(770,515))


#---------------------------------
#TOOLS

def pencil_draw():
    #Draw lines with 1 pixel thickness
    if mb[0]==1:
        draw.line(screen, color, (oldx,oldy), (mx,my), 1)

def brush_draw():
    #Draws circle at each point in between distance of old x, old y and mx,my (current position)
    if mb[0]==1:
        distance = sqrt((mx-oldx)**2+(my-oldy)**2)      #distance formula
        if distance == 0:
            distance = 1        #so distance will not be negative or 0
        x,y = oldx,oldy
        sx = (mx-oldx)/distance         #calculates start position of x-coordinate
        sy = (my-oldy)/distance         #calculates start position of y-coordinate
        distance = int(distance)
        for i in range(distance):
            draw.circle(screen,color,(int(x),int(y)),size)      #draws many circles in the distance range
            x += sx         #starting x + old x 
            y += sy
        draw.circle(screen,color,(mx,my),size)

def eraser_draw():
    #Draws circle at each point in between distance of old x, old y and mx,my
    #calculations are done for no lag/space in between circles
    if mb[0]==1:
        distance = sqrt((mx-oldx)**2+(my-oldy)**2)
        if distance == 0:
            distance = 1
        x,y = oldx,oldy
        sx = (mx-oldx)/distance
        sy = (my-oldy)/distance
        distance = int(distance)
        for i in range(distance):
            draw.circle(screen,(255,255,255),(int(x),int(y)),size)
            x += sx
            y += sy
        draw.circle(screen,(255,255,255),(mx,my),size)

def spray_draw():
    #Spray effect
    if mb[0]==1:
        for i in range(size * 10):           # For speed and more random dots
            x = randint(size*-3,size*3)      #random x coordinates, this will depend how close it will be
            y = randint(size*-3,size*3)      #random y coordinates
            #Check distance for circle border
            if hypot(x,y) <= size:          
                screen.set_at((mx+x,my+y),(color))      #sets screen to the current position +random int

                

def rectangle_empty(position,end):      
    if mb[0] == 1:
        screen.blit(copy,(0,0))         #blitts screen
        #draws rectangle with four points... start position at 0, start position at 1, and then the absolute value of other two points
        draw.rect(screen,(color),(min(position[0],end[0]),min(position[1],end[1]),abs(position[0]-end[0]),abs(position[1]-end[1])),size)

def rectangle_full(position,end):       #a start position and end position
    if mb[0] == 1:
        screen.blit(copy,(0,0))
        draw.rect(screen,(color),(min(position[0],end[0]),min(position[1],end[1]),abs(position[0]-end[0]),abs(position[1]-end[1])))

def ellipse_empty(position,end):        #same as rectangle
    if mb[0] == 1:
        screen.blit(copy,(0,0))
        try:
            #size causes unfilled
            draw.ellipse(screen,(color),(min(position[0],end[0]),min(position[1],end[1]),abs(position[0]-end[0]),abs(position[1]-end[1])),size)
        except:
            #did not always work
            print("")

def ellipse_full(position,end):
    if mb[0] == 1:
        screen.blit(copy,(0,0))
        try:
            draw.ellipse(screen,(color),(min(position[0],end[0]),min(position[1],end[1]),abs(position[0]-end[0]),abs(position[1]-end[1])))
        except:
            print("")



def bucket(x,y,oldColor,newColor):      #change points and change color
    points = [(x, y)]       #starting points are in a list
    while len(points) > 0:
        x,y = points.pop()          #Gets the last coordinates and deletes them from the points list
        if screen.get_at((x,y)) != oldColor:
            continue
        screen.set_at((x,y),newColor)
        #This adds the points to the list, all around the first point
        points.append((x + 1, y))        #up,down, left and right around one point
        points.append((x - 1, y))  
        points.append((x, y + 1))
        points.append((x, y - 1))


poly = []       #points go into a list
def polygon():
    global poly
    if mb[0]==1 and canvas.collidepoint(mx,my):
        draw.circle(screen,(0,0,0),(mx,my),4)       #points are circle, which are appended to a list
        poly.append((mx,my))
        
    if mb[2]==1:
        if len(poly)>2:
            draw.polygon(screen,color,poly,size)    #if right click, fills and connects all points
        poly = []       #makes the poly list empty again


def text_draw():
    text = input("Enter your text: ")       #in shell
    if mb[0]==1:
        #wherever the mouse clicks on screen, text from shell should appear
        screen.blit(font.render(str(text),True,(255,255,255)),(mx,my))      

# Lists to hold screen copies
undos = [screen.subsurface(canvas).copy()]      #copy of the canvas
redos = []



running = True
while running:
    #blitting this section of the background for time, coordinates and FPS to be constantly renewed
    screen.blit(background,(800,-500))      
    draw.rect(screen,color,(0,0,1000,600),20)       #shows the color selected 
    time()      #calls time function
    coordinates()       #calls coordinates function
    mouse_click = False         # checking for the mouse click and not just holding
    mx,my = mouse.get_pos()         #current mouse position
    mb = mouse.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            copy = screen.copy()
            mouse_click = True          #checks if mouse is clicked not held down
            position = mx,my        #defining position in rectangle and ellipse functions
            # change size
            if e.button == 4:
                size += 1
            if e.button == 5:
                if size > 1:        #so the size will never be negative or 0
                    size -= 1
            

        if e.type == MOUSEBUTTONDOWN:
            copy = screen.copy()
            if canvas.collidepoint((mx,my)):
                canvaspic = screen.subsurface(canvas).copy()
                undos.append(canvaspic)      #add a copy of the canvas to the undos list whenever the mouse is lifted up

        if e.type == MOUSEBUTTONUP:
            if mb[0]==1 and undo_rect.collidepoint((mx,my)):
                if len(undos) > 1:
                    screen.blit(undos[-2],(110,100))        #blit second last screen
                    redos.append(undos.pop())       #append to redo and delete from undo
            if mb[0]==1 and redo_rect.collidepoint((mx,my)):
                if len(redos)>0:
                    screen.blit(redos[-1],(110,100))    #blit last to screen
                    undos.append(redos.pop())       #append to undo and delete from redo



    #rectangle collidepoints, collision detection
    
    if color_selector_rect.collidepoint(mx,my):
        color = screen.get_at((mx,my))          #for custom colors
    
    
    if pencil_rect.collidepoint(mx,my) and mouse_click:
        tool = "pencil"
    elif eraser_rect.collidepoint(mx,my) and mouse_click:
        tool = "eraser"
    elif spray_rect.collidepoint(mx,my) and mouse_click:
        tool = "spray"
    elif bucket_rect.collidepoint(mx,my) and mouse_click:
        tool = "bucket"
    elif brush_rect.collidepoint(mx,my) and mouse_click:
        tool = "brush"
    elif text_rect.collidepoint(mx,my) and mouse_click:
        tool = "text"
    elif rect_rect.collidepoint(mx,my) and mouse_click:
        tool = "rectangle full"
    elif rect_empty_rect.collidepoint(mx,my) and mouse_click:
        tool = "rectangle empty"
    elif ellipse_rect.collidepoint(mx,my) and mouse_click:
        tool = "ellipse full"
    elif ellipse_empty_rect.collidepoint(mx,my) and mouse_click:
        tool = "ellipse empty"
    elif polygon_rect.collidepoint(mx,my) and mouse_click:
        tool = "polygon"
        
    elif stamp1_rect.collidepoint(mx,my) and mouse_click:
        tool = "stamp"
        stamp = "stamp1"
    elif stamp2_rect.collidepoint(mx,my) and mouse_click:
        tool = "stamp"
        stamp = "stamp2"
    elif stamp3_rect.collidepoint(mx,my) and mouse_click:
        tool = "stamp"
        stamp = "stamp3"
    elif stamp4_rect.collidepoint(mx,my) and mouse_click:
        tool = "stamp"
        stamp = "stamp4"
    elif stamp5_rect.collidepoint(mx,my) and mouse_click:
        tool = "stamp"
        stamp = "stamp5"
    elif stamp6_rect.collidepoint(mx,my) and mouse_click:
        tool = "stamp"
        stamp = "stamp6"

    screen.set_clip(canvas)
    
    #whichever tool is selected, calls on function       
    if tool == "pencil":
        pencil_draw()
    elif tool == "eraser":
        eraser_draw()
    elif tool == "spray":
        spray_draw()
    elif tool == "bucket":
        if mb[0] == 1:
            bucket(mx,my,screen.get_at((mx,my)),color)      #gets position curreent when clicked
    elif tool == "brush":
        brush_draw()
    elif tool == "text":
        text_draw()
    elif tool == "rectangle full":
        rectangle_full(position,(mx,my))    #mx,my = current position
    elif tool == "rectangle empty":
        rectangle_empty(position,(mx,my))
    elif tool == "ellipse full":
        ellipse_full(position,(mx,my))
    elif tool == "ellipse empty":
        ellipse_empty(position,(mx,my))
    elif tool == "polygon":
        polygon()
    
    elif tool == "stamp":
       
        if mb[0] == 1:
            if stamp == "stamp1":
                screen.blit(copy,(0,0))
                screen.blit(stamp1,(mx - 30,my - 30))       #centered stamps
            if stamp == "stamp2":
                screen.blit(copy,(0,0))
                screen.blit(stamp2,(mx - 30,my - 30))
            if stamp == "stamp3":
                screen.blit(copy,(0,0))
                screen.blit(stamp3,(mx - 30,my - 30))
            if stamp == "stamp4":
                screen.blit(copy,(0,0))
                screen.blit(stamp4,(mx - 30,my - 30))
            if stamp == "stamp5":
                screen.blit(copy,(0,0))
                screen.blit(stamp5,(mx - 30,my - 30))
            if stamp == "stamp6":
                screen.blit(copy,(0,0))
                screen.blit(stamp6, (mx - 30,my - 30))

    screen.set_clip(None)

    if delete_rect.collidepoint(mx,my) and mouse_click:
        draw.rect(screen,(255,255,255),canvas)          #Draw new canvas, clear button
    if save_rect.collidepoint(mx,my) and mouse_click:
        fileName = asksaveasfilename(parent=root,title="Save the image as...")            #Tkinter save
        image.save(screen.subsurface(canvas).copy(),fileName)
    if load_rect.collidepoint(mx,my) and mouse_click:
        fileName = askopenfilename(parent=root,title="Open Image:")             #Tkinter load
        screen.blit(image.load(fileName),(0,0))
    
    if music_rect.collidepoint(mx,my) and mouse_click:
        songs = ["song.mp3","song2.mp3","song3.mp3"]        #random song from list of 3
        mixer.music.load("music/" + choice(songs))
        mixer.music.play()
    if stop_rect.collidepoint(mx,my) and mouse_click:
        mixer.music.stop() # Stop music

    if bg1_rect.collidepoint(mx,my) and mouse_click:                #select background and fill canvas with them
        screen.blit(transform.scale(bg1,(750,390)),(110,100))
    if bg2_rect.collidepoint(mx,my) and mouse_click:
        screen.blit(transform.scale(bg2,(750,390)),(110,100))
    if bg3_rect.collidepoint(mx,my) and mouse_click:
        screen.blit(transform.scale(bg3,(750,390)),(110,100))
       
    oldx,oldy = mx,my       #set old mouse positions to new to get starting and ending position of a trail

    display.flip()
del font            #delete font at the end
quit()

#---------#
##THE END##
#---------#


