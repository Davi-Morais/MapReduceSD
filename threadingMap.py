import logging
import threading
from concurrent.futures import ThreadPoolExecutor
from os import listdir

from MapReduce import Map
from emit import deletar_intermediario


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    deletar_intermediario('./intermediario')


    arquivos = './arquivos'
    quantidade_arquivos = len(listdir(arquivos))

    # threads = list()
    # for index in range(quantidade_arquivos):
    #     logging.info("Main    : create and start thread %d.", index)
    #     x = threading.Thread(target=Map, args=("./arquivos/arquivo_teste{}.txt".format(index),))
    #     threads.append(x)
    #     x.start()

    # for index, thread in enumerate(threads):
    #     logging.info("Main    : before joining thread %d.", index)
    #     thread.join()
    #     logging.info("Main    : thread %d done", index)


    with ThreadPoolExecutor(max_workers=10) as executor:  # Defina o número máximo de threads conforme necessário
        for index in range(quantidade_arquivos):
            logging.info("Main    : create and start thread %d.", index)
            executor.submit(Map, "./arquivos/arquivo_teste{}.txt".format(index))

    logging.info("Main    : all threads are submitted")