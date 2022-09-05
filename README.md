# Images Downloader App

FastAPI application to download thousands of images asynchronously in few minutes.

<p align="center">
<img src="https://media.springernature.com/original/springer-static/image/chp%3A10.1007%2F978-3-030-25943-3_34/MediaObjects/486223_1_En_34_Figa_HTML.png">
</p>

## Run API in development mode

    $ pip install -r requirements.txt
    $ export PYTHON_ENV=development
    $ uvicorn src.main:app --reload

## Run API in production mode

    $ docker build -t images-downloader:latest .
	$ docker-compose up -d
