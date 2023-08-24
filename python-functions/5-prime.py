# A function that checks if a number is a prime number

def is_prime(num):
  a = []
  for i in range(2, num):
    if(num % i == 0):
      a.append('False')
      break
    else:
      a.append('True')
  if ('False' in a or num <= 1):
    is_valid = False
  else:
    is_valid = True
  return is_valid
