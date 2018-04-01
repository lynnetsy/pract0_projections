import file as rf
import projections

filename = "data.txt"

print("* reading file: {0}".format(filename))
points = rf.read(filename)

print("* creating projections")
for point in points:
    projections.npstere(id=point["id"], lat=point["lat"], lon=point["lon"])
    projections.spstere(id=point["id"], lat=point["lat"], lon=point["lon"])
    projections.northo(id=point["id"], lat=point["lat"], lon=point["lon"])
    projections.sortho(id=point["id"], lat=point["lat"], lon=point["lon"])
    projections.ngnom(id=point["id"], lat=point["lat"], lon=point["lon"])
    projections.sgnom(id=point["id"], lat=point["lat"], lon=point["lon"])

print("* end")
