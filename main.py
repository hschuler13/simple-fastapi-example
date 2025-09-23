from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from pathlib import Path
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Professors API",
    description="A simple FastAPI app using JSON as a database, demonstrating GET, POST, PUT, DELETE and HTML response.",
    version="1.0.0"
)

# Always resolve data.json relative to this file
DATA_FILE = Path(__file__).parent / "data.json"

def read_data():
    """Read JSON file and return its contents."""
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print("Error reading JSON file:", e)
        return {"cats": []}

def write_data(data):
    """Write data back to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

class Prof(BaseModel):
    code: int
    name: str
    message: str
    image_url: str = None

@app.get("/prof", response_model=list[Prof])
def list_profs():
    """Return all professors from data.json."""
    data = read_data()
    return data["professors"]

@app.get("/profs/{code}", response_model=Prof)
def get_profs(code: int):
    """Return a single professor by its code."""
    data = read_data()
    for prof in data["professors"]:
        if prof["code"] == code:
            return prof
    raise HTTPException(status_code=404, detail="Professor not found")

@app.post("/profs", response_model=Prof)
def add_prof(prof: Prof):
    """Add a new professor to the JSON file."""
    data = read_data()
    if any(c["code"] == prof.code for c in data["profs"]):
        raise HTTPException(status_code=400, detail="Professor code already exists")
    data["profs"].append(prof.dict())
    write_data(data)
    return prof

@app.put("/profs/{code}", response_model=Prof)
def update_prof(code: int, prof: Prof):
    """Update an existing professor via its code."""
    data = read_data()
    for idx, c in enumerate(data["professors"]):
        if c["code"] == code:
            data["professors"][idx] = prof.dict()
            write_data(data)
            return prof
    raise HTTPException(status_code=404, detail="Professor not found")

@app.delete("/profs/{code}")
def delete_prof(code: int):
    """Delete a professor via its code."""
    data = read_data()
    for idx, c in enumerate(data["professors"]):
        if c["code"] == code:
            deleted = data["professors"].pop(idx)
            write_data(data)
            return {"deleted": deleted}
    raise HTTPException(status_code=404, detail="Professor not found")

@app.get("/profs/{code}/image", response_class=HTMLResponse)
def show_prof_image(code: int):
    """
    Show an HTML page with the professor's image embedded.
    This demonstrates returning HTML instead of JSON.
    """
    data = read_data()
    for prof in data["professors"]:
        if prof["code"] == code and prof.get("image_url"):
            return f"""
            <html>
              <head><title>{prof['name']}</title></head>
              <body style='text-align:center; font-family:sans-serif; background-color: #c9ebee;'>
              <div style='display: flex; justify-content: center; align-items: center; max-height: 70%; max-width: 70%; padding: 10px; margin-left: auto; margin-right: auto;  background-image: linear-gradient(to top, #ff7ba0, #ffc2d3); border-radius: 20px; border-style: solid; border-width: 5px; border-color: #c32854;'>
                <div style='margin-top: 20px; margin-bottom: 20px; justify-content: center; max-width: 50%;'>
                    <img src="{prof['image_url']}" alt="prof image" style="max-width:50%; max-height:70%; height:70%; border-radius: 10px;" />
                </div>
                <div style='margin-top: 20px; margin-bottom: 20px; justify-content: center; max-width: 50%; color: #c32854;'>
                    <h1>{prof['name']} ({prof['code']})</h1>
                    <p>{prof['message']}</p>
                </div>
              </div>
              </body>
            </html>
            """
    raise HTTPException(status_code=404, detail="Professor not found or no image URL")