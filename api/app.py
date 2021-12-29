from io import BytesIO

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from PIL import Image, ImageDraw

import matplotlib.pyplot as plt

import matplotlib
# ważne - wykresy są generowane ale nie są pokazywane, oszczędzamy pamięć (i czas)
matplotlib.use('Agg')


app = FastAPI()


@app.get('/image/{num}')
async def get_image(num: int) -> StreamingResponse:
    """Metoda zwraca obrazek z wypisanym tekstem reprezentującym liczbę podaną jako parametr.

    Args:
        num (int): Liczba, która zostanie wypisana na obrazku

    Returns:
        StreamingResponse: obrazek w formacie PNG
    """
    img = Image.new('RGB', (350, 70), color=(51, 144, 255))
    canvas = ImageDraw.Draw(img)
    canvas.text((10, 10), str(num), fill='#FFFFFF')
    img_data = BytesIO()
    img.save(img_data, format='PNG')
    img_data.seek(0)
    return StreamingResponse(img_data, media_type="image/png")


@app.get('/chart/{num}')
async def get_chart(num: int) -> StreamingResponse:
    """Metoda zwraca wykres funkcji f(x)=x^2 dla wartości x z przedziału [0; num].
    Zwracany wykres jest obrazkiem w formacie PNG.

    Args:
        num (int): długość przedziału

    Returns:
        StreamingResponse: obrazek w formacie PNG
    """
    x = list(range(num))
    y = [xx**2 for xx in x]
    fig = plt.figure(figsize=(10, 5))
    plt.plot(x, y)
    plt.title(f'Wykres z {num=}')
    img_data = BytesIO()
    plt.savefig(img_data, format='png', dpi=90)

    # czyszczenie pamięci zajętej przez wykresy
    plt.close(fig)
    plt.cla()
    plt.clf()
    del fig

    img_data.seek(0)
    return StreamingResponse(img_data, media_type="image/png")
