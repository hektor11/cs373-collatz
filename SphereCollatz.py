#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

#-------------
#imports
#-------------
import sys

#-------------
#over_flow
#-------------

def over_flow(n):
    if(n > 2147483647):
        n = n % 2147483647
    return n


# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# cycle_length
# ------------

def cycle_length(n):
    assert n > 0
    global cache
    
    c = 1
    idx = n
    while (n > 1):
        # n is in cache
        if (n < 1000001) and (cache[n] != 0):
            c += cache[n] - 1
            n = 1
        else:
            if(n & 1) == 0:
                n = over_flow(n >> 1)
                c += 1
            else:
                n = over_flow(n + (n >> 1) + 1)
                c += 2

    assert c > 0
    if(idx < 1000001):
        cache[idx] = c
    return c

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i > 0 and i < 1000000
    assert j > 0 and j < 1000000

    #Check if range is not from least to greatest
    if(i > j):
        temp = i
        i = j
        j = temp

    #Optimize by reducing the range 
    m = (j >> 1) + 1
    if(i < m):
        i = m

    max = 1
    curr = 1
    for x in range(i,j+1):
        curr = cycle_length(x)
        if(curr > max):
            max = curr

    assert max > 0
    return max


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

# ----
# main
# ----

global cache
cache = [0] * 1000001

#precompute values
for x in range(1,10001):
    cache[x] = cycle_length(x)

collatz_solve(sys.stdin, sys.stdout)


