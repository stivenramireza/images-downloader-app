from fastapi.testclient import TestClient
from src.secrets import BASIC_AUTH_HEADER
from src.api import app

client = TestClient(app)

images = [
    {
        "image_id": 100, 
        "resource": "https://cdn.pixabay.com/photo/2014/02/27/16/10/tree-276014_960_720.jpg"
    }, 
    {
        "image_id": 150, 
        "resource": "https://cdn.pixabay.com/photo/2015/09/09/16/05/forest-931706_960_720.jpg"
    }, 
    {
        "image_id": 200, 
        "resource": "https://cdn.pixabay.com/photo/2015/06/19/21/24/the-road-815297_960_720.jpg" 
    }, 
    {
        "image_id": 250, 
        "resource": "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_960_720.jpg"
    }, 
    {
        "image_id": 300,
        "resource": "https://cdn.pixabay.com/photo/2015/12/01/20/28/road-1072823_960_720.jpg"
    }
]

def test_download_images():
    response = client.post(
        "/download",
        headers={
            "Cache-Control": "no-cache",
            "Content-Type": "application/json",
            "Authorization": f"Basic {BASIC_AUTH_HEADER}"
        },
        json={
            "images": images
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Images have been downloaded successfully",
        "images": [
            {
                "image_id": 100,
                "resource": "12cb5eb6f19cc393afa92efa43c915de.jpg"
            },
            {
                "image_id": 150,
                "resource": "84901b6ce4d9d19a26dc2b6651de3594.jpg"
            },
            {
                "image_id": 200,
                "resource": "1c861c8bf2530481963be6cf887664d2.jpg"
            },
            {
                "image_id": 250,
                "resource": "f9d276ffd376d268acffe66d3b88bd52.jpg"
            },
            {
                "image_id": 300,
                "resource": "0236bb405cafcdaac9ae53c37f832a9e.jpg"
            }
        ]
    }

def test_empty_images():
    response = client.post(
        "/download",
        headers={
            "Cache-Control": "no-cache",
            "Content-Type": "application/json",
            "Authorization": f"Basic {BASIC_AUTH_HEADER}"
        },
        json={
            "images": []
        }
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "There are not images to download"
    }

def test_bad_auth_header():
    response = client.post(
        "/download",
        headers={
            "Cache-Control": "no-cache",
            "Content-Type": "application/json",
            "Authorization": "Basic bnV0xdcafdssr0Kis="
        },
        json={
            "images": images
        }
    )
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid authentication credentials"
    }

def test_inexistent_auth_header():
    response = client.post(
        "/download",
        headers={
            "Cache-Control": "no-cache",
            "Content-Type": "application/json"
        },
        json={
            "images": images
        }
    )
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Not authenticated"
    }