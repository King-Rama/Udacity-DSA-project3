def get_min_max(ints):
     
    n = len(ints)
    
    # Checks if an inputs is empty
    if not ints:
         return
   # Boolen function to check if the list have even number of  elements
    def has_even_number_Of_elements(list):

        if n % 2 == 0:
            return True
        else:
            return False
        
    # Boolean function to help  that will help pairing  comparison
    def compare_the_pair(list):
        if i < n - 1:
            return True
        else:
            return False
        
    def compare_elements(list):
    
        if ints[i] < ints[i + 1]:
            return True
        else:
            return False
    
    
    # First  two element will be initialized as minimum and maximum for  array having an even of elements number
    if has_even_number_Of_elements(n):
        maximum = max(ints[0], ints[1])
        minimum = min(ints[0], ints[1])
         
        # start at index 2
        i = 2

    # First element will be initialized as minimum and maximum since array have an odd number 
    else:
        maximum = minimum = ints[0]
         
        # start at index 1 
        i = 1
         

    # Looping and compare paired elements
        
    while compare_the_pair(n):
        if compare_elements(n):
            maximum = max(maximum, ints[i + 1])
            minimum = min(minimum, ints[i])
        else:
            maximum = max(maximum, ints[i])
            minimum = min(minimum, ints[i + 1])
             
        # Since two elements are proceses in a loop then will increment by 2 
        i += 2
       
    # Return a tuple(min, max) out of list of unsorted integers.
    return (minimum, maximum)




import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

# Tests Cases

# First input
list_of_ints_01 = (0, 9)

# Second input
list_of_ints_02 = (0, 9)

# Third input
list_of_ints_03 = (0, 0)

# Last input
list_of_ints_04 = None


print("Pass" if (list_of_ints_01 == get_min_max(l)) else "Fail")  # Pass
print("Pass" if ( list_of_ints_02 == get_min_max([0])) else "Fail")  # Fail
print("Pass" if (list_of_ints_03 == get_min_max([0])) else "Fail")  # Pass
print("Pass" if ( list_of_ints_04 is get_min_max([])) else "Fail")  # Pass