
#####################
# Fibonacci Numbers #
#####################

#naive, recursive

def fib(n):
    'n-th Fibonacci number'

    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

#memoized version

def memfib(n):
    'n-th Fibonacci number'

    return memfib_r({0:0, 1:1}, n)

def memfib_r(T, n):
    'n-th Fibonacci number with memoized values T'

    if n in T:
        return T[n]
    else:
        T[n] = memfib_r(T, n-1) + memfib_r(T, n-2)
        return T[n]

#higher-order memoizer

def mem(f):
    'memoizer for f'

    T = {}

    def memf(x):

        if x in T:
            return T[x]
        else:
            y = f(x)
            T[x] = y
            return y

    return memf

#to memoize fib, we can use
#
#    fib = mem(fib)
#
#or in recent versions of Python,
#we can use decorators to
#apply higher-order function to function

@mem
def fib2(n):
    'n-th Fibonacci number'

    if n <= 1:
        return n
    else:
        return fib2(n-1)+fib2(n-2)


def fib_it(n):
    'n-th Fibonacci number'

    T = {0: 0, 1: 1}
    for i in range(2, n+1):
        T[i] = T[i-1] + T[i-2]
    return T[n]

def fib_it2(n):
    'n-th Fibonacci number'

    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b
    
    


#####################
# Text Segmentation #
#####################

words = open('words.txt', 'r').read().split()

def is_word(w):
    'is w in dictionary'

    return w in words

#Splittable(i): s[i:] can be split into list of words

def splittable(s):
    'can s be split into words?'

    split = {len(s): True}
    
    for i in range(len(s)-1, -1, -1):
        can_split = False
        for j in range(len(s), i, -1):
            if is_word(s[i:j]) and split[j]:
                can_split = True
        split[i] = can_split
    return split[0]

#challenges:
#- find actual segmentation
#- find all segmentations

def find_split(s):
    split = {0: True}
    sp = ""
    pos = 0
    for i in range(1, len(s)+1):
        split[i] = False
        for n in range(pos,i):
            if split[n] and is_word(s[n:i]):
                split[i] = True
                sp += s[pos:i] + ' '
                pos = i
                break
    print(sp)
    
#find_split('todayisfriday')






##################################
# Longest Increasing Subsequence #
##################################
nums = [7, 8, 1, 3, 9, 7, 5, 1, 9, 7, 4, 3, 6, 2, 7, 1, 3, 2, 4]

def lis_first(lst):
    'return length of longest increasing subsequence of lst'

    lis = {}
    for i in range(len(lst)-1, -1, -1):
        max_length = 0
        for j in range(i+1, len(lst)):
            if lst[j] > lst[i]:
                max_length = max(max_length, lis[j])
        lis[i] = 1 + max_length

    max_length = 0
    for i in range(len(lst)):
        max_length = max(max_length, lis[i])
    return max_length


#shorter variant, using some Python features
def lis_first2(lst):
    'return length of longest increasing subsequence of lst'

    lis = {}
    for i in range(len(lst)-1, -1, -1):
        lis[i] = 1+max([0]+[lis[j] \
                        for j in range(i+1, len(lst)) \
                        if lst[j] > lst[i]])
    return max(lis.values())

def word_chain(lst):
    'this is different from original submitted solution
    if not lst:
        print('list is empty')
        return
    l = len(lst)
    lis = [0]*l
    for i in range(l):
        #print(i, len(lst[i-1])-1)
        if i == 0:
            lis[i] = 1
        count = 1
        for n in range(i+1, l-1):
            while n < l:
                if lst[n][0] == lst[i][len(lst[i])-1]:
                    count += 1 
                    lis[n] = count
                    break
                if n == 0:
                    lis[i] = 1
##        else:
##            if lst[i][0] == lst[i-1][len(lst[i-1])-1]:
##                lis[i] = 1 + lis[i-1]
    #print(lis)
    return max(lis)
                                
text = ['fax', 'dowser', 'rogue', 'buddy', 'eel', 'yarn', 'elven', 'rocky', 'spoonerisms', 'premise',
'conflicts', 'compacter', 'backwood', 'rubbly', 'groat', 'nights', 'swapped', 'eagle', 'dilapidated',
'break', 'simple']
#s = word_chain(text)
#print(s)


    
#################
# Edit Distance #
#################


# since Python is 0-based we use
# a slightly modified definiton of edit(i,j)
#
# ed(i,j) := edit distance between
#            s[0:i+1], and t[0:j+1]
#
# base cases will then be ed(i,-1)
# and ed(-1,j)

def print_tab(ed,s,t):
    'print edit distance tableau for s and t'

    fmt = (len(t)+3)*(' {:>'+str(max(2, len(str(len(s))), \
                                    len(str(len(t)))))+'} ')

    tab = []
    tab.append([str(item) for item in ['', ''] + list(range(-1,len(t)))])
    tab.append([str(item) for item in ['', '', ''] + list(t)])
    for i in range(-1, len(s)):
        tab.append([str(item) for item in \
                    [i, (s[i] if i >= 0 else '')]+ \
                    [ed[(i,j)] for j in range(-1, len(t))]])
    for row in tab:
        print(fmt.format(*row))
       
def edist(s, t, outp = False):
    'calculate the edit distance between s and t'

    ed = {(-1,-1) : 0}
    for i in range(len(s)):
        ed[(i,-1)] = i+1
    for j in range(len(t)):
        ed[(-1,j)] = j+1
    for i in range(len(s)):
        for j in range(len(t)):
            ed[(i,j)] = min(ed[i,j-1]+1, \
                            ed[i-1,j]+1, \
                            ed[i-1,j-1]+ \
                            (1 if s[i] != t[j] else 0))
            
    if outp:
        print_tab(ed, s, t)

    return ed[(len(s)-1, len(t)-1)]


def shared_DNA(s,t): 
    # find the length of the strings 
    length1 = len(s) 
    length2 = len(t) 
  
    # declaring the 2D array for storing the dynamic programming values 
    table = [[None]*(length2+1) for i in range(length1+1)] 
  
    #inserts all values into 2D array
    for i in range(length1+1): 
        for j in range(length2+1): 
            if i == 0 or j == 0 : 
                table[i][j] = 0
            elif s[i-1] == t[j-1]: 
                table[i][j] = table[i-1][j-1]+1
            else: 
                table[i][j] = max(table[i-1][j] , table[i][j-1]) 
  
    # table[length1][length2] contains the length of shared_DNA of s[0..length1] & t[0.length2] 
    return table[length1][length2] 



##############
# Subset Sum #
##############


def sub_sum(X, tar):
    'given list of integers X, does it have a subset summing to tar'
    

    X_max_sum = sum([abs(x) for x in X])
    n = len(X)

    ss = {}
    for t in range(-X_max_sum, X_max_sum+1):
        ss[(n, t)] = (t == 0)
    for i in range(n-1,-1,-1):
        for t in range(-X_max_sum, X_max_sum+1):
            if -X_max_sum <= t-X[i] <= X_max_sum:
                ss[(i, t)] = ss[(i+1, t)] or \
                             ss[(i+1, t-X[i])]
            else:
                # t-X[i] is out of bounds,
                # so ss[(i+1, t-X[i])] is not
                # defined, but would have to be False
                # so can simplify formula
                ss[(i, t)] = ss[(i+1, t)]

    if (0,tar) in ss:
        return ss[(0,tar)]
    else:
        return False

#####################################
# Maximum Independent Set of a Tree #
#####################################

#the third, optional, parameter mis handles the memoization

def MIS(T, root, mis = {}):
    'maximum independent set of rooted tree T'

    if root not in T:
        mis[root] = 1
        return 1

    MISworoot = 0 #MIS without root
    MISwroot = 1  #MIS with root
    for u in T[root]: #children
        MISworoot += MIS(T, u, mis)
        if u in T: #u has children
            for v in T[u]: #grandchildren
                MISwroot += MIS(T, v, mis)
                
    mis[root] = max(MISworoot, MISwroot)
    return mis[root]

#sample tree, rooted at 0

T = {0: [1, 2, 3], 1:[4,5], 2:[6,7,8], 3:[9],\
     5: [10,11,12,13], 7:[14,15], 8:[16], \
     9:[17,18,19], 17:[20,21]}



