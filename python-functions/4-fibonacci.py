# fibonacci sequence
def fibonacci_sequence1(n):
  a,b = 0,1
  while (b<n):
    print(b, end=', ')
    a, b=b, a+b
    
#fib2
def fibonacci_sequence(n):
  a = []
  if(n >= 1):
    a.append(0)
  if(n > 1):
    a.append(1)
  for i in range(2, n):
    a.append(a[i - 1] + a[i - 2])
  return a
