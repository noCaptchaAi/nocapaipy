# nocapaipy
[BETA]: A python wrapper for NoCaptchaAI

## Installation

```bash
$ pip install git+https://github.com/noCaptchaAi/nocapaipy
```

## Usage

To use it in another script
```py
from nocapaipy import solve

params = {
    "images": {
        "0": "base64 hash from image",
        "1": "base64 hash from image",
        "...": "...",  # send totatl 18 images max;
        "18": "base64 hash from image",
    },
    "target": "Please click each image containing an airplane",
    "method": "hcaptcha_base64",
    "sitekey": "sitekey",
    "site": "website",
    "ln": "en",  # (Optional) language eg "ru" = Russain
    "softid":"softid assigned by noCaptchaAi" # (Optional) Please contact us for softid to get 5% usages fee from paid user.
}
print(solve(**params))
```

Another way to use it

```py
from nocapaipy import Nocapaipy

params = {
    "images": {
        "0": "base64 hash from image",
        "1": "base64 hash from image",
        "...": "...",  # send totatl 18 images max;
        "18": "base64 hash from image",
    },
    "target": "Please click each image containing an airplane",
    "method": "hcaptcha_base64",
    "sitekey": "sitekey",
    "site": "website",
    "ln": "en",  # (Optional) language eg "ru" = Russain
}
print(Nocapaipy(**params).solve())
```
