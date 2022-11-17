import requests
from time import sleep
from typing import Dict, Union

from bs4 import BeautifulSoup

from .base import get_base64
from .images import get_images
from .target import get_target


def solve_captcha(page: BeautifulSoup, api_key: str, uid: str, type: Union['free', 'pro']) -> None:
    outer = page.find('iframe', attrs={'data-hcaptcha-response': True})
    if not outer:
        raise Exception('solveCaptcha: captcha outer frame not found')
    outer_frame = outer['src']

    inner = page.find('iframe', attrs={'data-hcaptcha-response': 'false'})
    if not inner:
        raise Exception('solveCaptcha: captcha inner frame not found')
    inner_frame = inner['src']

    checkbox = outer.find('div', id='checkbox')
    if checkbox['aria-checked'] == 'false':
        raise Exception('solveCaptcha: captcha already solved')

    response = requests.get(inner_frame)
    language = page.find('html').attrs.get('lang', 'en')
    sitekey = page.find('div', class_='h-captcha')['data-sitekey']
    images = get_images(response.text)
    target = get_target(response.text)

    response = requests.post(
        get_api_url(type),
        json={
            'softid': 'python-pkg',
            'method': 'hcaptcha_base64',
            'site': page.url,
            'ln': language,
            'sitekey': sitekey,
            'images': images,
            'target': target,
        },
        headers={
            'Content-type': 'application/json',
            'apikey': api_key,
            'uid': uid,
        }
    ).json()

    if response['status'] == 'solved':
        for item in response['solution']:
            image_elements[item].click()
            sleep(200)
    elif response['status'] == 'new':
        for _ in range(10):
            sleep(1000)
            result = requests.get(response['url']).json()
            if result['status'] == 'solved':
                for item in result['solution']:
                    image_elements[item].click()
                    sleep(200)
                break
    elif response['status'] == 'skip':
        raise Exception(response['message'])
    elif response['status'] == 'error':
        raise Exception(response['message'])
    else:
        raise Exception(response)