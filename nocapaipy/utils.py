from time import sleep


def sleep(ms: int) -> None:
    sleep(ms / 1000)


def get_api_url(type: Union['free', 'pro']) -> str:
    return f'https://{type}.nocaptchaai.com/api/solve'