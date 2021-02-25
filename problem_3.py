class Heap:
    def __init__(self, initial_size):

        # used to store elements: helps in quick insertion
        self.cbt = [None for _ in range(initial_size)]

        # useful in insertion to determine the next index
        self.next_index = 0

    def insert(self, data):
        # insertion
        self.cbt[self.next_index] = data

        # heapify before updating the next insertion point
        self.insert_heapify()

        # point to the next insertion index
        self.next_index += 1

    def remove(self) -> int:
        """
        Remove and return the max element found at the top of the heap
        """
        if self.next_index == 0:
            return None

        self.next_index -= 1

        to_remove = self.cbt[0]
        first_element = self.cbt[self.next_index]

        self.cbt[0] = first_element

        self.cbt[self.next_index] = to_remove
        self.remove_heapify()

        return to_remove

    def remove_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent_value = self.cbt[parent_index]
            left_child_value = None
            right_child_value = None

            max_element = parent_value

            # check if left child exists
            if left_child_index < self.next_index:
                left_child_value = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child_value = self.cbt[right_child_index]

            # compare with left child
            if left_child_value is not None:
                max_element = max(parent_value, left_child_value)

            # compare with right child
            if right_child_value is not None:
                max_element = max(right_child_value, max_element)

            # check if parent is rightly placed
            if max_element == parent_value:
                return

            if max_element == left_child_value:
                self.cbt[left_child_index] = parent_value
                self.cbt[parent_index] = max_element
                parent_value = left_child_index

            elif max_element == right_child_value:
                self.cbt[right_child_index] = parent_value
                self.cbt[parent_index] = max_element
                parent_value = right_child_index

    def insert_heapify(self):
        # heapify is called during insertion, now the child index that will be
        # compared to its parent will be located at next_index: before it
        # has been incremented
        child_index = self.next_index

        # if child_index >=1 look for parent iteratively compare until no parent is
        # smaller

        while child_index >= 1:

            # obtain parent location
            parent_index = (child_index - 1)//2

            # obtain parent value
            parent_value = self.cbt[parent_index]

            # obtain child value
            child_value = self.cbt[child_index]

            # if parent is smaller than child shuffle the position
            # as this is max heap
            if parent_value < child_value:
                self.cbt[parent_index] = child_value
                self.cbt[child_index] = parent_value

                # update child index
                child_index = parent_index
            else:
                break


def rearrange_digits(input_list):

    input_size = len(input_list)

    output_list = []

    if input_size <= 0:
        return output_list

    if input_size == 1:
        return[input_list[0]]

    first_int = ""
    second_int = ""

    heap = Heap(len(input_list))
    for element in input_list:
        heap.insert(element)

    for k in range(len(input_list)):
        top_element = heap.remove()
        if k == 0 or k % 2 == 0:
            first_int += str(top_element)
        else:
            second_int += str(top_element)

    output_list.extend([int(first_int), int(second_int)])

    return output_list


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_case0 = [[1], [1,0]]
test_case1 = [[5], [5,0]]
test_case2 = [[], [0,0]]
test_case3 = [[9, 9, 9, 9, 9], [999, 99]]
test_case4 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case5 = [[3, 3, 3, 3, 3, 3], [333, 333]]
test_case6 = [[0, 0, 0, 0, 9, 8], [900, 800]]
test_case7 = [[0, 0, 0, 0, 0, 0], [0, 0]]

test_cases = [test_case0, test_case1, test_case2, test_case3, test_case4,test_case5,test_case6,test_case7]

for test_case in test_cases:
    test_function(test_case)
