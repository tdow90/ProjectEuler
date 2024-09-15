#1. Make list into an array
#2. Sort by alphabetical order the array
#3. Take sortd array and calaculate the aphabetical value and create hash name => alphabetical value
#4. add up all the alphabetical values


def create_alphabet
  alphabet = []
  ('a'...'z').each do |letter|
    alphabet.append(letter)
  end
  print alphabet
end

def sum_alphabet_values(names)
  create_alphabet
  # Take names list and make into a sorted array
  names_arr = File.read(names).split(",").map(&:strip).sort

  #Need to create hash:


end



sum_alphabet_values('names.txt')
