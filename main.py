import threading
import logging
import time
# pip install pyinstaller

# pyinstaller main.py

i = 0


def thread_func(name, a, time_s):
    while True:
        global i
        i = i + a
        logging.info("Thread  start %s", name)
        time.sleep(time_s)
        logging.info("%s  %i", name, i)
        logging.info("Thread  stop %s", name)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("main start")
    x = threading.Thread(target=thread_func, args=(1, 1, 1))
    x2 = threading.Thread(target=thread_func, args=(2, 1, 2))

    x.start()
    x2.start()

    logging.info('main stop')
