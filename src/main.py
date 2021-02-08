import os
import uvicorn

from src.api import app
from src.secrets import PORT, PYTHON_ENV
from src.logger import logger

def main() -> None:
    logger.info(f'Images downloader running at port {PORT} in {PYTHON_ENV} mode')
    uvicorn.run(app, host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    main()