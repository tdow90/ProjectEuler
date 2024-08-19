# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_divisible_by(x):
    num = 1
    check = False
    i=1
    while check == False:
        while i <= x:
            if num%i == 0:
                i+=1
            else:
                num+=1
                i=1
        print(num)
        check = True
    

is_divisible_by(20)

        
     
        
        
