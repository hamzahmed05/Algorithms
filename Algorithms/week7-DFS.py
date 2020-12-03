#running time: O(V+E)
def rev(G):
    'reverse edges of G'

    revG = {}
    for u in G:
        revG[u] = []
    for u in G:
        for v in G[u]:
            revG[v].append(u)
    return revG

def DFS(G):
    'full DFS traversal of G'
    clock = 0
    marked = {}
    PG = {} #parent graph, with clock info
    for v in G:
        marked[v] = False
        PG[v] = [None, None, None] #pre, post, parent
    for v in G:
        if not marked[v]:
            clock = DFS_r(G, v, clock, marked, PG)
    return PG

def DFS_r(G, v, clock, marked, PG):
    'DFS of G starting at v'
    marked[v] = True
    clock += 1
    PG[v][0] = clock
    
    for w in G[v]:
        if not marked[w]:
            PG[w][2] = v #parent
            clock = DFS_r(G,w,clock, marked, PG)
    clock += 1        
    PG[v][1] = clock
    return clock

def is_cut(G, v):
    e = v
    marked = {}
    disc = {}
    low = {}
    AP ={}
    parent = {}
    count = 0
    for v in G: 
        marked[v] = False
        AP[v] = False
        parent[v] = -1

        
    for v in G:
        if not marked[v]:
            count = is_cut_r(G, v,disc, marked, low, parent, AP, count)
    
    if AP[e] == True:                
        print( 'True')
    else:
        print('False')            
def is_cut_r(G, v, disc, marked, low, parent, AP, count):
    marked[v] = True
    children = 0
    low[v] = count
    disc[v] = count
    count = count + 1

    for d in G[v]:
        if not marked[d]:
            parent[d] = v
            children += 1
            count = is_cut_r(G, d, disc, marked, low, parent, AP, count)

            low[v] = min(low[v], low[d])

            if children > 1:
                AP[v] = True
        elif d != parent[v]:
            low[v] = min(low[v], disc[d])
    return count
     



def prereqs():
    D = {}
    while True:
        try:
             a,b = input('requires, required: ').split(',')
             a = a.strip()
             b = b.strip()
        except:
            break
        if a in D:
            D[a].append(b)
        else:
            D[a] = [b]
        if b not in D:
            D[b] = []
    d = DFSprereqs(D)
 #   d = munnaDFS(D)    
    #d = DFS(D)
    return d

def DFSprereqs(G):
    marked = {}
    order = []
    checker = {}
    #parent graph, with clock info
    for v in G:
        marked[v] = False
        checker[v] = False
    for v in G:
        if acyclic(G,v, checker) == False:
            return False
        if not marked[v]:
            order = DFS_pre(G, v, marked, order, checker)
    
    
    return order
def acyclic(G,v, checker):
    checker[v] = True
    for w in G[v]:
        if checker[w] == True:
            #print(w, v)
            return False
        elif checker[v] == False:
            if acyclic(w) == True:
                return False
    return True
    
def DFS_pre(G, v, marked, order, checker):
    #print(order)
    marked[v] = True
    if len(G.get(v)) == 0:
        order.append(v)
        return order
    for w in G[v]:
        if marked[w]:
            #print(w)
            #checker = False
            return
        if not marked[w]:
            DFS_pre(G,w, marked, order, checker)
    order.append(v)
    return order
    

def undirect(G):
    revG = {}
    
    for u in G:
        revG[u] = []
    for u in G:
        for v in G[u]:
            if v not in revG:
                revG[v] = []
            revG[v].append(u)
            revG[u].append(v)
            
    return revG
    

#some sample graphs

#undirected graph for DFS
G1 = {0: [1, 3, 4, 6, 7], 1: [0, 4, 7, 9], 2: [3, 5, 6, 9],
     3: [0, 2, 7, 8], 4: [0, 1, 5], 5: [2, 4], \
     6: [0, 2, 8], 7: [0, 1, 3], 8: [3, 6], 9: [1, 2]} 


#tree from slides
T = {'a': ['b', 'c', 'd'],\
     'b': ['a', 'e', 'f'],\
     'c': ['a'],\
     'd': ['a', 'g'],\
     'e': ['b'],\
     'f': ['b'],\
     'g': ['d', 'h', 'i', 'j'],\
     'h': ['g'],\
     'i': ['g'],\
     'j': ['g']}
d = {0: [11, 12], 1:[2,8,10,11], 2: [8,10,11], 3: [6, 7, 8], 4: [5,6], 5: [6],
6: [7,8], 7: [8], 8: [10,11], 9: [10], 10: [11], 11: [12]} 
#top sort example
D = {0: [6], \
     1: [], \
     2: [], \
     3: [1], \
     4: [1,2,3], \
     5: [0,3], \
     6: [2]}

##def undirect(G):
##    PG = {}
##    for v in G:
##        PG[v] = []
##    for v in G:
##        for e in G[v]:
##            n = undirect_r(G,v,e, PG[v], PG)
##        #PG[v] = n
##    print(PG)
##
##def undirect_r(G,v,e, neighbors, PG):
##    if v not in G:
##        print(v)
##        PG[v] = []
##    neighbors.append(e)
##    for w in G[v]:
##        undirect_r(G, w, v, neighbors, PG)
##    print(neighbors)
##    return neighbors
