import pytest
from data_structures.linked_list import LinkedList


def test_exists():
    assert LinkedList


# @pytest.mark.skip("TODO")
def test_instantiate():
    assert LinkedList()


# @pytest.mark.skip("TODO")
def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


# @pytest.mark.skip("TODO")
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


# @pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "NULL"


# @pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_to_string_double():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_includes_true():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")


# @pytest.mark.skip("TODO")
def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")


## New Test 01


def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert(1)

    linked_list.insert(2)

    assert str(linked_list) == "{ 2 } -> { 1 } -> { banana } -> { apple } -> NULL"


## New Test 02


def test_includes_boolean():
    linked_list = LinkedList()

    linked_list.insert("apple")
    linked_list.insert("banana")
    assert not linked_list.includes(False)


## New Test 03

def test_insert_array():
    linked_list = LinkedList()
    linked_list.insert([])
    assert linked_list.head.value == []


def test_to_string_one():
    linked_list = LinkedList()
    linked_list.insert("None")
    assert str(linked_list) == "{ None } -> NULL"


def test_to_string_two():
    linked_list = LinkedList()
    linked_list.insert("Node(banana)")
    assert str(linked_list) == "{ Node(banana) } -> NULL"


def test_includes_false_two():
    linked_list = LinkedList()
    linked_list.insert("banana")
    assert not linked_list.includes(None)
