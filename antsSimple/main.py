import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as rnd
from mpl_interactions import  panhandler, zoom_factory

#local files
import read_data as data
import display, ants

#start_id = input("Start Airport Identificator: ")
#end_id = input("End Airport Identificator: ")
start_id = "EDDH"
end_id = "EGLL"

start_airport = []
end_airport = []
display.plt = plt
ants.plt = plt

for airport in data.airports:
    if airport[0] == start_id:
        start_airport = airport
    if airport[0] == end_id:
        end_airport = airport

if start_airport == end_airport:
    print("Airport(s) not found or same airport id. Exiting.")
    exit()


fig, ax = plt.subplots()
#ax.set_yticklabels([])
#ax.set_xticklabels([])
ax.set_xlabel("Distance from equator (1000km)")
ax.set_ylabel("Distance from prime meridian (1000km)")

display.fromCoords(data.navaids, "RED", 0.2)
display.fromCoords(data.airports, "Blue", 0.4)

display.fromCoords([start_airport,end_airport], "Orange", 20)

for i in range(100):
    ants.Ant(rnd.random()*5,rnd.random()*5,rnd.random()*3.1)

antscat = ants.displayAnts()

def update(frame):
    points = []
    for ant in ants.ants:
        ant.tick()
        points.append(ant.pos)
    antscat.set_offsets(points)
    return antscat

plt.title("Navaids and Airports")
plt.legend(["Navaid","Airport", "Focus", "Ant"]).set_loc("lower right")
#plt.grid(True)
ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=1)
disconnect_zoom = zoom_factory(ax)
pan_handler = panhandler(fig)
plt.show()

