#!/usr/bin/env python3
import random


def generate(*args):
    # var init
    letters = "abcdefghijklmnopqrstuvwxyz"
    numb_symbs = "0123456789[]{}()*;/,._-"
    all = letters + letters.upper() + numb_symbs
    # check for *args else go to default lenght
    if len(args) != 0:
        length = args[0]
    else:
        length = 16
    # generate and returns password
    password = ''.join([random.choice(all) for _ in range(length)])
    return(password)


print(generate())
