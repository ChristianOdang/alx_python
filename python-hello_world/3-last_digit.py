import random
number = random.randint(-10000, 10000)

# Check if number is positive
if (number > 0):
  # convert to string
  num_str = str(number) 
  last_digit = int(num_str[-1])
elif (number < 0): # if number is negative
  num_str = str(number)
  last_digit = int('-' + num_str[-1])
else:
  last_digit = number
  
  status = str("Last digit of {} is {}".format(number, last_digit))
  if last_digit > 5:
    print(status, "and is greater than 5")
  elif last_digit < 6 and last_digit != 0:
    print(status, "and is less than 6 and not 0")
  elif last_digit == 0:
    print(status, "and is 0")
    