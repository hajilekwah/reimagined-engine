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
file_handler.setLevel(logging.INFO)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':

    binance = BinanceFuturesClient('', 
    '', True)
    print(binance.get_balances())
    # print(binance.place_order("BTCUSDT", "BUY", 0.01, "LIMIT", 20000, "GTC"))
    # order ID 2819190873 2819191303, 2819191461, 2819191442, 2819191423, 
    # print(binance.cancel_order("BTCUSDT", 2819191461))

    root = tk.Tk()
    root.mainloop()
