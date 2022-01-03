import requests

from config import Config


def get_image(num: int) -> None:
    res = requests.get(f"{Config.BASE_URL}/{Config.IMAGE_API}/{num}")
    if res.status_code == 200:
        with open(f"{Config.IMAGE_PATH}/{num:05}.png", "wb") as f:
            f.write(res.content)


def get_chart(num: int) -> None:
    res = requests.get(f"{Config.BASE_URL}/{Config.CHART_API}/{num}")
    if res.status_code == 200:
        with open(f"{Config.CHART_PATH}/{num:05}.png", "wb") as f:
            f.write(res.content)
