import pandas as pd
import numpy as np

from datetime import datetime


def read_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


def read_npy(filename: str) -> pd.DataFrame:
    return pd.DataFrame(np.load(filename))


def save_csv(nd_data: np.ndarray):
    t_now = datetime.now()
    filename = t_now.strftime("%Y%m%d%H%M%S%f")
    np.savetxt("./temp/{}.csv".format(filename), nd_data, delimiter=",", fmt="%.10f")


if __name__ == "__main__":
    list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    arr = np.array(list)
    np.save("./temp/np_save", arr)
