import os
import random
import json
from PIL import Image

sourceFiles = os.listdir("Source")

with open("Template_Data.json") as file:
    jsonData = json.load(file)

chosenFile = random.choice(jsonData["templates"])
template = Image.open(r"Templates/" + chosenFile["name"])

for values in chosenFile["values"]:
    posX = values["posX"]
    posY = values["posY"]
    sizeX = values["sizeX"]
    sizeY = values["sizeY"]
    sourceName = random.choice(sourceFiles)
    sourceFiles.remove(sourceName)
    source = Image.open("Source/" + sourceName)
    source = source.resize(size=(sizeX, sizeY))
    position = (posX, posY)
    template.paste(source, position)

template.show()
