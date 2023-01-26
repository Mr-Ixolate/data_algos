def paired(numbers:list,target:int) -> tuple:
    for i,num in enumerate(numbers):
        pair = target - num
        numbers[i]=str(num)
        if pair in numbers:
            output = (i,numbers.index(pair))
            return output

print(paired([3, 2, 5, 4, 1], 8))# -> (0, 2)
print(paired([4, 7, 9, 2, 5, 1], 5))# -> (0, 5)
print(paired([9, 9], 18))# -> (0, 1)
print(paired([0, 1, 4, 9, 12, 2, 5], 17))# -> (4, 6)
print(paired([6, 4, 2, 8],12))# -> (1,3)