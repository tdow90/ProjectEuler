from sympy import *
#Find the sum of all the primes below two million.

def sum_or_primes(x):
    list_of_primes = []
    for i in range(x):
        if isprime(i):
            list_of_primes.append(i)

    print(sum(list_of_primes))

sum_or_primes(2000000)
