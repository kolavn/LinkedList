class Node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1


def Delete_Tail(head):
    if head == None or head.next==None: #if LL has only one element and no 2nd element
        return None
    temp = head
    while(temp.next.next!=None): # condition for LL having more than 2 elements
        temp = temp.next
    temp.next = None # deleting last element once above loop reaches last element
    return head

def print_restof_LL(head):
    temp = head
    
    while(temp!=None):
        print(temp.data, end = " ")
        temp = temp.next
    

if __name__ == "__main__":
    arr = [2,5,6,7,9]
    head = Node(arr[0])
    temp = head
    for i in range(1,len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    
    head = Delete_Tail(head)
    print(head)
    print_restof_LL(head)
