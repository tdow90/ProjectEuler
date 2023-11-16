

def sum_of_multiples(num)
  i = 1
  sum = 0
    while i < num do
      if i%3==0 || i%5==0
        sum = sum + i
      end
      i+=1
    end
  puts sum
end

sum_of_multiples(1000)
