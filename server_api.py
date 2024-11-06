from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import UploadFile, File
from pathlib import Path
from ingest import run_ingest
from main import ask
import os

def data_dirname():
    return Path(__file__).resolve().parents[0] / "data"

class User_input(BaseModel):
    x: int
    y: int
    
app = FastAPI()

@app.post("/generate")
def generate(input:User_input):
    result = input.x+input.y
    return result


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    path_to_save_file = data_dirname()
    file_location = f"{path_to_save_file}/{file.filename}"
    if os.path.isfile(file_location):
         os.remove(file_location)
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    run_ingest(file_location)
    ans = ask()

    return ans
        
    