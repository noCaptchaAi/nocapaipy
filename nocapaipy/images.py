from typing import Dict

import requests


def get_images(frame) -> Dict[int, str]:
    images = frame.find('div', class_='task-image')
    if not images:
        raise Exception('getImages: no images found')

    data = {}
    for index, img in enumerate(images):
        value = img.find('div', class_='image')['style']
        url = value.split('"')[1]
        data[index] = get_base64(url)

    return data