#!/usr/bin/env python3


# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# import
# ------------
import sys

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
# over_flow
# ------------

def over_flow(n):
    if (n > 2147483647):
        n = n - 2147483647
    return n

# ------------
# cycle_length
# ------------

def cycle_length(n):
    global CACHE
    global MAX_INT
    global mx
    global ovf
    assert n > 0
    c = 1
    temp = n

        
    while n > 1:
        n = over_flow(n)
        if(n > mx):
            ovf += 1
            mx = n


        if n in CACHE:
            c += CACHE[n] - 1
            n = 1
        else:
            if(n & 1) == 0:
                n = over_flow(n >> 1)
                c += 1
            else:
                n = over_flow(n + (n >> 1) + 1)
                c += 2
    assert c > 0
    CACHE[temp] = c
    return c
    '''
    if n == 1:
        return 1

    #In cache
    if n in CACHE:
        return CACHE[n]
    elif(n & 1) == 0:
        return cycle_length(n >> 1) + 1
                
    else:
        return cycle_length(n + (n>>1) + 1) + 2
        

   
    elif(n < 1000001):

        if(cache[n] != 0):
            return cache[n]

        elif(n & 1) == 0:
            cache[n] = cycle_length(n >> 1) + 1
            return cache[n]
                
        else:
            cache[n] = cycle_length(n + (n>>1) + 1) + 2
            return cache[n]
    
    #Not in cache          
    else:
        if(n & 1) == 0:
            return cycle_length(n >> 1) + 1
        else:
            return cycle_length(n + (n >> 1) + 1) + 2
    '''
    
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
    assert i > 0 and i < 1000000
    assert j > 0 and j < 1000000

    if(i >= j):
        temp = i
        i = j
        j = temp
    
    m = (j >> 1) + 1
    if i < m:
        i = m
    
    
    global CACHE
    curr = 1
    max = 1
    for x in range(i,j+1):
        #curr = cycle_length(x)
        #if(x < 100001) and ( cache[x] != 0):
        #    curr = cache[x]
        if x in CACHE:
            curr = CACHE[x]
        else:
            curr = cycle_length(x)
        if (curr > max):
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

# -------------
# main
# -------------

#global cache
#cache = [0] * 1000001

global CACHE
global MAX_INT
global mx
global ovf
mx = 0
ovf = 0
MAX_INT = 2147483647
value = 1
CACHE =  dict()
#CACHE[1] = 1

#precompute table

for x in range(1,1000001):
    #print('x is: ', x)
    if(x & 1) == 0:
        CACHE[x] = 1 + CACHE[x >> 1]
    elif(x % 8) == 5:
        CACHE[x] = 4 + CACHE[(3 * ((x-5) >> 3)) + 2]
    else:
        CACHE[x] = cycle_length(x)

#collatz_solve(sys.stdin, sys.stdout)
print(ovf)