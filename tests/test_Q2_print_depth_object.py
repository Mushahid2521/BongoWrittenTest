import io
from Q2_print_depth_object import print_depth
import unittest.mock

class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

class Car(object):
    def __init__(self, price, model, similar):
        self.price = price
        self.model = model
        self.similar = similar

class TestQ2(unittest.TestCase):
    # Reusable helper method for testing print
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, data, expected_output, mock_stdout):
        print_depth(data)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_one_item(self):
        data = {"Key1": 1}
        expected = "Key1 1\n"
        self.assert_stdout(data, expected)

    def test_one_item_deep(self):
        data = {"Key1": {
                    "Key2": {
                        "Key3": 2
                    }
        }}
        expected = "Key1 1\nKey2 2\nKey3 3\n"
        self.assert_stdout(data, expected)

    def test_mutiple_item(self):
        data = {"key1":1, "key2":2, "key3":3}
        expected = "key1 1\nkey2 1\nkey3 1\n"
        self.assert_stdout(data, expected)

    def test_with_object(self):
        person_a = Person("User", "1", None)
        person_b = Person("User", "2", person_a)

        data = {
                "key1": 1,
                "key2": {
                    "key3": 1,
                    "key4": {
                        "key5": 4,
                        "key6": 10,
                        "user": person_b,
                    }
                },
            }
        expected = "key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\nkey6 3\nuser: 3\nfirst_name: 4\nlast_name: 4\nfather: 4\nfirst_name: 5\nlast_name: 5\nfather: 5\n"
        self.assert_stdout(data, expected)

    def test_empty_data(self):
        data = {}
        expected = "Empty Data Passed\n"
        self.assert_stdout(data, expected)

    def test_only_object(self):
        data = Person("User", "1", None)
        expected = "first_name: 1\nlast_name: 1\nfather: 1\n"
        self.assert_stdout(data, expected)

    def test_nested_object(self):
        person_a = Person("User", "1", None)
        person_b = Person("User", "2", person_a)

        expected = "first_name: 1\nlast_name: 1\nfather: 1\nfirst_name: 2\nlast_name: 2\nfather: 2\n"
        self.assert_stdout(person_b, expected)

    def test_nested_object_nested_dict(self):
        person_a = Person("User", "1", None)
        person_b = Person("User", "2", person_a)
        person_c = Person("User", "3", person_b)

        data = {"key1": {
                    "user": person_c
        }}
        expected = "key1 1\nuser: 2\nfirst_name: 3\nlast_name: 3\nfather: 3\nfirst_name: 4\nlast_name: 4\nfather: 4\nfirst_name: 5\nlast_name: 5\nfather: 5\n"
        self.assert_stdout(data, expected)

    def test_different_object(self):
        car_1 = Car(10, "CS", Car(30, "DFS", None))
        data = car_1

        expected = "price: 1\nmodel: 1\nsimilar: 1\nprice: 2\nmodel: 2\nsimilar: 2\n"
        self.assert_stdout(data, expected)



if __name__=="__main__":
    unittest.main()

