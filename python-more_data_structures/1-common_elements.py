# A function that returns a set of common elements in two sets

def common_elements(set_1, set_2):
  
  # create an empty set to store common elements
  cmmn_set = set()
  
  # Iterate through the element of set_1
  for element in set_1:
    if element in set_2:
      cmmn_set.add(element)
      
  return cmmn_set