#Find the sum of the digits in the number 100!

import math

def sum_fac(n): 
    sum = 0
    str_fac = str(math.factorial(n))
    for i in range(len(str_fac)):
        sum = sum + int(str_fac[i])
    print(sum)

 

sum_fac(100)