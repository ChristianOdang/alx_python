def numbers():
  for nums in range(100):
    print("{:02d}".format(nums), end=", " if nums < 99 else "\n")
numbers()
