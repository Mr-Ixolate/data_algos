def intersection(first:list,second:list) -> list:
    output = []
    for i in range(0,max(*first,*second)+1):
        if i in first and i in second:
            output.append(i)
    return output

test1 = intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
test2 = intersection([2,4,6], [4,2]) # -> [2,4]
test3 = intersection([4,2,1], [1,2,4,6]) # -> [1,2,4]
test4 = intersection([0,1,2], [10,11]) # -> []

#a = [ i for i in range(0, 50000) ]
#b = [ i for i in range(0, 50000) ]
#test5 = intersection(a, b) # -> [0,1,2,3,..., 49999]

print(test1,test2,test3,test4)