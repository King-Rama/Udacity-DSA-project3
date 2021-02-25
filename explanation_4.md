The aim of the program was to solve Dutch National Flag Problem. The flag consists of 3 colors white,red and blue.
Where by those colors in this particular scenerio are represented by numbers 0,1,2. So we are given an array with
these numbers which are rearranged. Our task is to now arrange or group them according to their identity and order.
Starting from 0, 1 and 2. The algorithm was to first declare the element that is supposed to stay at the center as
the pivot which is 1 then compare with other elements 0 and 2 such that when the element is 0 swapping is done to the left side 
of the middle element and when the element is found to be 2 the element is now swapped at the right side
of the middle element. This process is repeated until the traverse is finished.

-**The time complexity to traverse all the array is given by O(n)**.

-**The space complexity for this whole program is O(1)**; since there is no additional space complexity in swapping.
