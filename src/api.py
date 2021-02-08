from fastapi import FastAPI, Depends, HTTPException
from typing import List, Dict, Any

from src.storage import download_images_from_server
from src.auth import basic_auth
from src.model import Model
from src.logger import logger

app = FastAPI()

@app.post("/download")
async def download_images(model: Model, auth: str = Depends(basic_auth)) -> Dict[str, Any]:
    if not model.images:
        raise HTTPException(status_code=400, detail="There are not images to download")
    images: List[Dict[str, Any]] = await download_images_from_server(model.images)
    return {
        "message": "Images have been downloaded successfully",
        "images": images
    }