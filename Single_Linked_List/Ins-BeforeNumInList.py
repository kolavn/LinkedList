#we need to insert an element before a given element present in the list
class Node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1

def Insertion_Before_Number(head, number, k):#k is new number
    if head == None:
        return None #bcoz inserting elemennt before an emplty is not possibe
    
    if head.data == number:
        new = Node(k)
        new.next = head
        return new
    
    temp = head
    while(temp!=None):
        if temp.next.data==number: #then we need to insert the element
            new = Node(k)
            # temp.next = new #this should go down 
            # new.next = temp.next  #this step should go up to attach new to rest of LL
            
            
            new.next = temp.next
            temp.next = new
            break
        temp = temp.next
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
    
    head = Insertion_Before_Number(head, 7, 11)
    print_New_LL(head)