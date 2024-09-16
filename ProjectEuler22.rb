#1. Make list into an array
#2. Sort by alphabetical order the array
#3. Take sortd array and calaculate the aphabetical value and create hash name => alphabetical value
#4. add up all the alphabetical values


def create_alphabet
  alphabet = []
  ('A'..'Z').each do |letter|
    alphabet.append(letter)
  end
  alphabet
end

def sum_alphabet_values(names)
  alphabet = create_alphabet
  index = 1
  alphabet_value = []
  # Take names list and make into a sorted array
  names_arr = File.read(names).split(",").map(&:strip).sort
  names_arr.each do |name|
    sum_for_letter = 0
    name.chars.each do |letter|
      if alphabet.include?(letter)
        sum_for_letter += alphabet.index(letter) + 1
      end
    end
    alphabet_value.append(sum_for_letter*index)
    index += 1
  end
  total = alphabet_value.sum
  puts total
end


sum_alphabet_values('names.txt')
