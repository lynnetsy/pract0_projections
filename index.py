import file
import image
import projections

filename = "data.txt"

print("* reading file: {0}".format(filename))
points = file.read(filename)

print("* creating projections")
for point in points:
    if "lat" in point and "lon" in point:
        projections.npstere(id=point["id"], lat=point["lat"], lon=point["lon"])
        projections.northo(id=point["id"], lat=point["lat"], lon=point["lon"])
        projections.ngnom(id=point["id"], lat=point["lat"], lon=point["lon"])

        projections.spstere(id=point["id"], lat=point["lat"], lon=point["lon"])
        projections.sortho(id=point["id"], lat=point["lat"], lon=point["lon"])
        projections.sgnom(id=point["id"], lat=point["lat"], lon=point["lon"])

print("* create images .gif")
image.createGif(name="ngnom", path="./img/ngnom/", gifPath="./gif")
image.createGif(name="northo", path="./img/northo/", gifPath="./gif")
image.createGif(name="npstere", path="./img/npstere/", gifPath="./gif")
image.createGif(name="sgnom", path="./img/sgnom/", gifPath="./gif")
image.createGif(name="sortho", path="./img/sortho/", gifPath="./gif")
image.createGif(name="spstere", path="./img/spstere/", gifPath="./gif")

print("* end")
