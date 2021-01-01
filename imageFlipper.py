#!/usr/bin/env python

import tkinter as tk
from PIL import Image, ImageTk
import os

cell_rows=5
cell_cols=5
animation = []
ca = 0
mtime=0

def update_animation():
    global window,img,ca,mtime,animation
    
    m = os.stat("sample1.png").st_mtime
    if m != mtime:
        loadAnimation()
        mtime=m
        print("File changed")
        
    ca+=1
    if ca > 10:
        ca =0
    render = ImageTk.PhotoImage(animation[ca])
    img.configure(image=render)
    img.image = render
    window.after(200, update_animation)

def loadAnimation():
    global animation,cell_rows, cell_cols
    load = Image.open("sample1.png")
    width, height = load.size
    width = width / cell_cols
    height = height / cell_rows
    print("Cell size {},{}". format( width, height) )
    animation = []
    for y in range(0, cell_rows):
        for x in range(0, cell_cols):
            # (left, top, right, bottom)
            _x = x * width 
            _y = y * height 
            animation.append( load.crop( (_x,_y, _x+width, _y+height) ) )


window = tk.Tk()


loadAnimation()

render = ImageTk.PhotoImage(animation[0])
img = tk.Label(window, image=render)
img.image = render
img.place(x=0, y=0)

window.after(200, update_animation)
window.mainloop()

