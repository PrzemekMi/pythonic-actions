""" example python file which doesn't do anything specific """

import platform
import pandas as pd

if __name__ == '__main__':
    print(f"CI platform info {platform.platform()}")
    print(f"Pandas version {pd.__version__}")
