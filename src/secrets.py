import os
from dotenv import load_dotenv

from src.logger import logger

ENV = os.environ.get('ENV')
if ENV == 'production':
    dotenv_path = '.env'
    logger.info('Loading production environment variables')
else:
    dotenv_path = '.env.dev'
    logger.info('Loading development environment variables')

exists = os.path.exists(dotenv_path)

if not exists:
    raise Exception('env files do not exist')

load_dotenv(dotenv_path)

PORT = os.environ.get('PORT')
PYTHON_ENV = os.environ.get('PYTHON_ENV')

IMAGES_PATH = os.environ.get('IMAGES_PATH')
BASIC_USERNAME = os.environ.get('BASIC_USERNAME')
BASIC_PASSWORD = os.environ.get('BASIC_PASSWORD')
BASIC_AUTH_HEADER = os.environ.get('BASIC_AUTH_HEADER')