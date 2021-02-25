# problem_1
finding square root of a number and return its floored value
    at first I applied natural-log, but I found two problem when I was playing the scenario mechanically on paper

        - use log built func which is out of scope : not a valid choice for this
        - or use the multiplication of exponent of (0.5) which occur mechanically when simplifying the equation
    
therefore, I chose multiplication by exponent of (0.5)

        - which was converting the answer of (number ** 0.5) to string and split it by '.' then taking the first part
        - this was a O(log(n)) as suggested because it goes to one of the case but not both and finally convert str to int

the overall time complexity of the function sqrt(): log(n)

    - convert the output to string -> O(1)
    - check and splitting the str object and selecting zeroth element -> O(log(n))
    - convert the output to int -> O(1)
    - return the output -> O(n)

the overall space complexity of sqrt() : O(1) 
    since the output conversion will not depend on the input expected