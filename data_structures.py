import unittest
import bisect


"""
https://docs.python.org/3/tutorial/datastructures.html?highlight=lists
http://thomas-cokelaer.info/tutorials/python/lists.html
"""
class Lists():

    def __init__(self, elem):
        self.elem = elem

    def append(self, x):
        # same as self.elem[len(self.elem):] = [x]
        # self.elem.insert(len(self.elem), x)
        return self.elem.append(x)

    def extend(self, elem):
        return self.elem.extend(elem)

    def insert(self, index, value):
        return self.elem.insert(index, value)

    def remove(self, x):
        """Removes the first item from the list whose value is equal to x.
        It raises a ValueError if there is no such item.
        """
        return self.elem.remove(x)

    def pop(self, index=None):
        """Remove the item at the given position in the list, and return it.
        If no index is specified, a.pop() removes and returns the last item in the list
        """
        return self.elem.pop() if index is None else self.elem.pop(index)

    def clear(self):
        """Remove all items from the list.
        Equivalent to del self.elem[:]
        """
        return self.elem.clear()

    def len(self):
        return len(self.elem)

    def index(self, value, start=None, end=None):
        """Return zero-based index in the list of the first item whose value is equal to x.
        Raises a ValueError if there is no such item.
        The optional arguments start and end are interpreted as in the slice notation and
        are used to limit the search to a particular subsequence of the list.
        """
        if start is not None and end is not None:
            return self.elem.index(value, start, end)
        return self.elem.index(value)

    def count(self, value):
        """Return the number of times x appears in the list."""
        return self.elem.count(value)

    def reverse(self):
        """Reverse the elements of the list in place."""
        return self.elem.reverse()

    def copy(self):
        """Return a shallow copy of the list. Equivalent to a[:]"""
        return self.elem.copy()

    def sort(self, reverse=False):
        return self.elem.sort(reverse=reverse)

    def insort(self, value):
        """Inserting items into a sorted list"""
        return bisect.insort(self.elem, value)

    def bisect(self, value):
        """Inserting items into a sorted list and get the index"""
        index = bisect.bisect(self.elem, value)
        return self.elem.insert(index, value)

    def get_list(self):
        return self.elem

"""
A tuple is similar to a list. The difference between the two is that we cannot change the elements of a tuple once
it is assigned whereas in a list, elements can be changed.

- We generally use tuple for heterogeneous (different) datatypes and list for homogeneous (similar) datatypes.
- Since tuple are immutable, iterating through tuple is faster than with list. So there is a slight performance boost.
- Tuples that contain immutable elements can be used as key for a dictionary. With list, this is not possible.
- If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

https://www.programiz.com/python-programming/tuple
http://thomas-cokelaer.info/tutorials/python/tuples.html
"""
class Tuples():

    def __init__(self, elem):
        self.elem = elem

    def len(self):
        return len(self.elem)

    def sum(self):
        """Retrun the sum of all elements in the tuple."""
        return sum(self.elem)

    def enumerate(self):
        """Return an enumerate object. It contains the index and value of all the items of tuple as pairs."""
        return enumerate(self.elem)

    def max(self):
        """Return the largest item in the tuple."""
        return max(self.elem)

    def min(self):
        """Return the smallest item in the tuple"""
        return min(self.elem)

    def all(self):
        """Return True if all elements of the tuple are true (or if the tuple is empty)."""
        return all(self.elem)

    def any(self):
        """Return True if any element of the tuple is true. If the tuple is empty, return False."""
        return any(self.elem)

    def sort(self, reverse=False):
        return sorted(self.elem, reverse=reverse)

    def covert(self, list):
        return tuple(list)

    def exists(self, item):
        return item in self.elem

    def count(self, item):
        """Return the number of items that is equal to item"""
        return self.elem.count(item)

    def index(self, item):
        """Return index of first item that is equal to item"""
        return self.elem.index(item)

    def get(self, index):
        return self.elem[index]

    def get_tuple(self):
        return self.elem


class Dicts():

    def __init__(self, elem):
        self.elem = elem

    def len(self):
        return len(self.elem)

    def keys(self):
        return self.elem.keys()

    def values(self):
        return self.elem.values()

    def items(self):
        return self.elem.items()

    def get(self, key):
        return self.elem.get(key)

    def has(self, key):
        return key in self.elem.keys()

    def pop(self, key):
        return self.elem.pop(key)

    def popitem(self):
        return self.elem.popitem()

    def clear(self):
        return self.elem.clear()

    def update(self, dic):
        return self.elem.update(dic)

    def from_keys(self, list):
        return self.elem.fromkeys(list)

    def new_from_keys(self, list):
        return {}.fromkeys(list)

    def get_dict(self):
        return self.elem

class Strings():
    pass


class Sets():
    pass


class Frozensets():
    pass


class Collections():
    pass


class Heapq():
    pass


class Test(unittest.TestCase):

    def test_dicts(self):
        adic = Dicts({"A": 1, "B": 2, "C": 3})
        self.assertEqual(adic.len(), 3)
        self.assertEqual(list(adic.keys()), ["A", "B", "C"])
        self.assertEqual(list(adic.values()), [1, 2, 3])
        self.assertEqual(list(adic.items()), [("A", 1), ("B", 2), ("C", 3)])
        self.assertEqual(adic.get("C"), 3)
        self.assertEqual(adic.has("C"), True)

        self.assertEqual(adic.pop("C"), 3)
        self.assertEqual(adic.get_dict(), {"A": 1, "B": 2})
        self.assertEqual(adic.popitem(), ("B", 2))
        self.assertEqual(adic.get_dict(), {"A": 1})
        self.assertEqual(adic.clear(), None)
        self.assertEqual(adic.get_dict(), {})
        self.assertEqual(adic.update({"A": 1}), None)
        self.assertEqual(adic.get_dict(), {"A": 1})
        self.assertEqual(adic.from_keys(["H", "K"]), {"H": None, "K": None})
        self.assertEqual(adic.new_from_keys(["H", "K"]), {"H": None, "K": None})

    def test_lists(self):
        alist = Lists([1, 2, 3, 4])
        self.assertEqual(alist.get_list(), [1, 2, 3, 4])
        self.assertEqual(alist.append(5), None)
        self.assertEqual(alist.get_list(), [1, 2, 3, 4, 5])
        self.assertEqual(alist.extend([6, 7, 8]), None)
        self.assertEqual(alist.get_list(), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(alist.insert(0, 0), None)
        self.assertEqual(alist.insert(alist.len(), 9), None)
        self.assertEqual(alist.get_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(alist.remove(0), None)
        self.assertEqual(alist.remove(9), None)
        self.assertEqual(alist.get_list(), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(alist.pop(0), 1)
        self.assertEqual(alist.pop(6), 8)
        self.assertEqual(alist.pop(), 7)
        self.assertEqual(alist.get_list(), [2, 3, 4, 5, 6])
        self.assertEqual(alist.len(), 5)
        self.assertEqual(alist.clear(), None)
        self.assertEqual(alist.len(), 0)
        self.assertEqual(alist.get_list(), [])

        blist = Lists(["A", "a", "A", "b", "B", "B", "C", "C", "H", "B"])
        self.assertEqual(blist.count("B"), 3)
        self.assertEqual(blist.index("B"), 4)
        self.assertEqual(blist.index("B", 5, blist.len()), 5)

        clist = Lists(["A", "B", "C"])
        self.assertEqual(clist.reverse(), None)
        self.assertEqual(clist.get_list(), ["C", "B", "A"])
        self.assertEqual(clist.sort(), None)
        self.assertEqual(clist.get_list(), ["A", "B", "C"])
        self.assertEqual(clist.sort(True), None)
        self.assertEqual(clist.get_list(), ["C", "B", "A"])
        self.assertEqual(clist.copy(), ["C", "B", "A"])

        dlist = Lists(["A", "B", "C", "F"])
        self.assertEqual(dlist.insort("E"), None)
        self.assertEqual(dlist.insort("D"), None)
        self.assertEqual(dlist.get_list(), ["A", "B", "C", "D", "E", "F"])

        elist = Lists(["A", "B", "C", "E"])
        self.assertEqual(elist.bisect("D"), None)
        self.assertEqual(elist.get_list(), ["A", "B", "C", "D", "E"])

    def test_tuples(self):
        atuple = Tuples((1, 2, 3, 4, 5))
        self.assertEqual(atuple.get_tuple(), (1, 2, 3, 4, 5))
        self.assertEqual(atuple.get(1), 2)
        self.assertEqual(atuple.index(1), 0)
        self.assertEqual(atuple.count(5), 1)
        self.assertEqual(atuple.exists(5), True)
        self.assertEqual(atuple.covert([1, 2, 3, 4, 5]), atuple.get_tuple())
        self.assertEqual(atuple.min(), 1)
        self.assertEqual(atuple.max(), 5)
        self.assertEqual(atuple.len(), 5)
        self.assertEqual(atuple.sum(), 15)
        self.assertEqual(list(atuple.enumerate()), [(0,1), (1, 2), (2, 3), (3, 4), (4, 5)])
        self.assertEqual(atuple.sort(False), [1, 2, 3, 4, 5])
        self.assertEqual(atuple.sort(True), [5, 4, 3, 2, 1])
        self.assertEqual(atuple.any(), True)
        self.assertEqual(atuple.all(), True)
        btuple = Tuples((True, True, True, False))
        self.assertEqual(btuple.any(), True)
        self.assertEqual(btuple.all(), False)


if __name__ == "__main__":
    unittest.main()
