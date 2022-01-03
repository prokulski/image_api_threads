from dataclasses import dataclass


@dataclass
class Config:
    BASE_URL = "http://127.0.0.1:8000"
    IMAGE_API = "image"
    CHART_API = "chart"
    IMAGE_PATH = "images"
    CHART_PATH = "charts"
