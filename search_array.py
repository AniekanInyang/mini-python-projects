# input = [-2, -1, 3, 4, 7, 9]

# sorted array in asc order, non-repetitive
# target number = 7
# output the index of the number, else return -1

# function
def search_array(arr, target_num):
    low_index = 0 # low index pointer set to first index of array
    high_index = len(arr) - 1 # high pointer set to last index of array
    while (low_index <= high_index): # loop through list
        mid_index = (low_index + high_index) // 2 # middle index of array
        mid_num = arr[mid_index]
        if mid_num == target_num: # if middle element is the target number, return index of middle element
            return mid_index
        elif mid_num < target_num: # if middle element is less than the target number assign low index to index after middle index
            low_index = mid_index + 1 
        elif mid_num > target_num: # if middle element is less than the target number assign low index to index before middle index
            high_index = mid_index - 1

    return -1 # else return -1

# Test cases
input = [-2, -1, 3, 4, 7, 9]
print(search_array(input, 5)) # should print -1
print(search_array(input, -1)) # should print 1
print(search_array(input, 7)) # should print 4
print(search_array(input, -5)) # should print -1