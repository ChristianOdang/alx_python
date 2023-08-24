# A function that computes the square value of all integers of a matrix

def square_matrix_simple(matrix=[]):
  # create a new matrix to store to store the squared value
  new_squ_matrix = []
  for row in matrix:
    squ_row = []
    for element in row:
      squ_element = element ** 2
      squ_row.append(squ_element)
    new_squ_matrix.append(squ_row)
    
  return new_squ_matrix