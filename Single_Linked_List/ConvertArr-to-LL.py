#array to LL,
#mostly asks to print head

#common part
class Node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1

#actual code
def ConvertLLtoArr(arr):
    head  = Node(arr[0])
    mover = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    return head

arr = [2,4,7,9]
head = ConvertLLtoArr(arr)
print(head.data)


