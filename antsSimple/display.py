from pyproj import Transformer
import matplotlib
transformer = Transformer.from_crs("EPSG:4326", "EPSG:4087")
plt = []

def degToXY(lon, lat):
    x, y = transformer.transform(lon, lat)
    return x*10**-6,y*10**-6

def pointTransform(point):
    x, y = degToXY(point[1][0], point[1][1])
    return (point[0],(x,y))

def fromCoords(points, color, size) -> matplotlib.collections.PathCollection:
    nav_x  = []
    nav_y = []

    for nav in points:
        x, y = pointTransform(nav)[1]
        nav_x.append(x)
        nav_y.append(y)
    return plt.scatter(nav_x, nav_y, c=color, s=size, marker='o')