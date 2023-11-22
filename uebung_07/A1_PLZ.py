import uvicorn
from fastapi import FastAPI

app = FastAPI()

d = {}
file_path = "PLZO_CSV_LV95.csv"

file = open(file_path, encoding="utf-8")
next(file)

for line in file:
    data = line.strip().split(";")
    ortschaft = data[0]
    plz = data[1]
    zusatzziffer = data[2]
    gemeinde = data[3]
    bfsNr = data[4]
    kanton = data[5]
    ostkoord = data[6]
    nordkoord = data[7]
    sprache = data[8]
    d[gemeinde] = {  "PLZ": plz,
                "Gemeinde": gemeinde,
                "Ortschaft": ortschaft,
                "Kanton": kanton,
                "Zusatzziffer": zusatzziffer,
                "BFS-Nr": bfsNr,
                "E": ostkoord,
                "N": nordkoord}
file.close()

@app.get("/search")
async def search(gemeinde: str):
    if gemeinde in d:
        return d[gemeinde]
    else:
        return {"error": "not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)