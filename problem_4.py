"""
Required: To sort an array that is rearranged in 0's, 1's and 2's via the sort_012 function
which will sort the elements with a single traversal
"""


def sort_012(input_list):
    # We declare the values that are going to be in the input_list or array which are 0's, 1's and 2's
    left_low = center = 0
    right_high = len(input_list) - 1

    # A traverse throughout the whole array

    while center <= right_high:
        # The first condition is to check whether the element is 0 and if it's so we swap it with the element at the
        # center such that it is placed on the left of the middle element
        if input_list[center] == 0:
            input_list[center], input_list[left_low] = input_list[left_low], input_list[center]
            left_low += 1
            center = center + 1
        # The second condition is to check if the element is 1 the we don't do anything rather than to go to the next
        # element
        elif input_list[center] == 1:
            center += 1
        else:
            # The remaining condition is to check if the element is in the group of 2 , if it is so we swap it with
            # the element at the center such that it is placed on the right of the middle element
            input_list[center], input_list[right_high] = input_list[right_high], input_list[center]
            right_high -= 1


# Test function for test cases
def test_function(test_case):
    sort_012(test_case)
    print(test_case)
    if not test_case:
        print("The input_list is empty")

    elif (test_case == sorted(test_case)) and test_case != []:
        print("Pass")

    else:
        print("Fail")


test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test_case)

test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test_case)

test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)

test_case = []
test_function(test_case)
