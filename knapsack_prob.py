class Fruit:
  def __init__(self,name,price,weight):
    self.name = name
    self.price = price
    self.weight = weight
    
def knapsack(capacity,fruits):
  value = [0 for _ in range(capacity+1)]
  item = [0 for _ in range(capacity+1)]
  for i in range(len(fruits)):
    size = fruits[i].weight
    for j in range(size,capacity+1):
      p = j-size
      val = value[p] + fruits[i].price
      if val > value[j]:
        value[j] = val
        item[j] = i
  
  print(f"Weight of backpack \t Value \t Item \t Name")
  for i in range(1,capacity+1):
    print(f" \t {i}kg \t\t {value[i]} \t {item[i]} \t ")
    
  items = []  
  names = []    
  max = capacity
  while 1<=max:
    fruit = fruits[item[max]]
    items.append(item[max])
    names.append(fruit.name)
    max -= fruit.weight
  
  print(items)  
  print(names)

fruits = [Fruit("Plum",4500,4),
        Fruit("Apple",5700,5),
        Fruit("Orange",2250,2),
        Fruit("Strawberry",1100,1),
        Fruit("Melon",6700,6)]  
knapsack(8,fruits)
  