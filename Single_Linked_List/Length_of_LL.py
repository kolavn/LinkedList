class Node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1

#actual code
def Length_of_LL(head): # always head will be given
    count = 0
    temp = head
    while (temp!=None):
        temp = temp.next
        count+=1
    return count

arr = [2,5,6,7,9]
head = Node(arr[0])
temp = head

for i in range(1,len(arr)):
    temp.next = Node(arr[i])
    temp = temp.next

    
count = Length_of_LL(head)
print(count)

 