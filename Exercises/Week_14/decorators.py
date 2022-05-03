from ast import Num
from datetime import datetime
from threading import Timer
from tkinter import N

def log(func) :
    def wrapper(*args) :
        f = open('log.txt', 'a')
        f.write(f'{datetime.now()}, {args}, {func(*args)}\n')
        return func(*args)
    return wrapper

@log
def add(*args):
    sum = 0
    for i in args:
        sum += i 
    return sum

@log
def printer(text) :
    print('From printer')



######################################
######## Exercise 1: Time it! ########
######################################

import time

def timeTaker(func) :
    def wrapper(*args, **kwargs) : 
        start = time.time()
        func(*args, **kwargs)
        end = (time.time()) - start
        print(f'Time elapsed: {end}')

    return wrapper    

@timeTaker
def generate_list(num) :
    [x for x in range(0,num)]


######################################
####### Exercise 3: Countdown ########
######################################

import time 

def slowDown(func) :
    def wrapper(n) :
        time.sleep(1)
        return func(n)
    return wrapper

@slowDown
def countDown(n) :
    if not n :
        print('Liftoff')
    else :
        print(n)
        return countDown(n-1)

slowDown(countDown(15))        