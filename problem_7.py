class RouteTrie:
    """
    handling the path of the request
    """
    def __init__(self, handle):
        self.root = RouteTrieNode(handle)

    def insert(self, handle, path_parts):
        """
        inserting the parts of url into the trie
        """
        node = self.root
        for x in path_parts:
            node.kids[x] = RouteTrieNode()
            node = node.kids.get(x)
            if x == '':
                node.handle = 'root handler'
        node.handle = handle

    def find(self, path_parts):
        """
        finding handle for page requested
        """
        node = self.root
        for x in path_parts:
            if x in node.kids:
                node = node.kids.get(x)
            else:
                return None
        return node.handle


class RouteTrieNode:
    """
    storing the urls
    """
    def __init__(self, handle=None):
        self.kids = dict()
        self.handle = handle


class Router:
    """
    handling the http requests
    """
    def __init__(self, handle, root_handle):
        self.route_trie = RouteTrie(handle)
        self.root_handle = root_handle

    def add_handler(self, path, handle):
        """
        adding the page handler
        """
        self.route_trie.insert(handle, self.split_path(path))

    def lookup(self, path):
        """
        searching for available pages with handles
        """
        response = self.route_trie.find(self.split_path(path))
        return 'Not found handler' if response is None else response

    def split_path(self, path):
        """
        static method for returning part of path which are unique as a list
        """
        return set(path.strip().split('/'))


# Tests
router = Router("root handler", "Not found handler")
router.add_handler("/home/about", "about handler")


print(router.lookup('/'))  # 'root handler'
print(router.lookup(' '))  # 'root handler'
print(router.lookup('/home'))   # 'Not found handler'
print(router.lookup('/home/about'))     # 'about handler'
print(router.lookup('/home/about/'))    # 'about handler'
print(router.lookup('/home/about/me'))  # 'Not found handler'
print(router.lookup('classroom.udacity.com/me'))  # 'Not found handler'
