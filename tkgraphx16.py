#this is for the module
import tkinter as tk
from tkinter import *
import multiprocessing

x_len=0
y_len=0
screen_x=0
screen_y=0
pixel_x=0
pixel_y=0
framec=0

pixels=[]
sprites=[]
backgrounds=[]
list1=[]
list2=[]
list3=[]

class Pixel():
 def __init__(self, window_name, color, pixel_name):
  self.window_name=window_name
  self.color=color
  self.pixel_name=pixel_name
 def stamp(self):
  tk.canvas.itemconfigure(self.pixel_name, fill=self.color) 
 
class Sprite():
 def __init__(self, x, y, size, sprite):
  self.x=x
  self.y=y
  self.size=size
  self.sprite=sprite
  sprites.append(self)
 def render(self):
  sprite_x=round(self.x)
  sprite_y=round(self.y)
  current_x=sprite_x
  current_y=sprite_y
  for i in range(len(self.sprite)):
   if sprite_x>pixel_x-1 or sprite_y>pixel_y-1:
    break
   if self.sprite[i]=='n':
    current_x=sprite_x
    current_y+=self.size
    continue
   if self.sprite[i]==0:
    current_x+=self.size
    continue
   if current_x>pixel_x-1 or current_x<0 or current_y>pixel_y-1 or current_y<0:
    current_x+=1
    continue
   for q in range(self.size):
    for b in range(self.size-1):
     if current_x<pixel_x-1 and current_x>0 and current_y<pixel_y-1 and current_y>0:
      pixels[current_y*pixel_x+current_x].color=self.sprite[i]
      pixels[current_y*pixel_x+current_x].stamp()
     current_x+=1
    if current_x<pixel_x-1 and current_x>0 and current_y<pixel_y-1 and current_y>0:
     pixels[current_y*pixel_x+current_x].color=self.sprite[i]
     pixels[current_y*pixel_x+current_x].stamp()
    current_y+=1
    current_x-=self.size-1
   current_y-=self.size
   current_x+=self.size
 def unrender(self):
  sprite_x=round(self.x)
  sprite_y=round(self.y)
  current_x=sprite_x
  current_y=sprite_y
  for i in range(len(self.sprite)):
   if sprite_x>pixel_x-1 or sprite_y>pixel_y-1:
    break
   if self.sprite[i]=='n':
    current_x=sprite_x
    current_y+=self.size
    continue
   if self.sprite[i]==0:
    current_x+=self.size
    continue
   if current_x>pixel_x-1 or current_x<0 or current_y>pixel_y-1 or current_y<0:
    current_x+=1
    continue
   for q in range(self.size):
    for b in range(self.size-1):
     if current_x<pixel_x-1 and current_x>0 and current_y<pixel_y-1 and current_y>0:
      try:
       pixels[current_y*pixel_x+current_x].color=backgrounds[0].sprite[current_x-backgrounds[0].x+((current_y-backgrounds[0].y)*backgrounds[0].sprite0)]
       pixels[current_y*pixel_x+current_x].stamp()
      except:
       pixels[current_y*pixel_x+current_x].color='black'
       pixels[current_y*pixel_x+current_x].stamp()
     current_x+=1
    if current_x<pixel_x-1 and current_x>0 and current_y<pixel_y-1 and current_y>0:
     try:
      pixels[current_y*pixel_x+current_x].color=backgrounds[0].sprite[current_x-backgrounds[0].x+((current_y-backgrounds[0].y)*backgrounds[0].sprite0)]
      pixels[current_y*pixel_x+current_x].stamp()
     except:
      pixels[current_y*pixel_x+current_x].color='black'
      pixels[current_y*pixel_x+current_x].stamp()
    current_y+=1
    current_x-=self.size-1
   current_y-=self.size
   current_x+=self.size

class Background():
 def __init__(self, x, y, sprite0, sprite):
  self.x=x
  self.y=y
  self.sprite0=sprite0
  self.sprite=sprite
 def render(self):
  sprite_x=round(self.x)
  sprite_y=round(self.y)
  current_x=sprite_x
  current_y=sprite_y
  for q in range(len(self.sprite)):
   if sprite_x>pixel_x-1 or current_y>pixel_y-1:
    break
   if current_x-sprite_x>self.sprite0-1:
    current_x=sprite_x
    current_y+=1
    try:
     pixels[current_y*pixel_x+current_x].color=backgrounds[0].sprite[current_x-backgrounds[0].x+((current_y-backgrounds[0].y)*backgrounds[0].sprite0)]
     pixels[current_y*pixel_x+current_x].stamp()
    except:
     pixels[current_y*pixel_x+current_x].color='black'
     pixels[current_y*pixel_x+current_x].stamp()
    current_x+=1
    continue
   if current_x>pixel_x-1 or current_y<0:
    current_x=sprite_x
    current_y+=1
   if current_x<0:
    current_x=0
    continue
   try:
     pixels[current_y*pixel_x+current_x].color=backgrounds[0].sprite[current_x-backgrounds[0].x+((current_y-backgrounds[0].y)*backgrounds[0].sprite0)]
     pixels[current_y*pixel_x+current_x].stamp()
   except:
     pixels[current_y*pixel_x+current_x].color='black'
     pixels[current_y*pixel_x+current_x].stamp()
   current_x+=1

def qdee(window_name, scrn_x, scrn_y, pixl_x, pixl_y):
 global x_len
 global y_len
 global pixel_x
 global pixel_y
 global screen_x
 global screen_y
 screen_x=scrn_x
 screen_y=scrn_y
 pixel_x=pixl_x
 pixel_y=pixl_y
 x_len=screen_x/pixel_x
 y_len=screen_y/pixel_y
 pixels.clear()
 tk.canvas=Canvas(window_name, height=screen_y, width=screen_x)
 tk.canvas.pack(fill=BOTH)
 for i in range(pixel_y):
  for q in range(pixel_x):
   pixel_name=str(q)+'-'+str(i)
   pixel_name=tk.canvas.create_rectangle(q*x_len, screen_y-(i*y_len), q*x_len+x_len, screen_y-(i*y_len-y_len), fill = 'black', width = 0) 
   pixel_name=Pixel(window_name, '#000000', pixel_name)
   pixel_name.stamp()
   pixels.append(pixel_name)
 background=Background(0,0,pixel_x, '#000000')
 backgrounds.clear()
 backgrounds.append(background)

def adsprite(sprite_name, x, y, sprite):
 sprite_name=Sprite(x, y, sprite)
 sprites.append(sprite_name)
 
def adbackground(x, y, sprite0, sprite):
 for i in range(len(backgrounds)):
  backgrounds[0].x=x
  backgrounds[0].y=y
  backgrounds[0].sprite0=sprite0
  backgrounds[0].sprite=sprite
  break

def render_scene():
 for whocares in range(len(backgrounds)):
  backgrounds[0].render()
  break
 for i in range(len(sprites)):
  sprites[i-1].render()

def destroy():
 pixels.clear()

def wait(time, function):
 global list
 list1.append(time)
 list2.append(function)
 list3.append(framec)
 

def frame_count():
 global framec
 framec+=1
 for i in range(len(list1)):
  if framec==list3[i-1]+list1[i-1]:
    list2[i-1]()
 

#sprite.render()
#sprite.unrender()
#background.render()
#pixel.render()
  
#ok done

window=tk.Tk()
window.title('Tk Grafx 16')
window.configure(bg='#FFFFFF')
window.geometry("768x720+0+0")

def thing1():
 ship.unrender()
 ship.y+=1
 ship.render()
 wait(1800, thing2)
def thing2():
 ship.unrender()
 ship.y-=1
 ship.render()
 wait(1800, thing1)

def girth():
 mario.unrender()
 mario.size+=1
 mario.render()
 wait(10, girth)

def left(event):
 kyrbo.unrender()
 kyrbo.x-=2
 kyrbo.render()
def right(event):
 kyrbo.unrender()
 kyrbo.x+=2
 kyrbo.render()
def up(event):
 kyrbo.unrender()
 kyrbo.y+=2
 kyrbo.render()
def down(event):
 kyrbo.unrender()
 kyrbo.y-=2
 kyrbo.render()

qdee(window, 768, 720, 256, 240)
adbackground(50,100,13, (0, 0, 0, 0, 'white', 'white', 'white', 'white', 'blue', 'blue', 0, 0, 0, 0, 0, 0, 'white', 'brown', 'brown', 'brown', 'brown', 'blue', 'blue', 'blue', 0, 0, 0, 0, 'white', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown', 'blue', 'brown', 'blue', 0, 'white', 'white', 'white', 'white', 'brown', 'white', 'blue', 'brown', 'white', 'white', 'brown', 'blue', 'blue', 0, 0, 0, 0, 0, 'brown', 'brown', 'blue', 'brown', 'brown', 'blue', 0, 0, 0, 0, 0, 0, 0, 'blue', 'blue', 'blue', 'brown', 'blue', 'blue', 0, 0, 0, 0, 0, 0, 'blue', 'red', 'blue', 'red', 'brown', 'white', 'blue', 0, 0, 0, 0, 0, 'blue', 'red', 'white', 'red', 'red', 'blue', 'blue', 'blue', 0, 0, 0, 0, 0, 0, 'blue', 'white', 0, 'white', 'red', 'blue', 0, 0, 0, 0, 0, 0, 0, 'blue', 0, 0, 'white', 0, 'blue', 0, 0, 0, 0, 0, 0, 0, 'white', 'white', 0, 0, 0, 'blue', 'blue', 0, 0, 0, 0, 0, 'blue', 'red', 'white', 0, 0, 'white', 'blue', 'blue', 0, 0, 0, 0, 0, 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'blue', 'white', 0, 0, 0, 0, 0, 'white', 'white', 'white', 'blue', 'blue', 'blue', 'blue', 'white', 'white', 0, 0, 0, 0, 0, 'white', 0, 'white', 0, 0, 'white', 0, 'white', 0, 0, 0, 0, 0, 0, 'white', 0, 0, 0, 0, 'white', 0, 0))
adbackground(50,100,16, (0, 0, 0, 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 0, 0, 0, 0, 0, 0, 'white', 'white', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'white', 'white', 0, 0, 0, 0, 'white', 'gray', 'gray', 'gray', 'dark grey', 'dark grey', 'dark grey', 'dark grey', 'dark grey', 'dark grey', 'dark grey', 'dark grey', 'white', 0, 0, 0, 'white', 'gray', 'dark grey', 'dark grey', 'white', 'white', 'dark grey', 'white', 'white', 'dark grey', 'dark grey', 'dark grey', 'dark grey', 'white', 0, 'white', 'gray', 'gray', 'dark grey', 'white', 'light grey', 'light grey', 'white', 'light grey', 'light grey', 'white', 'light grey', 'dark grey', 'dark grey', 'white', 0, 'white', 'gray', 'gray', 'dark grey', 'white', 'light grey', 'light grey', 'light grey', 'light grey', 'light grey', 'white', 'light grey', 'dark grey', 'dark grey', 'dark grey', 'white', 'white', 'gray', 'gray', 'dark grey', 'light grey', 'light grey', 'light grey', 'light grey', 'light grey', 'light grey', 'light grey', 'light grey', 'white', 'dark grey', 'white', 0, 'white', 'gray', 'white', 'dark grey', 'dark grey', 'white', 'light grey', 'light grey', 'light grey', 'white', 'light grey', 'light grey', 'white', 'dark grey', 'white', 0, 0, 'white', 'white', 'dark grey', 'dark grey', 'dark grey', 'white', 'light grey', 'light grey', 'dark grey', 'white', 'light grey', 'white', 'white', 0, 0, 0, 0, 0, 'white', 'dark grey', 'dark grey', 'dark grey', 'dark grey', 'dark grey', 'dark grey', 'dark grey', 'dark grey', 'dark grey', 'white', 0, 0, 0, 0, 0, 0, 'white', 'dark grey', 'dark grey', 'white', 'white', 'white', 'dark grey', 'dark grey', 'white', 0, 0, 0, 0, 0, 0, 0, 0, 'white', 'white', 0, 0, 0, 'white', 'white', 0, 0, 0, 0))
red='#FF4D21'
black='#FFFFFF'
beige='#F5D8C1'
mario=Sprite(0, 0, 1, (0,'#FFFFFF', '#FFFFFF','n','#FFFFFF','#FF4D21','#FF4D21','#FFFFFF','#FFFFFF',0,0,0,0,0,0,0,'#FFFFFF','#FFFFFF','#FFFFFF','n','#FFFFFF','#FF4D21','#FF4D21','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF',0,0,0,'#FFFFFF','#FF4D21','#FF4D21','#FFFFFF','#FFFFFF','n','#FFFFFF','#FF4D21','#FF4D21','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FF4D21','#FF4D21','#FF4D21','#FFFFFF','n','#FFFFFF','#FF4D21','#FF4D21','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FF4D21','#FF4D21','#FF4D21','n','#FFFFFF','#FFFFFF','#FF4D21','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FF4D21','#FF4D21','#FF4D21','#FFFFFF','n',0,'#FFFFFF','#FF4D21','#FF4D21','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FF4D21','#FF4D21','#FF4D21','#FFFFFF','n',0,0,'#FFFFFF','#FFFFFF','#F5D8C1','#F5D8C1','#FFFFFF','#FFFFFF','#F5D8C1','#F5D8C1','#FFFFFF','#FFFFFF','#FF4D21','#FF4D21','#FFFFFF','n',0,'#FFFFFF','#FFFFFF','#F5D8C1','#F5D8C1','#F5D8C1','#F5D8C1','#F5D8C1','#FFFFFF','#F5D8C1','#F5D8C1','#FFFFFF','#FFFFFF','#F5D8C1','#F5D8C1','#FFFFFF','n','#FFFFFF','#FF4D21','#FFFFFF','#F5D8C1','#F5D8C1','#F5D8C1','#F5D8C1','#F5D8C1','#FFFFFF','#FFFFFF','#FFFFFF','#FF4D21','#FF4D21','#FFFFFF','#FFFFFF','n','#FFFFFF','#FF4D21','#FF4D21','#FFFFFF','#F5D8C1','#F5D8C1','#F5D8C1','#FFFFFF','#FFFFFF','#FFFFFF','#FF4D21','#FF4D21','#FFFFFF','#F5D8C1','#FFFFFF','n','#FFFFFF','#FF4D21','#FF4D21','#FF4D21','#FFFFFF','#FFFFFF','#FFFFFF','#FF4D21','#FFFFFF','#FF4D21','#FF4D21','#FF4D21','#FFFFFF','#FFFFFF','#F5D8C1','#FFFFFF','n',0,'#FFFFFF','#FF4D21','#FF4D21','#FF4D21','#FF4D21','#FF4D21','#FFFFFF','#FFFFFF','#FF4D21','#FF4D21','#FFFFFF','#FFFFFF','#F5D8C1','#F5D8C1','#FFFFFF','n',0,0,'#FFFFFF','#FF4D21','#FF4D21','#FF4D21','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF',0,'#FFFFFF','#FFFFFF','n',0,0,0,'#FFFFFF','#FFFFFF','#FFFFFF','#F5D8C1','#F5D8C1','#F5D8C1','#F5D8C1','#F5D8C1','#FFFFFF','n',0,0,'#FFFFFF','#FFFFFF','#F5D8C1','#F5D8C1','#F5D8C1','#F5D8C1','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','n',0,'#FFFFFF','#F5D8C1','#F5D8C1','#F5D8C1','#F5D8C1','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#F5D8C1','#F5D8C1','#FFFFFF','#FFFFFF','#FFFFFF','n','#FFFFFF','#F5D8C1','#F5D8C1','#F5D8C1','#FFFFFF','#F5D8C1','#F5D8C1','#FFFFFF','#F5D8C1','#F5D8C1','#F5D8C1','#F5D8C1','#F5D8C1','#FFFFFF','n','#FFFFFF','#F5D8C1','#F5D8C1','#FFFFFF','#FFFFFF','#FFFFFF','#F5D8C1','#F5D8C1','#F5D8C1','#F5D8C1','#F5D8C1','#F5D8C1','#F5D8C1','#FFFFFF','n',0,'#FFFFFF','#F5D8C1','#FFFFFF','#FFFFFF','#F5D8C1','#F5D8C1','#F5D8C1','#FFFFFF','#F5D8C1','#FFFFFF','#F5D8C1','#FFFFFF','n',0,'#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#F5D8C1','#F5D8C1','#F5D8C1','#FFFFFF','#F5D8C1','#FFFFFF','#F5D8C1','#FFFFFF','n',0,0))
pot=Sprite(30,30, 1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'red', 'red', 0, 0, 'red', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'red', 'red', 'red', 'red', 'red', 0, 'red', 'red', 0, 'red', 'red', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'red', 0, 'red', 'red', 'red', 0, 0, 'red', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'red', 0, 'red', 0, 'red', 'red', 'red', 0, 'n', 0, 0, 0, 0, 0, 0, 0, 0, 'red', 0, 'red', 0, 'red', 0, 'red', 0, 0, 'red', 'red', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'red', 0, 0, 0, 0, 0, 0, 'red', 'n', 'red', 0, 0, 0, 'red', 0, 0, 'red', 0, 0, 0, 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 'white', 'white', 'white', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'white', 'white', 0, 0, 'red', 'n', 0, 0, 0, 0, 0, 0, 'white', 'white', 0, 0, 0, 0, 0, 0, 0, 'yellow', 0, 'red', 'red', 0, 0, 'red', 'white', 'n', 0, 0, 0, 'red', 0, 'white', 0, 'red', 0, 0, 0, 'yellow', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'red', 'white', 'n', 0, 0, 0, 'red', 'white', 0, 0, 0, 'yellow', 0, 0, 0, 'yellow', 0, 'yellow', 'yellow', 0, 0, 0, 0, 0, 0, 0, 'white', 0, 0, 0, 'red', 'n', 0, 0, 0, 0, 'white', 0, 0, 0, 0, 0, 'yellow', 'white', 'white', 'white', 'white', 'yellow', 'yellow', 0, 'yellow', 0, 'yellow', 0, 0, 'white', 0, 0, 'red', 'n', 0, 0, 0, 'white', 0, 0, 0, 0, 'yellow', 'yellow', 'white', 'white', 'white', 0, 'white', 'white', 'white', 'yellow', 0, 0, 0, 0, 0, 0, 'white', 'n', 0, 0, 'white', 'white', 0, 'white', 'white', 'yellow', 'white', 'white', 0, 0, 0, 0, 0, 0, 0, 'white', 'white', 'white', 0, 0, 0, 0, 'white', 'n', 0, 'white', 'white', 'white', 'white', 'white', 'yellow', 'white', 0, 0, 0, 0, 0, 0, 'white', 0, 0, 0, 0, 'white', 'yellow', 'yellow', 0, 0, 'white', 'n', 0, 0, 0, 0, 0, 0, 0, 'yellow', 'white', 'white', 0, 0, 0, 'white', 'white', 'white', 0, 0, 0, 0, 'white', 'white', 'white', 0, 0, 'white', 'n', 0, 0, 0, 0, 0, 0, 'yellow', 0, 'yellow', 'yellow', 'white', 'white', 'white', 0, 'white', 0, 0, 'white', 0, 0, 'white', 'yellow', 0, 'white', 'white', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'yellow', 'yellow', 'yellow', 'yellow', 'white', 'yellow', 'white', 'white', 'white', 'white', 'white', 'yellow', 'yellow', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'yellow', 'yellow', 'white', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 0, 'yellow', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'yellow', 0, 0, 0, 0, 'white', 0, 0, 0, 'yellow', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'yellow', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'yellow'))
kyrbo=Sprite(60,50, 1, (0, 'red', 'red', 0, 0, 0, 0, 0, 0, 'red', 'red', 'n', 'red', 0, 0, 'red', 0, 0, 0, 0, 'red', 0, 0, 'red', 'n', 'red', 0, 0, 'red', 'red', 0, 0, 'red', 'red', 0, 0, 'red', 'n', 0, 'red', 'pink', 'pink', 'pink', 'pink', 'pink', 'pink', 'pink', 'pink', 'red', 'n', 0, 'pink', 0, 0, 0, 0, 0, 0, 0, 0, 'pink', 'n', 'pink', 0, 0, 0, 'white', 'white', 'white', 'white', 0, 0, 0, 'pink', 'n', 'pink', 0, 0, 'white', 0, 0, 0, 0, 'white', 0, 0, 'pink', 'n', 0, 'pink', 0, 0, 'white', 0, 0, 'white', 0, 0, 'pink', 'n', 0, 'pink', 0, 0, 0, 0, 0, 0, 0, 0, 'pink', 'n', 0, 0, 'pink', 0, 'white', 0, 0, 'white', 0, 'pink', 'n', 0, 0, 'pink', 0, 'white', 0, 0, 'white', 0, 'pink', 'n', 0, 0, 'pink', 0, 'white', 0, 0, 'white', 0, 'pink', 'n', 0, 0, 0, 'pink', 0, 0, 0, 0, 'pink', 'n', 0, 0, 0, 0, 'pink', 'pink', 0, 'pink', 'n', 0, 0, 0, 0, 'black', 0, 'black', 'n', 0, 0, 0, 'black', 0, 0, 'black', 'n', 0, 0, 0, 'black', 0, 0, 'black', 'n', 0, 0, 0, 0, 'black', 'black'))
ship=Sprite(100,60, 1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'blue', 0, 0, 0, 0, 0, 'grey', 'grey', 0, 'grey', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'grey', 0, 0, 0, 0, 'grey', 'grey', 0, 0, 0, 'grey', 'grey', 'grey', 'n', 0, 0, 0, 0, 0, 0, 'grey', 0, 'grey', 0, 'grey', 0, 0, 0, 'grey', 'grey', 0, 'grey', 'grey', 0, 0, 'grey', 'grey', 'blue', 'n', 0, 0, 0, 0, 0, 0, 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'blue', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'n', 0, 0, 0, 0, 0, 'grey', 'grey', 'grey', 'grey', 'blue', 'blue', 'blue', 'grey', 'grey', 'blue', 'blue', 'blue', 'grey', 'blue', 'blue', 'grey', 'blue', 'blue', 'blue', 'grey', 'grey', 'n', 0, 0, 0, 'grey', 0, 'grey', 'grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'grey', 'grey', 'n', 0, 'grey', 0, 'grey', 'grey', 'grey', 'blue', 'blue', 'dark blue', 'dark blue', 'dark blue', 'dark blue', 'dark blue', 'dark blue', 'dark blue', 'dark blue', 'dark blue', 'dark blue', 'dark blue', 'dark blue', 'dark blue', 'dark blue', 'blue', 'blue', 'blue', 'grey', 'grey', 0, 0, 'blue', 'n', 0, 'grey', 'grey', 'grey', 'grey', 'blue', 'blue', 'dark blue', 'dark blue', 'white', 'white', 'dark blue', 'dark blue', 'dark blue', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'dark blue', 'dark blue', 'dark blue', 'blue', 'blue', 'grey', 'grey', 'grey', 0, 'grey', 'n', 'grey', 'grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'dark blue', 'white', 'black', 'black', 'white', 'white', 'white', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'white', 'white', 'dark blue', 'dark blue', 'blue', 'blue', 'blue', 'grey', 'blue', 'grey', 'grey', 'n', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'dark blue', 'white', 0, 'white', 'white', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'white', 'white', 'dark blue', 'blue', 'blue', 'blue', 'grey', 'grey', 'grey', 'n', 0, 0, 0, 0, 0, 'blue', 'white', 'black', 'white', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'black', 'black', 'black', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'white', 'dark blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'grey', 'grey', 'grey', 'n', 0, 0, 0, 0, 0, 'white', 'black', 'white', 'white', 'gray', 'gray', 'gray', 'gray', 'gray', 'black', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'black', 'black', 'gray', 'gray', 'gray', 'white', 'dark blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'n', 0, 0, 0, 0, 'white', 'black', 'black', 'white', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'black', 'gray', 'gray', 'white', 'dark blue', 'blue', 'blue', 'n', 0, 0, 0, 'white', 'black', 'black', 'white', 'white', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'black', 'white', 'n', 0, 0, 'white', 'black', 'white', 'white', 'white', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'white', 'white', 'white', 'white', 'gray', 'gray', 'gray', 'gray', 'gray', 'black', 'white', 'n', 0, 0, 0, 'white', 'white', 'gray', 'gray', 'gray', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'dark red', 'dark red', 'dark red', 'dark red', 'white', 'white', 'gray', 'gray', 'gray', 'black', 'white', 'n', 0, 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'dark red', 'dark red', 'dark red', 'white', 'white', 'dark red', 'dark red', 'dark red', 'dark red', 'dark red', 'dark red', 'dark red', 'dark red', 'dark red', 'dark red', 'white', 'gray', 'gray', 'black', 'black', 'white', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 'white', 'white', 'white', 'dark red', 'dark red', 'white', 'white', 'dark red', 'dark red', 'dark red', 'dark red', 'dark red', 'white', 'white', 'white', 'white', 'gray', 'gray', 'black', 'white', 'white', 'white', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'white', 'white', 'dark red', 'white', 'white', 'white', 'white', 'white', 'white', 'dark red', 'dark red', 'white', 'white', 'white', 'white', 'white', 'white', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'white', 'white', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'white', 'white', 0, 0, 'white', 'white', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'white', 'white', 'white', 0, 'white', 'white', 'white', 'white', 'white', 'white', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'white', 0, 0, 'white', 0, 'white', 'white', 'white', 'white', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'white', 'white', 'white', 0, 0, 'white', 'white', 'white', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'white', 0, 0, 'white', 0, 'white', 'white', 'white', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'n', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'white', 'white', 'white', 'white', 'white', 'white'))
render_scene()
window.bind('a', left)
window.bind('d', right)
window.bind('w', up)
window.bind('s', down)
wait(1800, thing1)
wait(9000, girth)
while True:
 frame_count()
 window.update()
