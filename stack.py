class node:
  def __init__(self,val):
    self.data = val
    self.next = None

class stack(node):
  def __init__(self):
    self.head = None
    self.total_node = 0
    
  def push(self,val):
    new = node(val)
    if self.head == None:
      self.head = new
    else:
      new.next = self.head
      self.head = new
    self.total_node += 1
    
  def pop(self):
    if self.head == None:
      raise "Stack : Empty"
    else:
      self.head = self.head.next
    self.total_node -= 1
    
  def peek(self):
    if self.head == None:
      raise "stack : empty"
    else:
      return self.head.data
    
  def __str__(self):
    s=""
    if self.head==None:
      return "Stack : empty"
    else:
      curr = self.head
      while curr!=None:
        s += f"{curr.data} - "
        curr = curr.next
      return s+"End"
    
stack = stack()
print(stack)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
print(stack)
print(stack.total_node)
stack.pop()
print(stack)
stack.pop()
print(stack)
print(stack.total_node)
print(stack.peek())