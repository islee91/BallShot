import mapbase
from math import sqrt

class Ball:
    def __init__(self, mapbase, color='red', r=10, x=50, y=350):
        self.mapbase=mapbase
        self.color=color
        self.r=r
        self.x1=x-r
        self.y1=y-r
        self.x2=x+r
        self.y2=y+r
        self.x_sp=0
        self.y_sp=0
        self.ball=self.mapbase.draw_ball(self)

    def set_pos(self, x, y):
        self.x1=x-self.r
        self.y1=y-self.r
        self.x2=x+self.r
        self.y2=y+self.r

    def set_sp(self, xs, ys):
        self.x_sp=xs
        self.y_sp=ys

    def move(self):
        self.x1+=self.x_sp
        self.y1+=self.y_sp
        self.x2+=self.x_sp
        self.y2+=self.y_sp

        self.mapbase.canvas.coords(self.ball, self.x1, self.y1, self.x2, self.y2)

    def collision_check(self, other):
        x=((other.x1+other.r)-(self.x1+self.r))**2
        y=((other.y1+other.r)-(self.y1+self.r))**2
        z=sqrt(x+y)
        if z<(self.r+other.r):
            return 2
        if self.y2>=400:
            return 1
        else:
            return 0
    



        
