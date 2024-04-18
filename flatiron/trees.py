class BinaryTree:
   def __init__(self, value, left=None, right=None) -> None:
      self.value = value
      self.left = left
      self.right = right
      #self.parent --> kind of optional, but every node has a parent, so use if you want to navigate back up the tree

n1 = BinaryTree(10)
#Assume n2 is the head 
n2 = BinaryTree(30)
n3 = BinaryTree(2)
n4 = BinaryTree(100) 

n2.left = n1
n2.right = n4
n1.left = n3 

#      n2(30)        
#    /        \
#   n1(10)    n4(100)
#  /
# n3(2) 

# How would we insert n5 = BinaryTree(50)? 

def insertIntoTree(head, newnode):
   currenthead = head
   if newnode.value > currenthead.value:
      if currenthead.right == None:
         currenthead.right = newnode
      else: 
        insertIntoTree(currenthead.right, newnode)
   elif newnode.value < currenthead.value:
      if currenthead.left == None:
         #Loop finishes here - once n4/100 is reached, and 50 is less than 100, and there's no left node, 50 becomes the left node
         currenthead.left = newnode
      else:
         insertIntoTree(currenthead.left, newnode)
      




# Example
# Given the head of a binary tree print each value in the tree by level.