import os
import asyncio
import aiofiles

from aiohttp import ClientSession
from src.generator import generate_hash
from src.secrets import IMAGES_PATH
from src.logger import logger
from typing import List, Dict, Any

async def download_file(session: Any, image: Dict[str, Any], filename: str) -> Any:
    try:
        async with session.get(image['resource']) as response:
            if response.status == 200:
                async with aiofiles.open(filename, mode='wb') as f:
                    await f.write(await response.read())
                    return {
                        "image_id": image['image_id'],
                        "resource": filename.split('/')[-1]
                    }
    except:
        logger.error(f"Error to get {filename} from server")

async def bound_file(sem: Any, session: Any, image: Dict[str, Any], filename: str) -> Any:
    async with sem: 
        return await download_file(session, image, filename)
    
async def download_files(images: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    headers = {"user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
    async with ClientSession(headers=headers) as session:
        sem = asyncio.Semaphore(1000)
        tasks = [asyncio.ensure_future(bound_file(sem, session, image, get_filename(image))) for image in images]
        responses = await asyncio.gather(*tasks)
        downloaded_images = [image for image in responses]
        return downloaded_images
        
async def download_images_from_server(images: List[Dict[str, Any]]) -> Any:
    try:
        downloaded_images: List[Dict[str, Any]] = await download_files(images)
        logger.info(f'Images from server have been downloaded successfully')
        return downloaded_images
    except Exception as error:
        logger.error(f'Error to download images from server: {error}')
        raise

def get_filename(image: Dict[str, Any]) -> str:
    image_dir = '{}{}'.format(IMAGES_PATH, image['image_id'])
    image_file = '{}.jpg'.format(generate_hash(image['resource']))
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    return os.path.join(image_dir, image_file)