# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array):
    idx_list = [i for i, num in enumerate(source_array) if num % 2 == 1]
    num_list = [source_array[i] for i in idx_list]

    num_list.sort()
    
    for idx, val in zip(idx_list, num_list):
        source_array[idx] = val
    
    return source_array



print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))