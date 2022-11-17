import base64
import requests


def get_base64(url: str) -> str:
    response = requests.get(url)
    return base64.b64encode(response.content).decode()