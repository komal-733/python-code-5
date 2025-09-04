def josephus(n,k):
  if n==0:
    return n
  else:
    return (josephus(n-1,k)+k)%n

print(josephus(11,3)+1)