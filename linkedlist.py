class node:
  def __init__(self,value):
      self.data = value
      self.next = None
      
class linkedlist(node):
  def __init__(self):
    self.head=None
    self.tail=None
    self.total_node = 0
    
  def insert_head(self,val):
    self.new = node(val)
    if self.head == None:
      self.head = self.new
      self.tail = self.new
    else:
      self.new.next = self.head
      self.head = self.new
    self.total_node += 1
      
  def insert_tail(self,val):
    self.new = node(val)
    if self.tail == None:
      self.head = self.new
      self.tail = self.new
    else:
      self.tail.next=self.new
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
      while i<pos-1 and self.curr.next!=None:
        self.curr = self.curr.next
        i+=1
      self.new.next=self.curr.next
      self.curr.next=self.new
    self.total_node+=1
  
  def __str__(self):
    s=""
    if self.head == None:
      return "Empty Linked List"
    else:
      self.curr = self.head
      while self.curr!=None:
        s += f"{self.curr.data} ->"
        self.curr = self.curr.next
      return s+"End"

  def pop(self, pos):
    if self.head == None:
      raise "Error : Empty Linked List"
    else:
      self.curr = self.head
      i=0
      while i<pos-1 and self.curr.next!=None:
        self.curr=self.curr.next
        i+=1
      self.curr.next = self.curr.next.next
    self.total_node-=1
    
obj = linkedlist()
obj.insert_head("San Francisco")
obj.insert_head("Oakland")
obj.insert_head("Berkeley")
obj.insert_tail("Fremont")
obj.insert_at_pos("Walnut",2)
obj.insert_at_pos("Wall",2)
print(obj.total_node)
print(obj)
obj.pop(5)
print(obj.total_node)
print(obj)