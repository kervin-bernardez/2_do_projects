#!/usr/bin/env python3

import random


def generate():
    letters = "abcdefghijklmnopqrstuvwxyz"
    numb_symbs = "0123456789[]{}()*;/,._-"

    all = letters + letters.upper() + numb_symbs

    length = 16
    password = "".join(random.sample(all, length))
    return(password)


print(generate())
