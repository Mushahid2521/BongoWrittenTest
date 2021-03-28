
class Node:
    """
    Node class with value and parent
    """
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent



def lca(node1, node2):
    """
    The complexity of the solution is
    Time: O(N), where N is the total number of nodes present in the tree. We are traversing the tree two times.
    2*N in total so the complexity is linear and checking if a item is present in the set is constant time.

    Space: O(N), where N is the total number of nodes. We are storing the node values in a set to check for
    presence in the next traversal.

    :param node1: one node
    :param node2: another node
    :return:
    """
    # traverse first node and store its parents
    path = set()
    while node1!=None:
        path.add(node1.value)
        node1 = node1.parent

    # traverse node 2 and if any parent match from the previous parents set then this is lca
    while node2!=None:
        if node2.value in path:
            break
        else:
            node2 = node2.parent

    print(f"LCA {node2.value}")
