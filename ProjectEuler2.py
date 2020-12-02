# ProjectEuler.net problem 2

def fib_sum_of_even_num(val):
    fib = [1, 2]
    i=1
    sum = 0
    while(fib[i]<=val):
        fib.append(fib[i]+fib[i-1])
        if fib[i]%2==0:
            sum = sum + fib[i]
        i = i+1
    print(sum)



fib_sum_of_even_num(40000000000000000000000000000000000000000)

