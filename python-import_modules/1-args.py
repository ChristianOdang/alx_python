import sys

def main():
  args = sys.argv[1:]
  number_args = len(args)
  
  print("{} arguement{}:".format(number_args, 's' if number_args != 1 else ''))
  for i, arg in enumerate(args, 1):
    print("{}: {}".format(i, arg))
    
  if __name__ == "__main__":
    main()
       
  