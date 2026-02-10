
### This search is used when the values is ordenated:
def binary_search(arr,value):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left+right)//2
        print(f"left {left}",f"mid: {mid}",f"right: {right}")
        if value > arr[mid]:
            left = mid +1
        elif arr[left] == value:
            return left
        else:
            right = mid
            
    else:
        return -1
            
            
array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(binary_search(array,11))
print(array[binary_search(array,11)])
            