import glob
import time
from os import remove

from config import Config
from utils import get_chart, get_image

N_TIMES = 1000


def main() -> None:

    # usunięcie ewentualnych poprzenich plików
    for f in glob.glob(f"{Config.IMAGE_PATH}/*.png"):
        remove(f)

    for f in glob.glob(f"{Config.CHART_PATH}/*.png"):
        remove(f)

    # obrazki
    start_time = time.time()
    for i in range(N_TIMES):
        get_image(i)
    elapsed_time = time.time() - start_time
    print(
        f"Pobranie obrazków: {elapsed_time:.3f}s, średnio {N_TIMES/elapsed_time:.3f}/s"
    )

    # wykresy
    start_time = time.time()
    for i in range(N_TIMES):
        get_chart(i)
    elapsed_time = time.time() - start_time
    print(
        f"Pobranie wykresów: {elapsed_time:.3f}s, średnio {N_TIMES/elapsed_time:.3f}/s"
    )


if __name__ == "__main__":
    main()
