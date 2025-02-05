import pytest

from .natural_sort import natural_compare, natural_sort

class TestNaturalCompare:
    def test_alpha(self):
        assert natural_compare("a", "b") == -1
        assert natural_compare("b", "a") == 1
        assert natural_compare("a", "a") == 0

    def test_num_single(self):
        assert natural_compare("1", "2") == -1
        assert natural_compare("2", "1") == 1
        assert natural_compare("1", "1") == 0

    def test_num(self):
        assert natural_compare("10", "2") == 1
        assert natural_compare("2", "10") == -1
        assert natural_compare("10", "10") == 0

        # 123 > 30
        assert natural_compare("123", "30") == 1
        # 30 < 123
        assert natural_compare("30", "123") == -1

    def test_alpha_num(self):
        assert natural_compare("a1", "a2") == -1
        assert natural_compare("a2", "a1") == 1
        assert natural_compare("a1", "a1") == 0

    def test_num_alpha(self):
        assert natural_compare("1a", "2a") == -1
        assert natural_compare("2a", "1a") == 1
        assert natural_compare("1a", "1a") == 0


class TestNaturalSort:
    def test_alpha(self):
        assert natural_sort(["a", "b", "c"]) == ["a", "b", "c"]
        assert natural_sort(["b", "a", "c"]) == ["a", "b", "c"]
        assert natural_sort(["c", "b", "a"]) == ["a", "b", "c"]

    def test_num_single(self):
        assert natural_sort(["1", "2", "3"]) == ["1", "2", "3"]
        assert natural_sort(["2", "1", "3"]) == ["1", "2", "3"]
        assert natural_sort(["3", "2", "1"]) == ["1", "2", "3"]

    def test_num(self):
        assert natural_sort(["10", "2"]) == ["2", "10"]
        assert natural_sort(["2", "10"]) == ["2", "10"]

    def test_alpha_num(self):
        assert natural_sort(["a1", "a2"]) == ["a1", "a2"]
        assert natural_sort(["a2", "a1"]) == ["a1", "a2"]

    def test_num_alpha(self):
        assert natural_sort(["1a", "2a"]) == ["1a", "2a"]
        assert natural_sort(["2a", "1a"]) == ["1a", "2a"]

    def test_mixed(self):
        assert natural_sort(["10b","10","10c","9","9b","9c","9d","10d","10e","11","12","13","14","15","16","17","18","19","20"]) == ['9', '9b', '9c', '9d', '10', '10b', '10c', '10d', '10e', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']