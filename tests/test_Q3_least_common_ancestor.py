import io
from Q3_least_common_ancestor import lca
import unittest.mock


class Node:
    """
    Node class with value and parent
    """
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent



class TestQ3(unittest.TestCase):
    # Reusable helper method for testing print
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, node1, node2, expected_output, mock_stdout):
        lca(node1, node2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_same_branch(self):
        one = Node(1)
        two = Node(2)
        three = Node(3)
        """
               1
              / 
             2 
            /
           3    
        """

        two.parent = one
        three.parent = two
        expected = "LCA 1\n"
        self.assert_stdout(one, two, expected)

    def test_two_nodes_only(self):
        one = Node(1)
        two = Node(2)
        """
              1
             /
            2 
        """

        two.parent = one
        expected = "LCA 1\n"
        self.assert_stdout(one, two, expected)

    def test_ifnot_binary_tree(self):
        one = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        five = Node(5)
        six = Node(6)
        """
              1
             / \
            2   3
           /|\
          4 5 6
        """
        two.parent = one
        three.parent = one
        four.parent = two
        five.parent = two
        six.parent = two

        expected = "LCA 2\n"
        self.assert_stdout(four, six, expected)

    def test_given_sample(self):
        one = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        five = Node(5)
        six = Node(6)
        seven = Node(7)
        eight = Node(8)
        nine = Node(9)
        """
                1
               / \
              2   3
             / \ / \
            6  8 4  5
           / \
          7   9
        """

        two.parent = one
        three.parent = one
        four.parent = three
        five.parent = three
        six.parent = two
        eight.parent = two
        seven.parent = six
        nine.parent = six

        expected = "LCA 2\n"
        self.assert_stdout(eight, seven, expected)

    def test_immediate_parent(self):
        one = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        five = Node(5)
        six = Node(6)
        seven = Node(7)
        eight = Node(8)
        nine = Node(9)
        """
                1
               / \
              2   3
             / \ / \
            6  8 4  5
           / \
          7   9
        """

        two.parent = one
        three.parent = one
        four.parent = three
        five.parent = three
        six.parent = two
        eight.parent = two
        seven.parent = six
        nine.parent = six

        expected = "LCA 3\n"
        self.assert_stdout(four, five, expected)

    def test_root_is_lca(self):
        one = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        five = Node(5)
        six = Node(6)
        seven = Node(7)
        eight = Node(8)
        nine = Node(9)
        """
                1
               / \
              2   3
             / \ / \
            6  8 4  5
           / \
          7   9
        """

        two.parent = one
        three.parent = one
        four.parent = three
        five.parent = three
        six.parent = two
        eight.parent = two
        seven.parent = six
        nine.parent = six

        expected = "LCA 1\n"
        self.assert_stdout(seven, five, expected)

    def test_subbranch_member(self):
        one = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        five = Node(5)
        six = Node(6)
        seven = Node(7)
        eight = Node(8)
        nine = Node(9)
        """
                1
               / \
              2   3
             / \ / \
            6  8 4  5
           / \
          7   9
        """

        two.parent = one
        three.parent = one
        four.parent = three
        five.parent = three
        six.parent = two
        eight.parent = two
        seven.parent = six
        nine.parent = six

        expected = "LCA 2\n"
        self.assert_stdout(eight, seven, expected)



if __name__=="__main__":
    unittest.main()

