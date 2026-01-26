import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as rnd
from mpl_interactions import  panhandler, zoom_factory

#local files
#temporary test data from csv
import read_data as data
import display, ants

#Define ICAO-Codes of Start and End Airport
start_id = "EDDH"
end_id = "EGLL"

start_airport = []
end_airport = []
display.plt = plt
ants.plt = plt

#Search for Airports using ICAO Codes
for airport in data.airports:
    if airport[0] == start_id:
        start_airport = airport
    if airport[0] == end_id:
        end_airport = airport

if start_airport == end_airport:
    print("Airport(s) not found or same airport id. Exiting.")
    exit()


fig, ax = plt.subplots()
ax.set_xlabel("Distance from equator (1000km)")
ax.set_ylabel("Distance from prime meridian (1000km)")

#Plot Navaids and Airports
display.fromCoords(data.navaids, "RED", 0.2)
display.fromCoords(data.airports, "Blue", 0.4)

#Plot start and end Airport
display.fromCoords([start_airport,end_airport], "Orange", 20)

ants.Ant(0,0,3.14-rnd.random()*6.28)

for i in range(100):
    ants.Pheromone(rnd.random()*50,rnd.random()*50,1.0)

#Define Scatter for all Ants and Pheromones
antscat = ants.displayAnts()
pherscat = ants.displayPheromones()

#Update Animation
def update(frame):
    points = []
    for ant in ants.ants:
        ant.tick()
        points.append(ant.pos)
    antscat.set_offsets(points)
    return antscat

#Matplot stuff
plt.title("AeroAnts")
plt.legend(["Navaid","Airport", "Focus", "Ant"]).set_loc("lower right")
ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=1)
disconnect_zoom = zoom_factory(ax)
pan_handler = panhandler(fig)
plt.show()

