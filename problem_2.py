def rotated_array_search(input_list, number):

    left = 0
    right = len(input_list)-1

    if right > 0:
       
        pivot_elem = find_pivot_elem(input_list, left, right)

        if input_list[pivot_elem] == number:
            return pivot_elem

        if(input_list[left] <= number <= input_list[pivot_elem]):
            return binary_search(input_list, number, left, pivot_elem-1)
        else:
            return binary_search(input_list, number, pivot_elem+1, right)
    return -1


def find_pivot_elem(array, left, right):
    if array[left] < array[right]:
        return 0
    pivot_index = 0
    while left < right:
        pivot_index = (left+right)//2
        if array[pivot_index] > array[pivot_index+1]:
            return pivot_index
        elif array[pivot_index] < array[0]:
            right = pivot_index
        else:
            left = pivot_index + 1
    return pivot_index


def binary_search(array, target_element, start_index, end_index):
    if start_index > end_index:
        return -1

    middle_index = (start_index + end_index)//2
    middle_element = array[middle_index]

    if middle_element == target_element:
        return middle_index
    elif target_element < middle_element:
        return binary_search(array, target_element, start_index, middle_index - 1)
    else:
        return binary_search(array, target_element, middle_index + 1, end_index)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Test Cases provided with question
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


# My Test Cases
#normal rotated array
print (rotated_array_search([4, 5, 6, 7, 0, 1, 2], 0))
print (find_pivot_elem([4, 5, 6, 7, 0, 1, 2], 0, 6))
print(linear_search([4, 5, 6, 7, 0, 1, 2], 0))
test_function([[4, 5, 6, 7, 0, 1, 2], 0])
# 4
# 3
# 4
# pass

#array of single value
print (rotated_array_search([5], 0))
print (find_pivot_elem([5], 0, 0))
print(linear_search([5], 0))
test_function([[5], 0])
# -1
# 0
# -1
# Pass


#normal rotated array with more elements
print (rotated_array_search([6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 20, 1, 2, 3, 4, 5], 1))
print (find_pivot_elem([6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 20, 1, 2, 3, 4, 5], 0, 14))
print(linear_search([6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 20, 1, 2, 3, 4, 5], 1))
test_function([[6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 20, 1, 2, 3, 4, 5], 1])
# 11
# 10
# 11
# Pass



#normal rotated array with big range between element values
print (rotated_array_search([600183,1560202,0,1,2,3,5,6,7,8,9,10,12,13,36,28,49,292,3940,6060,60600,283744], 3))
print (find_pivot_elem([600183,1560202,0,1,2,3,5,6,7,8,9,10,12,13,36,28,49,292,3940,6060,60600,283744], 0, 21))
print(linear_search([600183,1560202,0,1,2,3,5,6,7,8,9,10,12,13,36,28,49,292,3940,6060,60600,283744], 3))
test_function([[600183,1560202,0,1,2,3,5,6,7,8,9,10,12,13,36,28,49,292,3940,6060,60600,283744], 3])
# 5
# 1
# 5
# Pass

#rotated array with string type instead of number values
print (rotated_array_search(["Q", "T", "U", "Y", "A", "B", "C", "D", "E", "F", "G", "H",], "F"))
print (find_pivot_elem(["Q", "T", "U", "Y", "A", "B", "C", "D", "E", "F", "G", "H",], 0, 11))
print (linear_search(["Q", "T", "U", "Y", "A", "B", "C", "D", "E", "F", "G", "H",], "F"))
test_function([["Q", "T", "U", "Y", "A", "B", "C", "D", "E", "F", "G", "H",], "w"])
# 9
# 3
# 9
# Pass

#empty array
test_function([[], 1])
#pass

#normal array which is not rotated
print (rotated_array_search([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 20], 8))
print (find_pivot_elem([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 20], 0, 14))
print(linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 20], 8))
test_function([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 20], 8])
# 7
# 0
# 7
# Pass