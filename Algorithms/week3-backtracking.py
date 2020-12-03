
####################
# n-queens problem #
####################

def print_chess(Q, n):
    'print queens in positions Q on nxn board'

    print((n+2)*'*')
    for i in range(n):
        print('*', end = '')
        for j in range(n):
            if Q[j] == i:
                print('Q', end = '')
            else:
                print(' ', end = '')
        print('*')
    print((n+2)*'*')

#modify code, so it counts number of solutions
    
def queens(n):

    queens_r({}, 0, n)

def queens_r(Q, k, n):
    '''place queen in k-th column of nxn board
    with previous placements Q'''

    if k == n:
        print_chess(Q,n)
        return
    else:
        for j in range(n):
            legal = True
            for i in range(k):
                if Q[i] == j or Q[i] == j+k-i or Q[i] == j-k+i:
                    legal = False
            #print(k,j,legal, Q)
            if legal:
                Q[k] = j
                queens_r(Q, k+1, n)


###########
# Notakto #
###########

def print_brd(brd, n):
    'print board'

    print((n+2)*'*')
    for i in range(n):
        print('*', end = '')
        for j in range(n):
            print(brd[n*i+j], end = '')
        print('*')
    print((n+2)*'*')

def done(brd, n):
    'does the nxn board contain 3-in a row/col/diag?'

    for i in range(n):
        if brd[i*n: (i+1)*n] == n*'x': #i-th row
            return True
        if brd[i:i+n**2:n] == n*'x': #i-th column
            return True

    d1,d2 = '', '' #main and second diagonal
    for i in range(n):
        d1 = d1 + brd[i*n+i]
        d2 = d2 + brd[(i+1)*n-i-1]
    if d1 == n*'x' or d2 == n*'x':
        return True
    
    return False

#Two player game, the players are 0 and 1

#first: determine whether there is a winning strategy for player 0

def notak(n):
    'does player 0 have a winning strategy for nxn Notakto?'


    brd = n**2*' '
    
    return notak_r(brd, n, 0)

def notak_r(brd, n, player):
    'does player have a win on nxn board brd?'

    #player has already won in current state
    if done(brd, n):
        #previous player completed 3 in row/col/diag
        #and lost
        return True
    #player has already lost in current state
    ### this does not occur in Notakto

    #recurse
    for i in range(len(brd)):
        if brd[i] == ' ': #legal move
            newbrd = brd[:i]+'x'+brd[i+1:]
            if not notak_r(newbrd, n, 1-player):
                return True
    return False

#Following is a playable version of Notakto
#with computer going first
#it only plays if it can win (so it won't play n = 4,
#n = 5 may blow time/memory
    
#Challenge:
#Extend the code, so you can play either player I or II
#(and the computer is the other player)
#so the computer needs to play even
#if it doesn't have a winning move
#(e.g. by picking a random legal move)

def play_notak(n):
    'play Notakto on nxn board against computer'

    brd = n**2*' '
    strat = play_notak_r(brd, n, 0)

    if (brd, 0) not in strat:
        print('I give up, you win')
        return

    state = (brd,0)
    while True:
        state = strat[state]
        if state == True:
            print('I win')
            return
        (brd, player) = state
        print_brd(brd, n)
        while True:
            move = eval(input('Your move (i,j): '))
            pos = n*move[0]+move[1]
            if brd[pos] != ' ':
                print('Illegal move')
            else:
                break
        
        brd = brd[:pos] + 'x' + brd[pos+1:]
        state = (brd, 0)
                

def play_notak_r(brd, n, player):
    'if exists return winning strategy for player in position brd'

    if done(brd, n):
        return {(brd, player): True}

    #recurse
    all_strat = {}
    for i in range(len(brd)):
        if brd[i] == ' ': #legal move
            newbrd = brd[:i]+'x'+brd[i+1:]
            strat = play_notak_r(newbrd, n, 1-player)
            if (newbrd, 1-player) not in strat:
                strat.update({(brd, player): (newbrd, 1-player)})
                return strat
            else:
                all_strat.update(strat)
    return all_strat


##############
# Subset Sum #
##############


def sub_sum(X, t):
    'is there a subset of X that sums up to t?'

    if len(X) == 0:
        return t == 0

    return sub_sum(X[1:], t) \
           or sub_sum(X[1:], t-X[0])

def find_sub_sum(X, t):
    'find subset of X that sums up to t'

    if len(X) == 0:
        if t == 0:
            return []
        else:
            return

    Xp = find_sub_sum(X[1:], t)
    if Xp != None:
        return Xp
    Xp = find_sub_sum(X[1:], t-X[0])
    if Xp != None:
        return [X[0]]+Xp
    return 


#####################
# Text Segmentation #
#####################
                
#words below is a global variable
#this is generally considered bad programming
#either go OO, or add words as an argument
#to following functions would be proper solution
                
words = open('words.txt', 'r').read().split()

def is_word(w):

    return w in words

def splittable(s):
    'can s be split into words?'

    return splittable_r(s, 0)

def splittable_r(s, i):
    'can s[i:] be split into words?'

    if i == len(s):
        return True #empty word
    for j in range(i+1, len(s)+1):
        if is_word(s[i:j]):
            if splittable_r(s, j):
                return True
    return False


#challenge: find all segmentations?

#find actual segmentation
def segment(s):
    'segment s into words'

    split = segment_r(s, 0)
    #print(split)
    if split != None:
        print([' '.join(split)])

def segment_r(s, i):
    'segment s[i:] into words'

    if i == len(s):
        return [] #empty list
    #for n in range(len(s)):
    for j in range(i+1, len(s)+1):
        if is_word(s[i:j]):
            split = segment_r(s, j)
            if split != None:
                return [s[i:j]] + split
    return 



def all_segments(s):
    'all segments s into words'

    splits = segments_c(s, 0)
    splitstring = []
    if len(splits) > 0:
        for split in splits:
            splitstring.append(' '.join(split))
    return splitstring
    
def segments_c(string, pos):
    
    if pos == len(string):
        return [[]] #empty list
    collect = []
    for j in range(pos+1, len(string) +1):
        if is_word(string[pos:j]):
           splits = segments_c(string, j)
           if len(splits) > 0:
               collect += [[string[pos:j]] + split for split in splits]
    return collect

text = 'hoorayitisfriday'
sumtext = 'whenlilacslastinthedooryardbloomed'
b = all_segments(text)
print(b)
#all_segments(sumtext)



    


from itertools import permutations
s = ['ACTGTAC', 'ACGCGAG', 'AGTTTGCGTG']
t = ['CAGAAGT', 'ATATC', 'ATTCT', 'TCCTAT', 'TAATCA', 'CTAAATA']
n = ['CCAC', 'TAAGCCC', 'CGGTCAGC', 'GCCAG', 'ACTGC', 'AGTCACG']


def bf_seq(p):
    if len(p) == 0:
        return ""
    perms = permutations(p)
    lst = []
    for perm in perms:
        legal = True
        for i in range(0,len(perm),len(perm)):
            if perm[i][-2:] != perm[i+1][:2]:
                legal = False
                break                    
    if legal == True:
        print('True')

bf_seq(n)

def seq(p):
    'function that checks if the subsequence list being passed is the orig seq'
    if not p[0]:
        print('False')
    m = seq_r(p, 0, p[0], len(p))  #passes p[0] as a string to evaluate later
    if m:   #if m is true
        print('True')
    else:
        print('False')

def seq_r(lst, pos, string, num):
    'checks if at the end of list'
    if pos +1 == num:
        return True
    secPos = 0
    key = string.rfind(lst[pos+1][secPos]) #finds last occurence of the 1st c 

    if key < 0:
        return False

    while key < len(lst[pos]) and pos+1 < num:
        #print(lst[pos][key], lst[pos+1][secPos])
        if lst[pos][key] != lst[pos+1][secPos]:
            return False
        key += 1
        secPos +=1
        
    return seq_r(lst, pos+1, lst[pos+1], len(lst)) 
#seq(s)
#l = ['ACCG', 'CGT', 'TAC']
#seq(l)

def find_seq(p):
    'checks if subseq being passed is orig seq and prints the orig seq' 
    if not p[0]:
        print('False')
    seqTracker = ""
    m = find_seq_r(p, 0, p[0], len(p), seqTracker) 
    print(seqTracker)
    if m:
        print('True')
    else:
        print('False')
    
def find_seq_r(lst, pos, string, num, origSeq):
    ''
    if pos+ 1 == num:
        #print(origSeq)
        origSeq += lst[pos]
        print(origSeq)
        return True
    secPos = 0
    key = string.rfind(lst[pos+1][secPos])
    tr = key
    #print(key)
    if key < 0:
        return False
    while key < len(string) and pos+1 < num:
        if lst[pos][key] != lst[pos+1][secPos]:
            return False
        #print(lst[pos][:key])
        #origSeq += lst[pos][:key]
        key += 1
        secPos +=1
    origSeq += lst[pos][:tr]
    return find_seq_r(lst, pos+1, lst[pos+1], len(lst), origSeq)

#find_seq(s)
    
##fileName = open("hw3-DNA.txt", "r")
##file = fileName.readlines()
##print(file)
#bf_seq(t)
                

##################################
# Longest Increasing Subsequence #
##################################

#challenge:
#modify code so it returns
#- one longest increasing subsequence
#- all longest increasing subsequences

def lis(lst):
    'return length of longest increasing subsequence of lst'

    max_length = 0
    for i in range(len(lst)):
        max_length = max(max_length, lis_r(lst, i))
    return max_length

def lis_r(lst, i):
    'length of LIS of lst starting with lst[i]'

    max_length = 1 #lst[i]
    for j in range(i+1, len(lst)):
        if lst[j] > lst[i]:
            new_length = lis_r(lst, j) + 1
            if new_length > max_length:
                max_length = new_length
    return max_length
            
#segment('wowthisiscrazy')
