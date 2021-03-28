import io
from Q1_print_depth import print_depth
import unittest.mock

class TestQ1(unittest.TestCase):
    # Reusable helper method for testing print
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, data, expected_output, mock_stdout):
        print_depth(data)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_empty_data(self):
        data = {}
        expected = "Empty Dictionary Passed\n"
        self.assert_stdout(data, expected)

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

    def test_mixed_depth(self):
        data = {"key1": 1,
                "key2": {
                    "key4":{
                        "key6":23
                    }
                },
                "key3": {
                    "key7":{
                        "key9":1
                    }
                }}
        expected = "key1 1\nkey2 1\nkey3 1\nkey4 2\nkey7 2\nkey6 3\nkey9 3\n"
        self.assert_stdout(data, expected)


if __name__=="__main__":
    unittest.main()

