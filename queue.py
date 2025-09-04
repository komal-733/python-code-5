class node:
  def __init__(self,val):
    self.data = val
    self.next = None
    
class queue(node):
  def __init__(self):
    self.head = None
    self.tail = None
    self.total_node = 0
    
  def __str__(self):
    s=""
    if self.head == None:
      return"Empty Queue"
    else:
      self.curr = self.head
      while self.curr!=None:
        s += f"{self.curr.data} - "
        self.curr =self.curr.next
      return s+"End"
    
  def insert(self,val):
    self.new = node(val)
    if self.head==None:
      self.head = self.new
      self.tail = self.new
    else:
      self.tail.next = self.new
      self.tail= self.new
    self.total_node += 1
    
  def pop(self):
    if self.head == None:
      raise "Error : Queue is Empty"
    else:
      self.head = self.head.next
      if self.head == None:
        self.tail == None
    self.total_node -= 1
    
  def peek(self):
    if self.head == None:
      raise "Queue : Empty"
    else:
      return self.head.data
queue = queue()
print(queue)
queue.insert(1)
queue.insert(2)
queue.insert(3)
queue.insert(4)
queue.insert(5)
queue.insert(6)
print(queue)
print(queue.total_node)
queue.pop()
print(queue)
queue.pop()
print(queue)
print(queue.total_node)
print(queue.peek())