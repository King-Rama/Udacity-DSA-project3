# problem_3
Rearranging elements in an array to obtain two numbers with maximum sum

The method rearrange_digits() has overall time complexity of O(nlog(n))

The method uses Max Heap to place the elements in a binary tree using
log(n) complexity then retrieve each element from largest to smallest 
with the same time complexity of log(n).

The linear iteration through all elements makes the overall time complexity
of O(nlog(n))

Max Heap uses array to store elements hence the space complexity of O(n)