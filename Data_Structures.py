import unittest
import bisect


"""
https://docs.python.org/3/tutorial/datastructures.html?highlight=lists
http://thomas-cokelaer.info/tutorials/python/lists.html
"""
class Lists():

    def __init__(self, list):
        self.list = list

    def append(self, x):
        # same as self.list[len(self.list):] = [x]
        # self.list.insert(len(self.list), x)
        return self.list.append(x)

    def extend(self, list):
        return self.list.extend(list)

    def insert(self, index, value):
        return self.list.insert(index, value)

    def remove(self, x):
        """Removes the first item from the list whose value is equal to x.
        It raises a ValueError if there is no such item.
        """
        return self.list.remove(x)

    def pop(self, index=None):
        """Remove the item at the given position in the list, and return it.
        If no index is specified, a.pop() removes and returns the last item in the list
        """
        return self.list.pop() if index is None else self.list.pop(index)

    def clear(self):
        """Remove all items from the list.
        Equivalent to del self.list[:]
        """
        return self.list.clear()

    def len(self):
        return len(self.list)

    def index(self, value, start=None, end=None):
        """Return zero-based index in the list of the first item whose value is equal to x.
        Raises a ValueError if there is no such item.
        The optional arguments start and end are interpreted as in the slice notation and
        are used to limit the search to a particular subsequence of the list.
        """
        if start is not None and end is not None:
            return self.list.index(value, start, end)
        return self.list.index(value)


    def count(self, value):
        """Return the number of times x appears in the list."""
        return self.list.count(value)

    def reverse(self):
        """Reverse the elements of the list in place."""
        return self.list.reverse()

    def copy(self):
        """Return a shallow copy of the list. Equivalent to a[:]"""
        return self.list.copy()

    def sort(self, reverse=False):
        return self.list.sort(reverse=reverse)

    def insort(self, value):
        """Inserting items into a sorted list"""
        return bisect.insort(self.list, value)

    def bisect(self, value):
        """Inserting items into a sorted list and get the index"""
        index = bisect.bisect(self.list, value)
        return self.list.insert(index, value)

    def get_list(self):
        return self.list


class Tuples():
    pass


class Dicts():
    pass


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


if __name__ == "__main__":
    unittest.main()
