class Node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1

def Delete_Kth_Element(head, k):
    if head==None:
        return None
    
    if k==1:
        temp = head
        head = head.next
        temp = None
        return head
    
    count = 0
    prev = None
    temp = head

    while(temp!=None): #traversal in LL
        count+=1

        if count==k:
            prev.next = prev.next.next #linking prev element to next element
            temp = None #deleting that element
            break

        prev = temp
        temp = temp.next #moving temp

    return head

def printing_the_LL(head):
    while(head!=None):
        print(head.data, end = " ")
        head = head.next


if __name__ == "__main__":
    arr = [2,5,6,7,9]
    k = 3
    head = Node(arr[0])
    temp = head
    for i in range(1,len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    head = Delete_Kth_Element(head,k)
    printing_the_LL(head)

         
    
