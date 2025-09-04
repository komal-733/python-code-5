class Node:
  def __init__(self,val):
    self.data = val
    self.left = None
    self.right = None
    
class bst:
  def __init__(self):
    self.root = None
    self.total_node = 0

  def insert(self,val):
    self.root = self._insert_rec(self.root,val)
    self.total_node += 1
    
  def _insert_rec(self,node,val):
    new = Node(val)
    if node == None:
      return new
    if node.data > val:
      node.left = self._insert_rec(node.left,val)
    else:
      node.right = self._insert_rec(node.right,val)
    return node
  
  def inorder(self):
    self._inorder_rec(self.root)
    print()
    
  def _inorder_rec(self,node):
    if node:
      self._inorder_rec(node.left)
      print(f"{node.data} ",end="")
      self._inorder_rec(node.right)
      
  def preorder(self):
    self._preorder_rec(self.root)
    print()
    
  def _preorder_rec(self,node):
    if node:
      print(f"{node.data} ",end="")
      self._preorder_rec(node.left)
      self._preorder_rec(node.right)
      
  def postorder(self):
    self._postorder_rec(self.root)
    print()
    
  def _postorder_rec(self,node):
    if node:
      self._postorder_rec(node.left)
      self._postorder_rec(node.right)
      print(f"{node.data} ",end="")
      
  def search(self,val):
    result = self._search_rec(self.root,val)
    print(f"{val} found") if result else print(f"{val} not found")
    
  def _search_rec(self,node,val):
    if node == None or node.data == val:
      return node
    if node.data > val:
      return self._search_rec(node.left,val)
    else:
       return self._search_rec(node.right,val)
     
  def max(self):
    result = self._max_rec(self.root)
    print(result)
    
  def _max_rec(self,node):
    if node == None:
      raise "Tree : Empty"
    if node.right:
      return self._max_rec(node.right)
    return node.data
  
  def min(self):
    result = self._min_rec(self.root)
    print(result)
    
  def _min_rec(self,node):
    if node == None:
      raise "Tree : Empty"
    if node.left:
      return self._min_rec(node.left)
    return node.data
  
  def delete(self,val):
    self.root = self._delete_rec(self.root,val)
    
  def _delete_rec(self,node,val):
    if node == None:
      return node
    if node.data > val:
      node.left = self._delete_rec(node.left,val)
    elif node.data < val:
      node.right = self._delete_rec(node.right,val)
    else:
      if node.left == None and node.right == None:
        return None
      elif node.left != None and node.right == None:
        return node.left
      elif node.right != None and node.left == None:
        return node.right
      else:
        rep_node = self._min_rec(node.right)
        node.data = rep_node.data
        node.right = self._delete_rec(node.right,rep_node.data)
    return node
        
tree = bst()
tree.insert(60)
tree.insert(40)
tree.insert(20)
tree.insert(10)
tree.insert(30)
tree.insert(50)
tree.insert(80)
tree.insert(70)
tree.insert(90)
tree.inorder()
tree.preorder()
tree.postorder()
tree.search(30)
tree.search(100)
print(tree.total_node)
tree.max()
tree.min()
tree.delete(30)
tree.inorder()