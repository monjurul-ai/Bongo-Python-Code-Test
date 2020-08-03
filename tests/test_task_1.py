from ..task_1 import print_depth


class TestTask1:

    def test_empty(self, capsys):
        data = {}
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == ""
        assert err == ""

    def test_single_element(self, capsys):
        data = {
            "test": 1
        }
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == "test 1\n"
        assert err == ""

    def test_nested_data(self, capsys):
        data = {
            "one": {
                "two": "three"
            }
        }
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == (
            "one 1\n"
            "two 2\n"
        )
        assert err == ""

    def test_complex_data(self, capsys):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == (
            "key1 1\n"
            "key2 1\n"
            "key3 2\n"
            "key4 2\n"
            "key5 3\n"
        )
        assert err == ""
