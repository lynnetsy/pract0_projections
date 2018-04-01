from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

def npstere(id, lat, lon):
    if lat < 0:
        return

    fig = plt.figure()
    imgPath = "./img/npstere/fig_{0}.png".format(id)
    groundColor = "#ffba60"
    waterColor = "#30afff"

    map = Basemap(projection="npstere", boundinglat=0, lon_0=0)

    map.drawparallels(np.arange(-80.,81.,20.))
    map.drawmeridians(np.arange(-180.,181.,20.))

    map.drawmapboundary(fill_color=waterColor)
    map.fillcontinents(color=groundColor, lake_color=waterColor)
    map.drawcoastlines()

    x, y = map(lon, lat)

    distanceToPoint = 200000
    plt.annotate("id: {0}".format(id),
        xy=(x + distanceToPoint, y),
        xycoords="data",
        xytext=(90, 20),
        textcoords="offset points",
        color="black",
        arrowprops=dict(arrowstyle="fancy", color="#8400ad"))

    map.plot(x, y, marker="D", color="#1b9b2d",  markersize=6, markeredgewidth=2, markeredgecolor="r")

    fig.savefig(imgPath)
    print("projection npstere saved in: {0}".format(imgPath))

def spstere(id, lat, lon):
    if lat > 0:
        return

    fig = plt.figure()
    imgPath = "./img/spstere/fig_{0}.png".format(id)
    groundColor = "#ffba60"
    waterColor = "#30afff"

    map = Basemap(boundinglat=0, lon_0=0, projection="spstere")

    map.drawparallels(np.arange(-80.,81.,20.))
    map.drawmeridians(np.arange(-180.,181.,20.))
    map.drawmapboundary(fill_color=waterColor)
    map.fillcontinents(color=groundColor, lake_color=waterColor)
    map.drawcoastlines()

    x, y = map(lon, lat)

    distancetopoint = 200000
    plt.annotate("id: {0}".format(id),
    xy=(x + distancetopoint, y),
    xycoords="data",
    xytext=(90, 20),
    textcoords="offset points",
    color="black",
    arrowprops=dict(arrowstyle="fancy", color="#8400ad"))

    map.plot(x, y, marker="D", color="#1b9b2d",  markersize=6, markeredgewidth=2, markeredgecolor="r")
    fig.savefig(imgPath)
    print("projection spstere saved in: {0}".format(imgPath))

def northo(id, lat, lon):
    if lat < 0:
        return

    fig = plt.figure()
    imgPath = "./img/northo/fig_{0}.png".format(id)
    groundColor = "#ffba60"
    waterColor = "#30afff"

    map = Basemap(lat_0=90, lon_0=0, projection="ortho")

    map.drawparallels(np.arange(-80.,81.,20.))
    map.drawmeridians(np.arange(-180.,181.,20.))
    map.drawmapboundary(fill_color=waterColor)
    map.fillcontinents(color=groundColor, lake_color=waterColor)
    map.drawcoastlines()

    x, y = map(lon, lat)

    distancetopoint = 200000
    plt.annotate("id: {0}".format(id),
    xy=(x + distancetopoint, y),
    xycoords="data",
    xytext=(90, 20),
    textcoords="offset points",
    color="black",
    arrowprops=dict(arrowstyle="fancy", color="#8400ad"))

    map.plot(x, y, marker="D", color="#1b9b2d",  markersize=6, markeredgewidth=2, markeredgecolor="r")
    fig.savefig(imgPath)
    print("projection North Pole Orthographic saved in: {0}".format(imgPath))

def sortho(id, lat, lon):
    if lat > 0:
        return

    fig = plt.figure()
    imgPath = "./img/sortho/fig_{0}.png".format(id)
    groundColor = "#ffba60"
    waterColor = "#30afff"

    map = Basemap(lat_0=-90, lon_0=0, projection="ortho")

    map.drawparallels(np.arange(-80.,81.,20.))
    map.drawmeridians(np.arange(-180.,181.,20.))
    map.drawmapboundary(fill_color=waterColor)
    map.fillcontinents(color=groundColor, lake_color=waterColor)
    map.drawcoastlines()

    x, y = map(lon, lat)

    distancetopoint = 200000
    plt.annotate("id: {0}".format(id),
    xy=(x + distancetopoint, y),
    xycoords="data",
    xytext=(90, 20),
    textcoords="offset points",
    color="black",
    arrowprops=dict(arrowstyle="fancy", color="#8400ad"))

    map.plot(x, y, marker="D", color="#1b9b2d",  markersize=6, markeredgewidth=2, markeredgecolor="r")
    fig.savefig(imgPath)
    print("projection sortho saved in: {0}".format(imgPath))

def ngnom (id, lat, lon):
    if lat < 0:
        return

    fig = plt.figure()
    imgPath = "./img/ngnom/fig_{0}.png".format(id)
    groundColor = "#ffba60"
    waterColor = "#30afff"

    map = Basemap(width=15.e6, height=15.e6, lat_0=90, lon_0=0, projection="gnom")

    map.drawparallels(np.arange(-80.,81.,20.))
    map.drawmeridians(np.arange(-180.,181.,20.))
    map.drawmapboundary(fill_color=waterColor)
    map.fillcontinents(color=groundColor, lake_color=waterColor)
    map.drawcoastlines()

    x, y = map(lon, lat)

    distancetopoint = 200000
    plt.annotate("id: {0}".format(id),
    xy=(x + distancetopoint, y),
    xycoords="data",
    xytext=(90, 20),
    textcoords="offset points",
    color="black",
    arrowprops=dict(arrowstyle="fancy", color="#8400ad"))

    map.plot(x, y, marker="D", color="#1b9b2d",  markersize=6, markeredgewidth=2, markeredgecolor="r")
    fig.savefig(imgPath)
    print("projection Gnomonic North Pole saved in: {0}".format(imgPath))

def sgnom (id, lat, lon):
    if lat >0:
        return

    fig = plt.figure()
    imgPath = "./img/sgnom/fig_{0}.png".format(id)
    groundColor = "#ffba60"
    waterColor = "#30afff"

    map = Basemap(width=15.e6, height=15.e6, lat_0=-90, lon_0=0, projection="gnom")

    map.drawparallels(np.arange(-80.,81.,20.))
    map.drawmeridians(np.arange(-180.,181.,20.))
    map.drawmapboundary(fill_color=waterColor)
    map.fillcontinents(color=groundColor, lake_color=waterColor)
    map.drawcoastlines()

    x, y = map(lon, lat)

    distancetopoint = 200000
    plt.annotate("id: {0}".format(id),
    xy=(x + distancetopoint, y),
    xycoords="data",
    xytext=(90, 20),
    textcoords="offset points",
    color="black",
    arrowprops=dict(arrowstyle="fancy", color="#8400ad"))

    map.plot(x, y, marker="D", color="#1b9b2d",  markersize=6, markeredgewidth=2, markeredgecolor="r")
    fig.savefig(imgPath)
    print("projection Gnomonic South Pole saved in: {0}".format(imgPath))
