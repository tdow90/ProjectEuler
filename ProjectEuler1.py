
# Problem 1 from projecteuler.net
def Multiple_of_3or5(limit):
    sum = 0
    for i in range(limit):
        if i%3==0 or i%5==0:
            sum = i + sum
    print(sum)

Multiple_of_3or5(10000)