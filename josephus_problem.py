def josephus(n,k):
  people = list(range(1,n+1))
  index = 0
  seq = []
  while people:
    index = (index+k-1)%len(people)
    seq += [people.pop(index)]
  return seq

print(josephus(11,3))