import time
import json
import requests
import numpy
from addict import Dict
from multiprocessing.pool import ThreadPool
import tkinter as tk
import tkinter.messagebox

_FINISH = False
pool = ThreadPool(processes=8)

def hang(i, j):
    while True:
        if _FINISH:
            break
        print('%d + %d is %d' % (i, j, i + j))
        time.sleep(1)
class champion:
    def __init__(self, name, key):
        self.name = name
        self.key = key

def main():
    '''
    with open('champion.json', encoding='utf-8') as cjs:
        champions = json.load(cjs)

    champs = {}
    for c in champions['data']:
        champs[champions['data'][c]['key']] = c

    for item in champs:
        print(item, champs[item])
    # f = open('champion.json', encoding='utf-8')
    # cf = Dict(f)
    '''
    
    global _FINISH
    global pool
    #pool.apply_async(hang)
    tmp = input()
    for i in range(8):
        pool.apply_async(hang, (i, i**i))
    while tmp != 'quit':
        if tmp == 'stop':
            _FINISH = True
            pool.terminate()
            pool.join()
        elif tmp == 'restart':
            i+=1
            pool = ThreadPool(2)
            _FINISH = False
            pool.apply_async(hang, (i,))
        tmp = input()
        
    print( 'main process exiting..')


if __name__ == '__main__':
    main()