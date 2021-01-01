#!/usr/bin/env python3
import random


def generate(*args):
    letters = "abcdefghijklmnopqrstuvwxyz"
    numb_symbs = "0123456789[]{}()*;/,._-"
    all = letters + letters.upper() + numb_symbs
    if len(args) != 0:
        length = args[0]
    else:
        length = 16
    password = ''.join([random.choice(all) for _ in range(length)])
    return(password)
