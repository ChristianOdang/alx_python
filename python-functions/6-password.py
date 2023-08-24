# A function to validate a password from user
def validate_password(password):
  # Check password lenth
  if len(password) < 8:
    return False
  
  # Check for uppercase, lowercase, and digits
  pswd_has_uppercase = False
  pswd_has_lowercase = False
  pswd_has_digit = False
  
  for char in password:
    if char.isupper():
      pswd_has_uppercase = True
    elif char.islower():
      pswd_has_lowercase = True
    elif char.isdigit():
      pswd_has_digit = True
      
  # Check if all conditions are met
  if not (pswd_has_uppercase and pswd_has_lowercase and pswd_has_digit):
    return False
  
  # Check for white spaces 
  if ' ' in password:
    return False
  return True

