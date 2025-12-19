vector = [15,2,7,3,9,4,12,10,14,5]


def insertion_sort_ascending(vector):
    for i in range(1,len(vector)):
        key = vector[i]
        j = i-1
        while j>=0 and vector[j] > key:
            vector[j+1] = vector[j]
            j = j-1
        vector[j+1] = key 
    return vector

sorted_vector = insertion_sort_ascending(vector)
print("Ascending sorted_vector:", sorted_vector)


def insertion_sort_descending(vector):
    for i in range(1,len(vector)):
        key = vector[i]
        j = i-1
        while j >= 0 and vector[j] < key:
            vector[j+1] = vector[j]
            j = j-1
        vector[j+1] = key
    return vector

sorted_vector = insertion_sort_descending(vector)
print("Descending sorted_vector:", sorted_vector)


""" Description:
    *Insertion Sort Algorithm in Python*

    - It works by dividing the list into a sorted and an unsorted region,
    and repeatedly inserting elements from the unsorted region into the 
    correct position in the sorted region.
"""