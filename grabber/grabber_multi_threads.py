import glob
import time
from concurrent.futures import ThreadPoolExecutor
from os import cpu_count, remove

from config import Config
from utils import get_chart, get_image

N_TIMES = 1000


def main() -> None:
    # usunięcie ewentualnych poprzenich plików
    for f in glob.glob(f"{Config.IMAGE_PATH}/*.png"):
        remove(f)

    for f in glob.glob(f"{Config.CHART_PATH}/*.png"):
        remove(f)

    num_cores = cpu_count()
    id_list = list(range(N_TIMES))

    # obrazki
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=num_cores) as executor:
        result = executor.map(get_image, id_list)
    elapsed_time = time.time() - start_time
    print(
        f"Pobranie obrazków: {elapsed_time:.3f}s, średnio {N_TIMES/elapsed_time:.3f}/s"
    )

    # wykresy

    start_time = time.time()
    with ThreadPoolExecutor(max_workers=num_cores) as executor:
        result = executor.map(get_chart, id_list)
    elapsed_time = time.time() - start_time
    print(
        f"Pobranie wykresów: {elapsed_time:.3f}s, średnio {N_TIMES/elapsed_time:.3f}/s"
    )


if __name__ == "__main__":
    main()
