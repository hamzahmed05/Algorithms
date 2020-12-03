#you may have to install some
#of these libraries first
#pip install matplotlib
#pip install networkx

import matplotlib.pyplot as plt
import networkx as nx

#####################
# Wolf/Goat/Cabbage #
#####################

#showing all solutions
def WGCsolve():
    'build and draw Wolf,Goat,Cabbage Graph'

    G = nx.Graph()

    for vx in range(8):
        G.add_node(vx)
    
    labels = {0:'WGC', 1: ' GC', 2: 'W C',\
              3:'WG ', 4: 'W  ', 4: ' G ',\
              5:' G ', 6: '  C', 7: '---'}
    G.add_edges_from([\
        (0,2),(1,5),(2,1),(2,3),\
        (3,5),(5,7)])

    ct = 1
    for path in nx.all_simple_paths(G, 0, 7):
        print('Solution {}'.format(ct))
        for vx in path:
            print('Left bank: {}'.format(labels[vx]))
        ct += 1

#################
# Binary Search #
#################

#- not in-place
#  requires Theta(n) additional space
#  (lst[:mid], and lst[mid+1:] require copies of lst)

def bfind_bk(lst, x):
    'binary search for x in lst[i:j]'

    if len(lst) == 0:
        return False #x not found
    mid = len(lst)//2
    if x == lst[mid]:
        return True
    elif x < lst[mid]:
        return bfind_bk(lst[:mid], x)
    else:
        return bfind_bk(lst[mid+1:], x)

#Second solution
#- in-place, no additional space

def bfind(lst, x):
    'binary search for x in sorted lst'
    
    return bfind_r(lst, x, 0, len(lst))

#remember that in Python lst[i:j] excludes lst[j]
def bfind_r(lst, x, i, j):
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
    
###################
# Towers of Hanoi #
###################

def hanoi(n):
    'solve towers of hanoi with n disks'

    hanoi_r(n,0,2)

def hanoi_r(n,a,b):
    'moves n disks from peg a to peg b'

    if n == 0:
        return
    c = 3-a-b #trick: a+b+c = 3
    hanoi_r(n-1, a, c)
    print('Move disk from {} to {}'.format(a,b))
    hanoi_r(n-1, c, b)


def c_hanoi(n):
    'circular towers of hanoi with n disks'
    hanoi_c(n, 0,2)


def hanoi_c(n,src,dst):
    'moves n disks from peg a to peg b'

    if n == 0:
        return
    hlp = 3-src-dst #trick: a+b+c = 3
    

    
    if n ==1: 
        print('Move disk from {} to {} '.format(src, hlp))
        print('Move disk from {} to {} '.format(hlp, dst))
    
    hanoi_c(n-1, src, hlp, dst)
    #print('Move disk from {} to {} '.format(src, hlp))
    hanoi_c(n-1, dst, hlp, src)

    
    #hanoi_c(n-1, dst, hlp, src)
#hanoi(2) 

    


#############
# Mergesort #
#############

#Solution is not in-place, much harder to do so
inv =0
def merge(L, R):
    'merge two sorted lists L and R into one sorted list'
    i, j = 0, 0
    global inv
    out = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            out.append(L[i])
            i += 1
        else:
            inv +=len(L) - i
            out.append(R[j])
            j += 1
    if i == len(L):
        out += R[j:]
    else: #j == len(R)
        out += L[i:]
    
    return out

def mergesort(lst):
    'mergesort lst'

    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    L = mergesort(lst[:mid])
    R = mergesort(lst[mid:])
    return merge(L,R)


#############
# Quicksort #
#############

#first version (book version)
#- not in-place
#- using Lomuto partitioning

def partition_bk(lst, pos):
    'partition lst with respect to pivot in position pos'

    #ensure pivot is in final position (j-1)
    lst[-1], lst[pos] = lst[pos], lst[-1]
    p = -1
    for k in range(len(lst)-1):
        if lst[k] < lst[-1]:
            p += 1
            lst[k], lst[p] = lst[p], lst[k]
    p += 1
    lst[-1], lst[p] = lst[p], lst[-1]
    return p

def qs_bk(lst):
    'quicksort lst'

    if len(lst) <= 1:
        return lst
    piv = len(lst)//2
    part = partition_bk(lst, piv)
    L = qs_bk(lst[:part])
    R = qs_bk(lst[part+1:])    
    return L + [lst[part]] + R

#second version
#- in-place
#- using Lomuto partitioning

def partition(lst, i, j, pos):
    'partition lst[i:j] with respect to pivot in position pos'

    #ensure pivot is in final position (j-1)
    lst[j-1], lst[pos] = lst[pos], lst[j-1]
    p = i-1
    for k in range(i, j-1):
        if lst[k] < lst[j-1]:
            p += 1
            lst[k], lst[p] = lst[p], lst[k]
    p += 1
    lst[j-1], lst[p] = lst[p], lst[j-1]
    return p

def qs_r(lst, i, j):
    'recursively quicksort lst[i:j]'
    
    if j <= i+1: #at most one element
        return
    piv = (i+j)//2
    part = partition(lst, i, j, piv)
    qs_r(lst, i, part)
    qs_r(lst, part+1, j)

def qs(lst):
    'quicksort lst'

    qs_r(lst, 0, len(lst))

###############
# QuickSelect #
###############

#first solution
#- close to book
#- not in-place

#Challenge: can you adjust the code
#from k being 0-based to 1-based?
    
def quick_select_bk(lst, k):
    'find k-th element in lst, with k = 0 being first'

    if len(lst) == 1:
        return lst[0]
    else:
        piv = len(lst)//2
        part = partition_bk(lst, piv)

        if k < part:
            return quick_select_bk(lst[:part], k)
        elif k > part:
            return quick_select_bk(lst[part+1:], k-part-1)
        else:
            return lst[part]

#second solution
#- in-place version of quick-select
        
def quick_select_r(lst, i, j, k):
    'find k-th element in lst[i:j], with k = 0 being first'

    if j == i+1: #one element, lst[i] left
        return lst[i]
    else:
        piv = (i+j)//2
        part = partition(lst, i, j, piv)

        if k < part:
            return quick_select_r(lst, i, part, k)
        elif k > part:
            return quick_select_r(lst, part+1, j, k)
        else:
            return lst[part]

def quick_select(lst, k):
    'find k-th element in lst, with k = 0 being first'

    return quick_select_r(lst, 0, len(lst), k) 
    
############################
# Selection in Linear Time #
############################

#MedianOfFive is a bit of a cheat
#can be done using at most 6 comparisons in the worst case

def MedianOfFive(lst):
    'find median of five element list'

    lst.sort() 
    return lst[2]

#Challenge: rewrite to work in place (not trivial)
    
def mom_select_bk(lst, k):
    'return k-th smallest element of lst, with k = 0 being first'

    n = len(lst)
    if n <= 25:
        lst.sort()
        return lst[k]
    else:
        m = (n+4)//5 # = ceil(n/5), but avoiding float arithmetic
        M = []
        for i in range(m-1):
            M.append(MedianOfFive(lst[5*i:5*(i+1)]))
        mom_val = mom_select_bk(M, m//2)
        mom_pos = lst.index(mom_val)
        part = partition_bk(lst, mom_pos)
        if k < part:
            return mom_select_bk(lst[:part], k)
        elif k > part:
            return mom_select_bk(lst[part+1:], k-part-1)
        else:
            return lst[part]


def lstmaker(n):
    lst1 = [0] * n
    for i in range(n, 1):
        lst1[i] = n
    return lst1

import timeit
def numInv(lst):
    l = len(lst)
    count = 0

    for i in range(l):
        for j in range(i+1, l):
            if (lst[i] > lst[j]):
                count += 1
    return count
#lst1 = lstmaker(10000)

def timing():
     start = timeit.default_timer()
     numInv(lst1)
     stop = timeit.default_timer()
     print('Time: ', stop - start) 



'''def openfile():
    fil = open('longlist.txt')
    o = int(fil.read())
    newlst = o.split(",")
  
    

    fil.close()'''
#timing()
#arr = [1,20,6,4,5]
#arr = [10,9,8,7,6,5,4,3,2,1]

#mergesort(lst)
#mergesort(arr)
#print(inv)

#print(numInv(arr))


c_hanoi(1)
#hanoi(2)
#hanoi(2)
