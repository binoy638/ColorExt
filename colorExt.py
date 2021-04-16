import requests
import extcolors
import os

temp_dir = "temp"

if not os.path.exists(temp_dir):
    os.mkdir(temp_dir)

def getRBGarray(tupleArray):
    colors = []
    for color in tupleArray:
        colors.append(str(color[0]))
    return colors

def downloadImage(URL,name):
    r = requests.get(URL)
    path = f"{temp_dir}/{name}.jpg"
    with open(path, "wb") as f:
        f.write(r.content)
    return path

def extractColors(path):
    colors, pixel_count = extcolors.extract_from_path(path)
    return getRBGarray(colors) 

def cleanUp(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print(f"{path} not found")

def getColorFromImage(url,name):
    path = downloadImage(url,name)    #download and save the image
    colors = extractColors(path)          #extract colors from the image
    cleanUp(path)                    #delete the image
    return colors                     

