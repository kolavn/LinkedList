class Node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1

def Insertion_Head(head, k):#K is element to be inserted
    if head == None:
        return None
    temp = Node(k)
    temp.next = head
    return temp

def print_New_LL(head):
    temp = head
    while(temp!=None):
        print(temp.data, end = " ")
        temp = temp.next
    print() #for new line after printing

    
if __name__ == "__main__":
    arr = [2,5,6,7,9]
    head = Node(arr[0])
    temp = head
    for i in range(1,len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    
    head = Insertion_Head(head, 55)
    print_New_LL(head)      