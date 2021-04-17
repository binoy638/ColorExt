from fastapi import Body,FastAPI, File, UploadFile, HTTPException
from colorExt import getColorFromImage,getColorFromImage_
from dotenv import load_dotenv
import shutil
import os
import json
import redis

load_dotenv()
app = FastAPI()
cache = redis.from_url(url=os.environ.get("REDIS_URL"),decode_responses=True)


@app.get("/")
def read_root():
    return {"Status": "Server is ready"}
#https://i.scdn.co/image/ab67616d00001e02ed3faf75cfde73ebb4734162
@app.post("/url_color",status_code=200)
def getColor(payload: dict = Body(...)):
    url = payload["url"]
    isCached = cache.get(url)
    if isCached:
        colors = json.loads(isCached)
    else:
        colors = getColorFromImage(url)
        if colors:
            cache.set(url,json.dumps(colors))
        else:
            raise HTTPException(status_code=404, detail="Could not download image")
    return {"colors":colors}

@app.post("/file_color",status_code=200)
async def image(image: UploadFile = File(...)):
    path = f"temp/{image.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    colors = getColorFromImage_(path)
    if not colors:
        raise HTTPException(status_code=500, detail="Could not process image")
    return {"colors":colors}