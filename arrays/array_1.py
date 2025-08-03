# 1) Largest number in an array :
arr = [3,5,2,8,6]
largest  = arr[0]
for i in range(arr):  # time complexity O(n) 
    if i > largest :
        largest = i
    print("Largest number in the array is:", largest)



#secidn) Smallest number in an array :
arr = [3,5,2,8,6]
largest = 0 
for i in range(arr): #time complexity = O(n)
    if i > largest:
        largest = i

s_largest = -1        
for j in range(arr):  #time complexity = O(n)
    if j > s_largest and j != largest:
        s_largest = j 
    print("Second largest number in the array is:", s_largest)