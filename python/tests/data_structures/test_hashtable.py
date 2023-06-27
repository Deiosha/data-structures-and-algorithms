import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


def test_hashtable():
    hashtable = Hashtable()

    # Test set() and get() methods
    hashtable.set("name", "John")
    assert hashtable.get("name") == "John"


def test_hashtable_4():
    hashtable = Hashtable()

    hashtable.set("name", "John")
    assert hashtable.get("name") == "John"

    hashtable.set("age", 25)
    assert hashtable.get("age") == 25

# @pytest.mark.skip("TODO")
# def test_internals():
#     hashtable = Hashtable(1024)
#     hashtable.set("ahmad", 30)
#     hashtable.set("silent", True)
#     hashtable.set("listen", "to me")
#
#     actual = []
#
#     # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
#     for item in hashtable._buckets:
#         if item:
#             actual.append(item.display())
#
#     expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]
#
#     assert actual == expected\
