# A function that returns a key with the biggest integer value

def best_score(a_dictionary):
  if a_dictionary == None:
    best_score = None
  elif len(a_dictionary) == 0:
    best_score = None
  else:
    for i, j in a_dictionary.items():
      if j == max(list(a_dictionary.values())):
        best_score = i
    return best_score