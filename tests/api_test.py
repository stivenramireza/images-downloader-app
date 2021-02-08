from fastapi.testclient import TestClient
from src.secrets import BASIC_AUTH_HEADER
from src.api import app

client = TestClient(app)

images = [
    {
        "image_id": 100, 
        "resource": "https://pikwizard.com/photos/71c820cabadce0681a690d1f8c037732-m.jpg"
    }, 
    {
        "image_id": 100, 
        "resource": "https://pikwizard.com/photos/ea4fd6f25a43338fddde688136e87497-m.jpg"
    },
    {
        "image_id": 200,
        "resource": "https://pikwizard.com/photos/2589a1e71af3179ab26650de5bc67466-m.jpg"
    },
    {
        "image_id": 200,
        "resource": "https://pikwizard.com/photos/f5b20b453a4b8598022740d6f91c7952-m.jpg"
    },
    {
        "image_id": 200,
        "resource": "https://pikwizard.com/photos/bcb07f16924e72c3a0f784717dcb56c6-m.jpg"
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
                "resource": "9d1bd11d056b0caa086dd20684d15b10.jpg"
            },
            {
                "image_id": 100,
                "resource": "41b084900060d194256f0d4474410f5d.jpg"
            },
            {
                "image_id": 200,
                "resource": "a6c9a104e4fa4c68eeaa42bf0820eea5.jpg"
            },
            {
                "image_id": 200,
                "resource": "041ba19d096da343f6566a4b468d7266.jpg"
            },
            {
                "image_id": 200,
                "resource": "71f29d7768dc1c6a390a37b24ab6a4c2.jpg"
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