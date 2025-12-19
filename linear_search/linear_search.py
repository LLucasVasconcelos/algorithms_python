## linear search


def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


array = [1,2,3,4,5,6,7,9,14,12,412,3146,6543,656,2233,58]
value = 3146
search_result = linear_search(array=array, value=value)
print(f"Position: {search_result}\nValue: {value}")

"""
    As the Name suggests, this algorithm searches for a value in a list,
    if the value is present, the algorith returns its position,
    otherwise, it returns a error.
"""





     
    