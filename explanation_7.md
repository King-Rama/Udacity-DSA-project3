# problem_7
http Request Routing in a Web Server with a Trie

the solution is implemented on the blueprints given from the question

    - on the walk through of the problem on paper I had several implementation choice, but some extended beyond O(n)
    - the obviously choice was using three classes one for the Trie(whole path from root) to act as base url
    - the other class for holding single route with its kids which are other routes and linking then by objects storing in a dict of O(n) space
    - the other class was for the router its self this was doing some initialization it was there to remove the need of having one large func
    - add_handler() and lookup() methods required looping and accessing the trie to avoid expensive search
    - lookup() needed to have less control to avoid double call of the previous classes as it was only receiving response from find()

the overall time complexity: O(n)

    - adding handler requires iteration : O(n)
    - conditional inside the loops : O(log(n))
    - path lookup involves loops: O(n)

the overall space complexity: O(n)

    - three class used
        - one for node with kids of type dict : O(n)
        - the other for route path : O(n)
        - the other for handling request  : O(n)
    
    - lookup menthod: O(1)
    - adding_handler method: O(n)
    
