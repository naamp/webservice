from pyproj import Transformer
import uvicorn
from fastapi import FastAPI

app = FastAPI()

wgs84= "epsg:4326"
lv95= "epsg:2056"

wgs84lv95 = Transformer.from_crs("epsg:4326", "epsg:2056")

lv95wgs84 = Transformer.from_crs("epsg:2056", "epsg:4326")


@app.get("/wgs84lv95")
async def getlv95(lng: float=0, lat: float=0):
        return {"Koordinaten LV95": wgs84lv95.transform(lng, lat)}

@app.get("/lv95wgs84")
async def getwgs84(E: float=0, N: float=0):
        res_wgs84 = lv95wgs84.transform(E, N)
        return {"Koordinaten LV95": {"Lat":res_wgs84[0],
                "Lng": res_wgs84[1]}}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)