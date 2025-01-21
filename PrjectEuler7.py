#what is the 10001 prime number?
def find_num_of_prime(x):
    list_of_primes = []
    i = 1
    while len(list_of_primes) < x:
        if isprime(i) == True:
            list_of_primes.append(i)
            i+=1
        else:
            i+=1
    print(list_of_primes[x-1])
    


find_num_of_prime(10001)


