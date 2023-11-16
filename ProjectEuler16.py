#What is the sum of the digits of the number 2^1000?

def sum_of_digits(num, exp):
    bigNum = num**exp
    bigNum_str = str(bigNum)
    sum = 0
    for i in range(len(bigNum_str)):
        temp = int(bigNum_str[i])
        sum = sum + temp
    print("The Sum of all of the digits for your number is " + str(sum) + "!")



sum_of_digits(2,1000)