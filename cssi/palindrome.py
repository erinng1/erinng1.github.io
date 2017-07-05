def is_palindrome(word):
  first_half = None
  second_half = None

  if len(word) % 2 == 0:
  	first_half = len(word) / 2
  	second_half = len(word) / 2
  else:
  	first_half = (len(word) / 2) + 1
  	second_half = len(word) / 2

  if first_half == second_half:
  	return word + ' is a palindrome!'
  else:
  	return word + ' is not a palindrome...'
    
  first_half = word[:first_half]
  second_half = word[second_half:]
  second_half = second_half[::-1]

print is_palindrome('kayak')
print is_palindrome('racecar')
print is_palindrome('katniss everdeen')
