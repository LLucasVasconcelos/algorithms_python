def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    L = merge_sort(arr[:len(arr)//2])
    R = merge_sort(arr[len(arr)//2+1:])
    return merge(L,R)

def merge(L,R):
    i = j = 0
    result = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
    result += L[i:]
    result += R[j:]x
    return result
vector = [15,2,7,3,9,4,12,10,14,5]

print(merge(vector))