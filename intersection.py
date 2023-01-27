def intersection(first:list,second:list) -> list:
    output = []
    for i in range(0,max(*first,*second)+1):
        if i in first and i in second:
            output.append(i)
    return output

def intersection_conc(first,second):
    output = []
    [output.append(i) for i in range(0,max(*first,*second)+1) if i in first and i in second]
    return output

def intersection_better(first:list,second:list) -> list:
    output = []
    short = [*set(max(first,second,key=len))]
    long = [*set(max(first,second,key=len))]
    [output.append(i) for i in short if i in long and i not in output]
    return output

def intrsct(l1:list,l2:list) -> list:
    return [i for i in set(min(l1,l2,key=len)) if i in max(l1,l2,key=len)]

test1 = intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
test2 = intersection_conc([2,4,6], [4,2]) # -> [2,4]
test3 = intersection_better([4,2,1], [1,2,4,6]) # -> [1,2,4]
test4 = intrsct([0,1,2], [10,11]) # -> []

#a = [ i for i in range(0, 50000) ]
#b = [ i for i in range(0, 50000) ]
#test5 = intersection(a, b) # -> [0,1,2,3,..., 49999]

print(test1,test2,test3,test4)