from tkinter import *

class Map:
    def __init__(self, window, color='light blue', width=700, height=400):
        self.width=width
        self.height=height
        self.color=color
        self.canvas=Canvas(window, bg=self.color, height=self.height, width=self.width)
        self.canvas.pack()
        self.text=self.canvas.create_text(20,20,font=('monaco',10), fill='black', anchor=NW)
        self.message=self.canvas.create_text(350,200,font=('monaco',20), fill='black')
        
    def draw_ball(self, oval):
        return self.canvas.create_oval(oval.x1, oval.y1, oval.x2, oval.y2, fill=oval.color)

    def draw_line(self, line):
        return self.canvas.create_line(line.x1, line.y1, line.x2, line.y2, fill=line.color, width=line.width, )
        
    def write_text(self, t):
        self.canvas.itemconfigure(self.text, text=t)

    def write_message(self, t):
        self.canvas.itemconfigure(self.message, text=t)
        
