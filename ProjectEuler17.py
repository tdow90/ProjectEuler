from num2words import num2words

def find_num_of_letters(x):
    str = ''
    i = 1
    while i <= x:
        letter = num2words(i)
        str = str + letter
        i+=1
    #Need to remove the "-" for str
    str_no_dash = str.replace('-', '')
    #Need to remove the " " too
    str_no_dash_or_space = str_no_dash.replace(' ', '')
    print(len(str_no_dash_or_space))

find_num_of_letters(1000)
