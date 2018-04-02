import imageio
from pprint import pprint
from os import listdir
from os.path import isfile, join

def createGif(name, path, gifPath):
    imgs = []
    for file in listdir(path):
        if isfile(join(path, file)) and file.find(".png") >= 0:
            imgs.append(join(path, file))

    images = []
    for img in imgs:
        images.append(imageio.imread(img))

    imageio.mimsave("{0}/{1}.gif".format(gifPath, name), images)
