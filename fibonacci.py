def fibonacci(n):
  if n==1 or n==0:
    return n 
  else:
    return fibonacci(n-1)+fibonacci(n-2)
  
for i in range(7):  
  print(fibonacci(i))