for i in range(100):
  for j in range(i, 10):
    if i != j:
      print("{}{}".format(i,j), end=", " if i != 8 or j != 9 else "\n")
  