import tkinter as tk
import logging
from connectors.binance_futures import BinanceFuturesClient

logger = logging.getLogger()
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':

    binance = BinanceFuturesClient('19d62e5f771bef25adc1aa61b3ff5c516b9d63a243676e9aac6f350b7fbb2a94', 
    '28650dc71c844064032341f8e9d6802951045986f24d7f3a05baff570c979453', True)

    root = tk.Tk()
    root.mainloop()
