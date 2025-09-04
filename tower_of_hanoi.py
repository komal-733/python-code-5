def toi(n,left,mid,right):
  if n==1:
    print(f"Move {n} from {left} to {right}")
  else:
    toi(n-1,left,right,mid)
    print(f"Move {n} from {left} to {right}")
    toi(n-1,mid,left,right)
    
toi(3,"A","B","C")