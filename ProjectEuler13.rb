#need to get first 10 digits of a larger sum(sum.txt) in Ruby.

def big_sum(file)
  sum_file = file
  sum = 0
  File.foreach(sum_file) do |line|
    sum+=line.to_i
  end
  sum_str = sum.to_s
  puts sum_str[0...10]
end

big_sum('sum.txt')
