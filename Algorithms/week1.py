def gcd(a,b):
    'greatest common divisor of a, b >= 0'

    #print(a,b) #uncomment to see a,b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


#Travelling Salesperson Problem
#pseudo-code (Python style) for nearest
#neighbor heuristic
#
#we assume that pointset P has
#method P.pop_close(p) that pops
#the closest point to p in P

'''
def TSP(P):
    'using nearest neighbor heuristic'

    p = P.pop()
    tour = [p]
    while |P| >= 1:
        q = P.closest(p) #closest point
                         #in P to p
        tour.append(q)
        p = q
    return tour
'''

#following algorithm for gcd is "correct"
#technically speaking, it just does
#not terminate on all inputs

def gcd_bad(a,b):
    'greatest common divisor of a, b >= 0'    

    if b == 0:
        return a
    else:
        return gcd_bad(a,b)


#the maximum of an empty
#list is negative infinity
#(because it is the neutral
#element of taking the max of
#two values)
    
def maximum(lst):
    'find maximum of lst'

    max_val = -float('inf')
    for i in range(len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
    return max_val

#same function annotated for
#correctness proof
#using loop invariant
#max_val = max(lst[0], ..., lst[i-1])

def maximum(lst):
    'find maximum of lst'

    max_val = -float('inf')
    for i in range(len(lst)):
        #max_val =
        #   max(lst[0], ..., lst[i-1])
        if lst[i] > max_val:
            max_val = lst[i]
    #i = len(lst) and
    #max_val = max(lst[0], ..., lst[i-1])
    #so
    #max_val = max(lst[0], ..., lst[len(lst)-1])
    #        = max(lst)
    return max_val

#iterative version of gcd
#avoiding recursion

def gcd(a,b):
    'greatest common divisor of a, b >= 0'

    while b > 0:
        a, b = b, a%b
    return a

#to state the loop invariant cleanly
#variables renamed
def gcd(a_in,b_in):
    'greatest common divisor of a, b >= 0'

    a,b = a_in, b_in
    while b > 0:
        #gcd(a_in, b_in) = gcd(a,b)
        a, b = b, a%b
    #b = 0 (assuming b >= 0)
    #so gcd(a_in, b_in) = gcd(a,b) =
    #                   = gcd(a,0)
    #                   = a
    return a

def find(lst, x):
    'find index i of x in lst'
    
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1 #x not found in lst

from time import time

#how long does it take to perform n passes on average

def ops(n):
    'average time for a single operation'
    
    t_start = time()
    for i in range(n):
        pass
    t_end = time()
    return ((t_end-t_start)/n)


#you may have to install some
#of these libraries first
#pip install matplotlib
#pip install networkx

import matplotlib.pyplot as plt
import networkx as nx

def WGC():
    'build and draw Wolf,Goat,Cabbage Graph'

    G = nx.Graph()

    for vx in range(16):
        G.add_node(vx)
    
    #labels = {0:'WGC', 1: ' GC', 2: 'W C',\
     #         3:'WG ', 4: 'W  ', 4: ' G ',\
      #        5:' G ', 6: '  C', 7: '---'}
    labels = {0:'0000', 1: ' 0001', 2: '0010',\
              3:  '0011', 4: '0100', 5: '0101',\
              6:' 0110', 7: '0111', 8: '1000', 9: '1001', 10: '1010',\
              11: '1011', 12: '1100', 13: '1101', 14:'1110', 15: '1111'}
   #"""  G.add_edges_from([\
    #    (0,2),(1,5),(2,1),(2,3),\
     #   (3,5),(5,7)]) """
    G.add_edges_from([\
        (0,12),(0,6),(0,3),(1,13),(1,7),(1,2),\
        (2,14),(2,4),(2,1),
        (3,15),(3,5),(3,0),\
        (4,8),(4,2),(4,7),\
        (5,9),(5,3),(5,6),\
        (6,10),(6,0),(6,5),\
        (7,11),(7,1),(7,4),\
        (8,4),(8,14),(8,11),\
        (9,5),(9,15),(9,10),\
        (10,6),(10,12),(10,9),\
        (11,7),(11,13),(11,8),\
        (12,0),(12,10),(12,15),\
        (13,1),(13,11),(13,14),\
        (14,2),(14,8),(14,13),\
        (15,3),(15,9),(15,12)]) 
    #pos = nx.spring_layout(G)
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos,labels,font_size = 20)

    plt.show() # to display graph

#for running time examples

def f1(n):
    'linear'

    print('Hello')
    print('Here are the numbers')
    print('From one to')
    print(n)
    
    for i in range(n):
        print(i)

def f2(n):
    'quadratic'

    for i in range(n):
        for j in range(n):
            print(i,j)

def f3(n):
    'mystery'

    for i in range(n):
        for j in range(j,n):
            print(i,j)

def f4(n):
    'cubic'

    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)

from itertools import permutations

def f5(n):

    for p in permutations(range(n)):
        print(p)

def add(x,y):
    'add x and y (strings representing integers)'

    xlst = [eval(d) for d in x]
    ylst = [eval(d) for d in y]

    nx, ny = len(xlst), len(ylst)

    if nx < ny:
        nx, ny = ny, nx
        xlst, ylst = ylst, xlst
    #so nx >= ny

    zlst = []
    carry = 0
    for i in range(-1,-nx-1,-1):
        if -i >= ny+1:
            digitsum = xlst[i] + carry
        else:
            digitsum = xlst[i] + ylst[i] + carry
        digit = digitsum % 10
        carry = digitsum // 10
        zlst.append(digit)
    if carry > 0:
        zlst.append(carry)
    return ''.join([str(d) for d in zlst[::-1]])

def bfind(lst, x):
    'binary search for x in sorted lst'
    
    return bfind_h(lst, x, 0, len(lst))

#remember that in Python lst[i:j] excludes lst[j]
def bfind_h(lst, x, i, j):
    'binary search for x in lst[i:j]'

    if j <= i:
        return -1 #x not found
    mid = (i+j)//2
    if x == lst[mid]:
        return mid
    elif x < lst[mid]:
        return bfind_h(lst, x, i, mid)
    else:
        return bfind_h(lst, x, mid+1, j)


# Starting script here
WGC()
