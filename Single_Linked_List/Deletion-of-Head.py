class Node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1

#function for deleting head
def Delete_Head(head):
    if head==None:
        return None
    head = head.next
    return head

#function for LinkedList printing
def printing_the_LL(head):
    
    while(head!=None):
        print(head.data, end = " ")
        head = head.next
    

if __name__ == "__main__":
    arr = [2,5,6,7,9]
    head = Node(arr[0])
    temp = head
    for i in range(1,len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    head = Delete_Head(head)
    printing_the_LL(head)
    

    



