class node:
  def __init__(self,val):
    self.data = val
    self.prev = None
    self.next = None

class doublylinkedlist(node):
  def __init__(self):
    self.head = None
    self.tail = None
    self.total_node = 0
    
  def __str__(self):
    s1 = ""
    s2 = ""
    if self.head == None:
      return "Empty linked list"
    else:
      self.curr = self.head
      while self.curr != None:
        s1 += f"{self.curr.data} ->"
        self.curr = self.curr.next
      self.curr = self.tail
      while self.curr != None:
        s2 += f"{self.curr.data} ->"
        self.curr = self.curr.prev
      return f"{s1}End \n{s2}Start"
    
  def insert_head(self,val):
    self.new = node(val)
    if self.head == None:
      self.head = self.new
      self.tail = self.new
    else:
      self.new.next = self.head
      self.head.prev = self.new
      self.head = self.new
    self.total_node += 1
    
  def insert_tail(self,val):
    self.new = node(val)
    if self.head == None:
      self.head = self.new
      self.tail = self.new
      
    else:
      self.tail.next = self.new
      self.new.prev = self.tail
      self.tail = self.new
    self.total_node+=1
    
  def insert_at_pos(self,val,pos):
    self.new = node(val)
    if self.head==None:
      self.head = self.new
      self.tail = self.new
    else:
      i=0
      self.curr = self.head
      while i<pos-1 and self.curr.next != None:
        self.curr = self.curr.next
        i+=1
      self.new.next = self.curr.next
      self.curr.next = self.new
      self.new.prev = self.curr
      self.new.next.prev = self.new
    self.total_node+=1
        
  def pop(self,pos):
    if self.head==None:
      raise "Error : Empty Linked List"
    else:
      i=0
      self.curr = self.head
      while i < pos-1 and self.curr.next!=None:
        self.curr = self.curr.next
        i+=1
      self.curr.next = self.curr.next.next
      self.curr.next.prev = self.curr
    self.total_node -= 1
  
obj = doublylinkedlist()
print(obj)
obj.insert_head("San Francisco")
obj.insert_head("Oakland")
obj.insert_head("Fremont")
print(obj)
print(obj.total_node)
obj.insert_tail("Walnut")
print(obj)
print(obj.total_node)
obj.insert_at_pos("Wall",0)
print(obj)
print(obj.total_node)
obj.pop(3)
print(obj)
print(obj.total_node)