#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def dif_SqSum_minus_SumSq(val):
    sumSq = 0
    sum = 0
    for i in range(val + 1):
        sum = sum + i
        sumSq = sumSq + i**2

    diff = sum**2 - sumSq
    print(diff)

dif_SqSum_minus_SumSq(100)