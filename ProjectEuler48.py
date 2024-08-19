#Find the last ten digits of the SUM of i^i

def find_last_ten_of_sum(x):
    sum = 0
    i=1
    while i <= x:
        sum += (i**i)
        i+=1
    to_str = str(sum)
    length_to_str = len(to_str)
    last_ten_of_to_str = to_str[length_to_str-10:length_to_str]
    print(last_ten_of_to_str)

find_last_ten_of_sum(1000)