import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.colorchooser, tkinter.messagebox
from PIL import Image, ImageTk
import numpy as np

window=tk.Tk()
window.title('Tk Grafx 16')
window.configure(bg='#FFFFFF')
window.geometry("768x720+0+0")


#this is for the module
x_len=0
y_len=0
screen_x=0
screen_y=0
pixel_x=0
pixel_y=0
mouse_x=0
mouse_y=0
mouse_colour='#ffffff'
posx_mod=0
posy_mod=0

pixels=[]
sprites=[]
recent_colours=[]
starts=[]
ends=[]
pixel_array=[]

class Pixel():
 def __init__(self, window_name, color, pixel_name, outline):
  self.window_name=window_name
  self.color=color
  self.pixel_name=pixel_name
  self.outline=outline
 def stamp(self):
  tk.canvas.itemconfigure(self.pixel_name, fill=self.color, outline=self.outline) 
 
class Sprite():
 def __init__(self, x, y, sprite, outline):
  self.x=x
  self.y=y
  self.sprite=sprite
  self.outline=outline
  sprites.append(self)
 def render(self):
  sprite_x=round(self.x)
  sprite_y=round(self.y)
  if sprite_x+posx_mod<=159 and sprite_y+posy_mod<=150 and sprite_x+posx_mod>=-90 and sprite_y+posy_mod>=-96:
    try:
     pixel_array[-sprite_y-posy_mod-90][sprite_x+posx_mod+96]=tuple(int(self.sprite.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    except:
     pixel_array[-sprite_y-posy_mod-90][sprite_x+posx_mod+96]=(0,0,0)
  if sprite_x+posx_mod<=pixel_x-1 and sprite_y+posy_mod<=pixel_y-1 and sprite_x+posx_mod>=0 and sprite_y+posy_mod>=0:
    pixels[(sprite_y+posy_mod)*pixel_x+sprite_x+posx_mod].color=self.sprite
    pixels[(sprite_y+posy_mod)*pixel_x+sprite_x+posx_mod].outline=self.outline
    pixels[(sprite_y+posy_mod)*pixel_x+sprite_x+posx_mod].stamp()
 def unrender(self):
  sprite_x=round(self.x)
  sprite_y=round(self.y)
  if sprite_x+posx_mod<=159 and sprite_y+posy_mod<=150 and sprite_x+posx_mod>=-90 and sprite_y+posy_mod>=-96:
   pixel_array[-sprite_y-posy_mod-90][sprite_x+posx_mod+96]=(0,0,0)
  if sprite_x+posx_mod<=pixel_x-1 and sprite_y+posy_mod<=pixel_y-1 and sprite_x+posx_mod>=0 and sprite_y+posy_mod>=0:
    pixels[(sprite_y+posy_mod)*pixel_x+sprite_x+posx_mod].color='#000000'
    pixels[(sprite_y+posy_mod)*pixel_x+sprite_x+posx_mod].outline='white'
    pixels[(sprite_y+posy_mod)*pixel_x+sprite_x+posx_mod].stamp()
    
class BeegSprite():
 def __init__(self, x, y, sprite):
  self.x=x
  self.y=y
  self.sprite=sprite
 def render(self):
  sprite_x=round(self.x)
  sprite_y=round(self.y)
  current_x=sprite_x
  current_y=sprite_y
  for i in range(len(self.sprite)):
   if self.sprite[i]=='n':
    current_x=sprite_x
    current_y+=1
    continue
   if self.sprite[i]==0:
    current_x+=1
    continue
   sprite_name=Sprite(current_x, current_y, self.sprite[i], 'black')
   sprites.append(sprite_name)
   sprite_name.render()
   current_x+=1

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
   if current_x-sprite_x>self.sprite0-1:
    current_x=sprite_x
    current_y+=1
    if self.sprite[current_x-self.x+((current_y-self.y)*self.sprite0)]==0:
     current_x+=1
     continue
    try:
     sprite_name=Sprite(current_x, current_y, self.sprite[current_x-self.x+((current_y-self.y)*self.sprite0)], 'black')
     sprites.append(sprite_name)
     sprite_name.render()
    except:
     fuck=1+1
    continue
   if self.sprite[current_x-self.x+((current_y-self.y)*self.sprite0)]==0:
    current_x+=1
    continue
   try:
     sprite_name=Sprite(current_x, current_y, self.sprite[current_x-self.x+((current_y-self.y)*self.sprite0)], 'black')
     sprites.append(sprite_name)
     sprite_name.render()
   except:
     fuck=1+1
   current_x+=1

def qdee(window_name, scrn_x, scrn_y, pixl_x, pixl_y):
 global x_len
 global y_len
 global pixel_x
 global pixel_y
 global screen_x
 global screen_y
 global pixel_array
 screen_x=scrn_x
 screen_y=scrn_y
 pixel_x=pixl_x
 pixel_y=pixl_y
 x_len=screen_x/pixel_x
 y_len=screen_y/pixel_y
 pixels.clear()
 tk.canvas=Canvas(window_name, height=screen_y-100, width=screen_x)
 tk.canvas.pack(fill=BOTH, side=BOTTOM)
 for i in range(pixel_y):
  for q in range(pixel_x):
   pixel_name=str(q)+'-'+str(i)
   pixel_name=tk.canvas.create_rectangle(q*x_len, screen_y-(i*y_len), q*x_len+x_len, screen_y-(i*y_len-y_len), fill = 'black', outline = 'white', width = 1) 
   pixel_name=Pixel(window_name, '#000000', pixel_name, 'white')
   pixel_name.stamp()
   pixels.append(pixel_name)
 for i in range(240):
  pixel_array.append([])
 for i in range(240):
  for q in range(256):
   pixel_name=str(q)+'-'+str(i)
   pixel_array[i].append((0,0,0))

def render_scene():
 for i in range(len(sprites)):
  sprites[i-1].render()

def destroy():
 pixels.clear()

def left(event):
 if mouse_x<63 and mouse_x>1 and mouse_y<59 and mouse_y>1:
  global posx_mod
  for i in range(len(sprites)):
   sprites[i-1].unrender()
  posx_mod-=1
  for i in range(len(sprites)):
   sprites[i-1].render()
  
def right(event):
 if mouse_x<63 and mouse_x>1 and mouse_y<59 and mouse_y>1:
  global posx_mod
  for i in range(len(sprites)):
   sprites[i-1].unrender()
  posx_mod+=1
  for i in range(len(sprites)):
   sprites[i-1].render()
  
def up(event):
 if mouse_x<63 and mouse_x>1 and mouse_y<59 and mouse_y>1:
  global posy_mod
  for i in range(len(sprites)):
   sprites[i-1].unrender()
  posy_mod+=1
  for i in range(len(sprites)):
   sprites[i-1].render()
  
def down(event):
 if mouse_x<63 and mouse_x>1 and mouse_y<59 and mouse_y>1:
  global posy_mod
  for i in range(len(sprites)):
   sprites[i-1].unrender()
  posy_mod-=1
  for i in range(len(sprites)):
   sprites[i-1].render()
  
def deleted(event):
 for q in range(len(sprites)):
   if sprites[q-1].x+posx_mod==mouse_x and sprites[q-1].y+posy_mod-9==mouse_y:
    sprites[q-1].sprite='#000000'
    sprites[q-1].outline='white'
    sprites[q-1].render()
    sprites.pop(q-1)
 
def start(event):
 for q in range(len(sprites)):
   if sprites[q-1].x+posx_mod==mouse_x and sprites[q-1].y+posy_mod-9==mouse_y:
    sprites.pop(q-1)
 object_name=str(mouse_x)+'-'+str(mouse_y)
 object_name=Sprite(mouse_x-posx_mod, mouse_y-posy_mod+9, 'orange', 'blue')
 global starts
 if len(starts)>0:
  starts[0].sprite='#000000'
  starts[0].outline='white'
  starts[0].render()
 starts.clear()
 starts.append(object_name)
 object_name.render()
 
def stop(event):
 global mouse_x
 global mouse_y
 for q in range(len(sprites)):
   if sprites[q-1].x+posx_mod==mouse_x and sprites[q-1].y+posy_mod-9==mouse_y:
    sprites.pop(q-1)
 object_name=str(mouse_x)+'-'+str(mouse_y)
 object_name=Sprite(mouse_x-posx_mod, mouse_y-posy_mod+9, 'yellow', 'purple')
 object_name.render()
 
def end(event):
 global mouse_x
 global mouse_y
 for q in range(len(sprites)):
   if sprites[q-1].x+posx_mod==mouse_x and sprites[q-1].y+posy_mod-9==mouse_y:
    sprites.pop(q-1)
 object_name=str(mouse_x)+'-'+str(mouse_y)
 object_name=Sprite(mouse_x-posx_mod, mouse_y-posy_mod+9, 'green', 'red')
 global ends
 if len(ends)>0:
  ends[0].sprite='#000000'
  ends[0].outline='white'
  ends[0].render()
 ends.clear()
 ends.append(object_name)
 object_name.render()

def pick_colour(event):
 global mouse_colour
 mouse_colour=recent.get()
 if mouse_colour in recent_colours:
  recent_colours.remove(mouse_colour)
 recent_colours.insert(0, mouse_colour)
 if len(recent_colours)>9:
  recent_colours.pop(0)
 recent['values']=recent_colours

def get_sprite():
 end_sprite=[]
 current_x=starts[0].x
 current_y=starts[0].y
 varidk=0
 breaking=0
 for i in range(999999999999):
  current_x+=1
  varidk=0
  for q in range(len(sprites)):
   if sprites[q-1].x==current_x and sprites[q-1].y==current_y:
    if sprites[q-1].outline=='white':
     end_sprite.append(0)
     varidk=1
     break
    elif sprites[q-1].outline=='purple':
     varidk=1
     current_y+=1
     current_x=starts[0].x
     end_sprite.append('n')
     break
    elif sprites[q-1].outline=='red':
     varidk=1
     breaking=1
     break
    else:
     varidk=1
     end_sprite.append(tuple(int(sprites[q-1].sprite.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)))
     break
  if breaking==1:
   break
  if varidk==0:
   end_sprite.append(0)
 print(end_sprite)

def get_background():
 end_sprite=[]
 background_sprite=[]
 current_x=starts[0].x
 current_y=starts[0].y
 varidk=0
 othervaridk=0
 breaking=0
 for i in range(9999999999999):
  current_x+=1
  varidk=0
  for q in range(len(sprites)):
   if sprites[q-1].x==current_x and sprites[q-1].y==current_y:
    if sprites[q-1].outline=='white':
     end_sprite.append(0)
     varidk=1
     othervaridk+=1
     break
    elif sprites[q-1].outline=='purple':
     varidk=1
     othervaridk=0
     current_y+=1
     current_x=starts[0].x
     break
    elif sprites[q-1].outline=='red':
     varidk=1
     breaking=1
     break
    else:
     varidk=1
     end_sprite.append(tuple(int(sprites[q-1].sprite.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)))
     othervaridk+=1
     break
  if breaking==1:
   break
  if varidk==0:
   end_sprite.append(0)
   othervaridk+=1
 background_sprite.append(othervaridk)
 background_sprite.append(end_sprite)
 print(background_sprite)
 
def paint(event):
 global mouse_colour
 for q in range(len(sprites)):
  if sprites[q-1].x+posx_mod==mouse_x and sprites[q-1].y+posy_mod-9==mouse_y:
   sprites[q-1].sprite=mouse_colour
 object_name=str(mouse_x)+'-'+str(mouse_y)
 object_name=Sprite(mouse_x-posx_mod, mouse_y-posy_mod+9, mouse_colour, 'black')
 object_name.render()

def load_sprite():
  spriteset=loadsprite.get()
  spriteset=eval(spriteset)
  if isinstance(spriteset[0],int)==True and spriteset[0]!=0:  #format [sprite0,[sprite]]
   sprite0=spriteset[0]
   for i in range(len(spriteset[1])):
    if spriteset[1][i]!=0 and spriteset[1][i]!='n':
     spriteset[1].insert(i, '')
     spriteset[1][i]='%02x%02x%02x' % spriteset[1][i+1]
     print(spriteset[1][i])
     spriteset[1][i]='#'+spriteset[1][i]
     spriteset[1].pop(i+1)
   sproot=Background(20+posx_mod, 18+posy_mod, sprite0, spriteset[1])
   sproot.render()
  else:  #format [sprite]
   for i in range(len(spriteset)):
    if spriteset[i]!=0 and spriteset[i]!='n':
     spriteset.insert(i, '')
     spriteset[i]='%02x%02x%02x' % spriteset[i+1]
     spriteset[i]='#'+spriteset[i]
     spriteset.pop(i+1)
   sproot=BeegSprite(20+posx_mod, 18+posy_mod, spriteset)
   sproot.render()

qdee(window, 768, 720, 64, 60)
render_scene()
window.bind('d', left)
window.bind('a', right)
window.bind('s', up)
window.bind('w', down)
def mouse_move(event):
 x, y=event.x, event.y
 global mouse_x
 global mouse_y
 mouse_x, mouse_y=round(x/12-0.5), round((screen_y-y-100)/12)
 
tk.canvas.bind("<Button-1>", paint)
window.bind("<BackSpace>", deleted)
window.bind("<space>", start)
window.bind("<m>", stop)
window.bind("<p>", end)
tk.canvas.bind('<Motion>', mouse_move)
recent= ttk.Combobox(window, values = recent_colours)
recent.set('Enter colour')
recent.place(x=250, y=45)
window.bind('<Return>', pick_colour)
thebutton=Button(window, text="Get sprite as object", command=get_sprite)
thebutton.place(x=100, y=55)
theotherbutton=Button(window, text="Get sprite as background", command=get_background)
theotherbutton.place(x=85, y=30)
loadsprite=Entry(window, width=20)
loadsprite.insert(0,'Enter sprite')
loadsprite.place(x=500, y=60)
textee=Label(window, text="Load Sprite:")
textee.place(x=500, y=35)
theotherotherbutton=Button(window, text="Load", command=load_sprite)
theotherotherbutton.place(x=700, y=63)

def openColorDialog():
    global mouse_colour
    global recent_colours
    # display color dialog box
    color = colorDialog.show()
    # show the chosen RBG value
    mouse_colour=color[1]
    if mouse_colour in recent_colours:
     recent_colours.remove(mouse_colour)
    recent_colours.insert(0, mouse_colour)
    if len(recent_colours)>9:
     recent_colours.pop(0)
    recent['values']=recent_colours

colorDialog = tkinter.colorchooser.Chooser(window)
        
colour_picker=Button(window, text="Open color dialog box", command=openColorDialog)
colour_picker.place(x=280,y=20)
while True:
 array = np.array(pixel_array, dtype=np.uint8)
 

 # Use PIL to create an image from the new array of pixels
 new_image = Image.fromarray(array)
 img=ImageTk.PhotoImage(new_image)
 label=tk.Label(image=img)
 label.place(x=512, y=480)
 window.update()
 label.destroy()
