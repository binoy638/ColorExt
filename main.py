from fastapi import Body,FastAPI
from colorExt import getColorFromImage

app = FastAPI()

@app.get("/")
def read_root():
    return {"Status": "Server is ready"}
#https://i.scdn.co/image/ab67616d00001e02ed3faf75cfde73ebb4734162
@app.post("/color")
def getColor(payload: dict = Body(...)):
    colors = getColorFromImage(payload["url"],payload["name"])
    if not colors:
        return {"StatusCode":404}
    return {"StatusCode":200,"data":colors}
