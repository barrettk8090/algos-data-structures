[{"a":1, "b": 2},1,3]
lista = [1,2,3]
lista.append(5)
lista[2]
#Example of "finding number" algorithm

# for i in lista:
#     if i == 2:
#         return True


# Creating a node for a singly linked list
class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next
        self.previous = None


linkeda = Node(1,Node(2,Node(3)))

#Same as writing
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n1.next = n2
# n2.next = n3

current = linkeda
if current.value == True:
    return True
while current.next != None:
    if current.next.value == 2:
        return True
    current = current.next