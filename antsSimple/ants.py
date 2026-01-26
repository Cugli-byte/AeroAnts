import display
import math
import matplotlib

plt = []
display.plt = plt

ants=[]
phermones=[]

class Ant:
    pos = (0,0)
    dir = 0.0
    speed = 10**-3
    range = 1

    def __init__(self, x,y, dir):
        self.pos = (x,y)
        self.dir = dir
        ants.append(self)

    #Gets run every tick and updates position accordingly
    #TODO: Ant logic
    def tick(self):
        self.sense()
        self.pos=(self.pos[0]+self.speed*math.cos(self.dir),self.pos[1]+self.speed*math.sin(self.dir))

    #Update dir based on surrounding pheromones
    def sense(self):
        surrounding=[]
        for p in phermones:
            print(math.sqrt((p.pos[0]-self.pos[0])**2+(p.pos[1]-self.pos[1])**2))
    
    #Debug display of one ant
    def display(self):
        display.fromCoords([("Ant",self.pos)], "BROWN", 2)

class Pheromone:
    pos = (0,0)
    weight = 0.0

    def __init__(self, x,y, weight):
        self.pos = (x,y)
        self.weight = weight;
        phermones.append(self)


    #TODO: Pheromone logic

#Generate Scatter for Ants
def displayAnts() -> matplotlib.collections.PathCollection:
    points = []
    for ant in ants:
        points.append(("Ant",ant.pos))
    
    return display.fromCoords(points, "Brown", 2)

#Generate Scatter for Pheromones
def displayPheromones() -> matplotlib.collections.PathCollection:
    points = []
    for p in phermones:
        points.append(("Pheromone",p.pos))
    
    return display.fromCoords(points, "Cyan", 2)

