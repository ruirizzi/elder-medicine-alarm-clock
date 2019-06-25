import logging
import threading
import time

def thread_function(name):
    time.sleep(2)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    x = threading.Thread(target=thread_function, args=(1,))
    x.start()
    # x.join()