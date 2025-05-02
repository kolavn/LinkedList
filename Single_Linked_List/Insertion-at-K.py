class Node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1

def Insertion_at_K(head, number, k):
    if head == None:
        return Node(number)
    
    if k == 1:
        temp = Node(number)
        temp.next = head
        return temp
    
    count = 0
    temp = head
    while(temp!=None):
        temp = temp.next
        count+=1
        
        if count==k-1: #then we need to insert the element
            new = Node(number)
            # temp.next = new #this should go down 
            # new.next = temp.next  #this step should go up to attach new to rest of LL
            new.next = temp.next
            temp.next = new
            break
    return head

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
    
    head = Insertion_at_K(head, 55, 3)
    print_New_LL(head)      