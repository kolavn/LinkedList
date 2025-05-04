#pick 4 consecutive numbers such that their sum is max
#we need to pick some numbers in first and some no. in last and not in middle

def max_point_cards(arr,k):
    left_sum = 0
    n = len(arr)
    right_sum = 0
    max_sum = 0
    #for left sum; only left numbers are taken into consideration
    for i in range(0,k):
        left_sum = left_sum + arr[i]
        max_sum = left_sum #lets say max sum is obtained from left list
    
    right_index  = n - 1 
    for i in range(k-1,0,-1): #descreasing left and increase right
        left_sum = left_sum - arr[i]
        right_sum =  right_sum + arr[right_index] #add right elements
        right_index = right_index - 1 #decrease the index
    max_sum =  max(max_sum, (left_sum+right_sum))

    return max_sum

arr = [1, 2, 3, 4, 5]
k = 5
print('max sum is', max_point_cards(arr,k))




