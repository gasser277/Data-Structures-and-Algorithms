from collections import defaultdict
class RouteTrie:
    def __init__(self, h):
        self.root = RouteTrieNode(h)
    def insert(self, part, h):
        node = self.root
        for part in part:
            node.insert(part)
            node = node.children[part]
        node.h = h
    def find(self, part):
        node = self.root
        for part in part:
            if part in node.children:
                node = node.children[part]
            else:
                return None
        return node.h
class RouteTrieNode:
    def __init__(self, h=None):
        self.children = defaultdict(RouteTrieNode)
        self.h = h

    def insert(self, path):
        self.children[path] = RouteTrieNode()
class Router:
    def __init__(self, h, not_found_h):
        self.routeTrie = RouteTrie(h)
        self.not_found_h = not_found_h

    def add_h(self, path, h):
        part = self.split_path(path)
        self.routeTrie.insert(part, h)

    def lookup(self, path):
        part = self.split_path(path)
        h = self.routeTrie.find(part)
        if h is None:
            return self.not_found_h
        else:
            return h
    def split_path(self, path):
        path = path.strip("/")
        return path.split("/") if path else []
router = Router("root h", "not found h")
router.add_h("/home/about", "about h")  # add a route

#Test case 1
print("pass" if router.lookup("/")== "root h" else "fail")
# Test case 2
print("pass" if router.lookup("/home/about")== "about h" else "fail")
print("pass" if router.lookup("/home/about/") == "about h" else "fail")
print("pass" if router.lookup("/home")== "not found h" else "fail")
# Test case 3
print("pass" if router.lookup("")== "root h" else "fail")
print("pass" if router.lookup("/home/about/me")== "not found h" else "fail")


