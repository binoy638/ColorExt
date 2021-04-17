import requests
import extcolors
import os
import uuid

temp_dir = "temp"

if not os.path.exists(temp_dir):
    os.mkdir(temp_dir)

def getRBGarray(tupleArray,pixel_count):
    colors = []
    for color in tupleArray:
        percent = color[1]/pixel_count * 100
        colors.append([str(color[0]),round(percent,2)])
    return colors

def downloadImage(URL):
    try:
        r = requests.get(URL)
        if r.status_code == 200:
            name = uuid.uuid4()
            path = f"{temp_dir}/{name}.jpg"
            with open(path, "wb") as f:
                f.write(r.content)
            return path
        else:
            return None
    except:
        return None 
    


def extractColors(path):
    colors, pixel_count = extcolors.extract_from_path(path)
    return getRBGarray(colors,pixel_count) 

def cleanUp(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print(f"{path} not found")


def getColorFromImage(url):
    path = downloadImage(url)
    #download and save the image
    if not path:
        return None
    #extract colors from the image
    colors = extractColors(path)  
    #delete the image        
    cleanUp(path)                    
    return colors                     

def getColorFromImage_(path):
    if not path:
        return None
    #extract colors from the image
    colors = extractColors(path)  
    #delete the image        
    cleanUp(path)                    
    return colors                     
