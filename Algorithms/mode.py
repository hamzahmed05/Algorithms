def mode(list):
    
    table = {}
    answer = []
    maxCount = 1
    count= 0

    for x in list:
        if x not in table:
            table[x] = 1
        else:
            table[x] +=1
            if table[x] >= maxCount:
                maxCount = table[x]

    for z in table:
        if table[z] == maxCount:
            answer.append(z)    
    #print(answer)
    return(answer)

        
            
mode([5,2,6,2,5,3])






