# Importing Dependencies
import pandas as pd
import numpy as np
from pull_stock import get_stock_data

if __name__ == '__main__':
    print(get_stock_data("RELIANCE.NS"))