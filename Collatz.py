#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

global d    # create dictionary for cache
d = {}

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    assert type(i) is int    # check pre-conditions
    assert type(j) is int

    assert i > 0             # check argument validity
    assert i < 1000000
    assert j > 0
    assert j < 1000000
    if i > j:
        temp = i
        i = j
        j = temp
    assert i <= j

    mlen = 0                    # max length
    clen = 1                    # current length
    for x in range(i, j+1):
        tmp = x
        while x > 1:
            if x in d:          # if possible, use existing values already in dictionary
                clen = clen + d[x] - 1
                x = 1
            else:               # take a step
                if x%2 == 0:
                    x = x >> 1
                    clen += 1
                else:
                    x = x + (x >> 1) + 1
                    clen += 2
        if tmp not in d:        # add new values to dictionary
            d[tmp] = clen
        if clen > mlen:        # update max length
            mlen = clen
        clen = 1

    assert mlen > 0            # check post-conditions
    assert type(mlen) is int

    return mlen                # check return-value validity

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
