import mapbase

class Line:
    def __init__(self, mapbase, color='green', x=50, y=350, width=3):
        self.mapbase=mapbase
        self.color=color
        self.x1=x
        self.y1=y
        self.x2=x
        self.y2=y
        self.width=width
        self.line=self.mapbase.draw_line(self)

    def set_line(self, x, y):
        self.x2=self.x1 +x
        self.y2=self.y1 +y
        self.mapbase.canvas.coords(self.line, self.x1, self.y1, self.x2, self.y2)
