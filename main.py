from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
import uvicorn
from pathlib import Path

from dotenv import dotenv_values

app = FastAPI()

config = dotenv_values()
SECRET_CODE = config["SECRET_CODE"]


@app.get("/")
async def main():
    return {
        "info": "SIMPLE API"
    }


@app.get("/get/{secret_code}/{path:path}")
async def get_file_or_directory(secret_code: str, path: str):
    if secret_code != SECRET_CODE:
        raise HTTPException(status_code=403, detail="Forbidden")

    file_path = Path(config["PATH1"]) / path

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Path not found")

    if file_path.is_dir():
        entries = [entry.name for entry in file_path.iterdir()]
        return JSONResponse(content={"directory_contents": entries})

    if file_path.is_file():
        with open(file_path, 'r', encoding="utf-8") as file:
            file_content = file.read()
        return PlainTextResponse(content=file_content)

    raise HTTPException(status_code=400, detail="Invalid path type")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)