import display
import math
import matplotlib

plt = []
display.plt = plt

ants=[]

class Ant:
    pos = (0,0)
    dir = 0.0
    speed = 10**-3

    def __init__(self, x,y, dir):
        self.pos = (x,y)
        self.dir = dir
        ants.append(self)

    def tick(self):
        self.pos=(self.pos[0]+self.speed*math.cos(self.dir),self.pos[1]+self.speed*math.sin(self.dir))
        print(self.pos)
    
    def display(self):
        display.fromCoords([("Ant",self.pos)], "BROWN", 2)

class Pheromone:
    pos = (0,0)
    weight = 0.0

    def __init__(self, x,y, weight):
        self.pos = (x,y)
        self.weight = weight;

def displayAnts() -> matplotlib.collections.PathCollection:
    points = []
    for ant in ants:
        points.append(("Ant",ant.pos))
    
    return display.fromCoords(points, "Brown", 2)

