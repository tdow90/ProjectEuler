# ProjectEuler.net Problem 2 in Ruby


def sum_of_even_fibonachi(val)
  sequence = [1, 2]
  sum = 0
  i = 1
  while sequence[i] < val do
    sequence.append(sequence[i]+sequence[i-1])
    if sequence[i].even?
      sum = sum + sequence[i]
    end
    i+=1
  end
  puts sum
end

sum_of_even_fibonachi(4000000)
