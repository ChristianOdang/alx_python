# A function that replaces or adds key/value in a dictionary

def update_dictionary(a_dictionary, key, value):
  if len(a_dictionary) == 0:
    a_dictionary[key] = value
  else:
    for a, b in a_dictionary.items():
      if key in a == True:
        a_dictionary[key] = value
      else:
        a_dictionary[key] = value
      return a_dictionary
  return a_dictionary