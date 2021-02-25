## Problem 5
For this trie I decided to use Dictionary (Dict) to store the children, beacause it makes easier to read and change the data,also it is simple to retrieve values based on their key.

 ## Insert Method

 Time compexity O(n)

Since each character of the word needs to be inserted into the child node separately, therefore iteration should be done to each character of the word.
If a word contains four character then we will have four successful iterations.

 Space Complexity O(n)

 Each character need to allocated in memory


## Find Method

Time Complexity O(n)

Finding a node that contains given prefix depends on a number of characters present in the prefix, so if we have the prefix of two characters then iteration will be done twice.

Space Complexity O(1)

No memory allocated


## Suffixes Method

Time Complexity O(n)

Each character need to be iterated through

Space Complexity O(1)


No memory is allocated

The time complexity to traverse through tries given by O(n).

The space complexity for this whole program is O(1).







