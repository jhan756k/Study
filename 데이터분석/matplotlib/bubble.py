import numpy as np

def bubblelistsmall(getlist):
    for x in range(len(getlist)):
        if x == 0:
            pass

        if x != 0:
            if getlist[x] < getlist[x-1]:

                a = getlist[x]
                b = getlist[x-1]
                getlist[x-1] = a
                getlist[x] = b

def bubblelistbig(getlist):
    for x in range(len(getlist)):
        if x == 0:
            pass

        if x != 0:
            if getlist[x] > getlist[x-1]:

                a = getlist[x]
                b = getlist[x-1]
                getlist[x-1] = a
                getlist[x] = b


