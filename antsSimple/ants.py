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

    #Gets run every tick and updates position accordingly
    #TODO: Ant logic
    def tick(self):
        self.pos=(self.pos[0]+self.speed*math.cos(self.dir),self.pos[1]+self.speed*math.sin(self.dir))
        print(self.pos)
    
    #Debug display of one ant
    def display(self):
        display.fromCoords([("Ant",self.pos)], "BROWN", 2)

class Pheromone:
    pos = (0,0)
    weight = 0.0

    def __init__(self, x,y, weight):
        self.pos = (x,y)
        self.weight = weight;

    #TODO: Pheromone logic

#Generate Scatter for Ants
def displayAnts() -> matplotlib.collections.PathCollection:
    points = []
    for ant in ants:
        points.append(("Ant",ant.pos))
    
    return display.fromCoords(points, "Brown", 2)

