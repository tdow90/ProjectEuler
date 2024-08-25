#find the sum of all the primes below 200000

require 'prime'

def sum_of_primes(x)
  list_of_primes = []
  (0..x).each do |num|
    if num.prime?
      list_of_primes.append(num)
    end
  end
  sum_list_of_primes = list_of_primes.sum
  puts sum_list_of_primes
end



sum_of_primes(2000000)
