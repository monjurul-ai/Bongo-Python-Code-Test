import pytest

from ..task_2 import print_depth, Person


class TestTask1:

    @pytest.fixture
    def person_a(self):
        return Person("Paige", "Turner", None)

    @pytest.fixture
    def person_b(self, person_a):
        return Person("Walter", "Melon", person_a)

    def test_empty(self, capsys):
        data = {}
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == ""
        assert err == ""

    def test_single_dict(self, capsys):
        data = {
            "test": 1
        }
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == "test 1\n"
        assert err == ""

    def test_nested_dict(self, capsys):
        data = {
            "Turner": {
                "Melon": "three"
            }
        }
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == (
            "Turner 1\n"
            "Melon 2\n"
        )
        assert err == ""

    def test_multi_nested_dict(self, capsys):
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

    def test_single_person(self, capsys, person_a):
        print_depth(person_a)
        out, err = capsys.readouterr()
        assert out == (
            "Paige 1\n"
            "Turner 1\n"
            "None 1\n"
        )
        assert err == ""

    def test_nested_person(self, capsys, person_b):
        print_depth(person_b)
        out, err = capsys.readouterr()
        assert out == (
            "Walter 1\n"
            "Melon 1\n"
            "Paige Turner 1\n"
            "Paige 2\n"
            "Turner 2\n"
            "None 2\n"
        )
        assert err == ""

    def test_mixed_data(self, capsys, person_b):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": person_b,
                }
            },
        }
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == (
            "key1 1\n"
            "key2 1\n"
            "key3 2\n"
            "key4 2\n"
            "key5 3\n"
            "user 3\n"
            "Walter 4\n"
            "Melon 4\n"
            "Paige Turner 4\n"
            "Paige 5\n"
            "Turner 5\n"
            "None 5\n"
        )
        assert err == ""
