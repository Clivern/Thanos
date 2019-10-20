import unittest
import bisect
from heapq import *


"""
https://www.freecodecamp.org/news/the-top-data-structures-you-should-know-for-your-next-coding-interview-36af0831f5e3/
https://docs.python.org/3/tutorial/datastructures.html?highlight=lists
http://thomas-cokelaer.info/tutorials/python/lists.html

Python’s built-in list type makes a decent stack data structure as it supports push and pop operations in amortized O(1) time.
https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues
https://www.hackerrank.com/challenges/30-queues-stacks/problem
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


class Queue():

    def __init__(self):
        self.queue = []

    def enqueueCharacter(self, char):
        self.queue.insert(0, char)

    def dequeueCharacter(self):
        return self.queue.pop()

    def __repr__(self):
        return str(self.queue)


class Stack():

    def __init__(self):
        self.stack = []

    def pushCharacter(self, char):
        self.stack.append(char)

    def popCharacter(self):
        return self.stack.pop()

    def __repr__(self):
        return str(self.stack)


class Heap():

    def __init__(self):
        self.heap = []

    def heappush(self, item):
        """Push the value item onto the heap, maintaining the heap invariant."""
        heappush(self.heap, item)

    def heappop(self):
        """Pop and return the smallest item from the heap, maintaining the heap invariant."""
        return heappop(self.heap)

    def heappushpop(self, item):
        """Push item on the heap, then pop and return the smallest item from the heap."""
        return heappushpop(self.heap, item)

    def heapreplace(self, item):
        """
        Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change.
        If the heap is empty, IndexError is raised.
        """
        return heapreplace(self.heap, item)

    def size(self):
        return len(self.heap)

    def heapsort(self):
        h = []
        for value in self.heap:
            heappush(h, value)
        self.heap = [heappop(h) for i in range(len(h))]

    def __repr__(self):
        return str(self.heap)


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


"""
Strings are immutable sequence of characters

http://thomas-cokelaer.info/tutorials/python/strings.html
https://docs.python.org/3/library/stdtypes.html#string-methods
"""
class Strings():

    def __init__(self, elem):
        self.elem = elem

    def get(self, index):
        return self.elem[index]

    def len(self):
        return len(self.elem)

    def count(self, char, start, end):
        return self.elem.count(char, start, end)

    def isdigit(self):
        return self.elem.isdigit()

    def isalpha(self):
        return self.elem.isalpha()

    def islower(self):
        return self.elem.islower()

    def isupper(self):
        return self.elem.isupper()

    def istitle(self):
        return self.elem.istitle()

    def isspace(self):
        return self.elem.isspace()

    def isalnum(self):
        return self.elem.isalnum()

    def title(self):
        return self.elem.title()

    def capitalize(self):
        return self.elem.capitalize()

    def lower(self):
        return self.elem.lower()

    def upper(self):
        return self.elem.upper()

    def swapcase(self):
        return self.elem.swapcase()

    def center(self, lenght, fillchar=" "):
        return self.elem.center(lenght, fillchar)

    def ljust(self, lenght, fillchar=" "):
        return self.elem.ljust(lenght, fillchar)

    def rjust(self, lenght, fillchar=" "):
        return self.elem.rjust(lenght, fillchar)

    def zfill(self, lenght):
        return self.elem.zfill(lenght)

    def strip(self, chars):
        return self.elem.strip(chars)

    def rstrip(self, chars):
        return self.elem.rstrip(chars)

    def lstrip(self, chars):
        return self.elem.lstrip(chars)

    def endswith(self, suffix, start, end):
        return self.elem.endswith(suffix, start, end)

    def subexist(self, sub):
        return sub in self.elem

    def find(self, sub, start, end):
        return self.elem.find(sub, start, end)

    def get_string(self):
        return self.elem


"""
Linked Lists

A linked list is an ordered collection of values.
Linked lists are similar to arrays in the sense that they contain objects in a linear order.
However they differ from arrays in their memory layout.

Arrays are contiguous data structures and they’re composed of fixed-size data records stored in adjoining blocks of memory.
Linked lists, however, are made up of data records linked together by pointers.

https://dbader.org/blog/python-linked-list
"""
class SListNode():

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class DListNode():
    """
    A node in a doubly-linked list.
    """
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:

    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        self.head = SListNode(data=data, next=self.head)

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.

        https://www.hackerrank.com/challenges/30-linked-list/problem
        """
        if not self.head:
            self.head = SListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = SListNode(data=data)

    def insert(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = SListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = SListNode(data=data)

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        # Unlink it from the list
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node

    def remove_duplicates(self):
        """
        Your remove_duplicates function should return the head of the updated linked list. after removing duplicates

        https://www.hackerrank.com/challenges/30-linked-list-deletion/problem
        """
        if not self.head:
            return None
        n = self.head
        while n.next:
            if n.data == n.next.data:
                n.next = n.next.next
            else:
                n = n.next
        return self.head


class DoublyLinkedList():

    def __init__(self):
        """
        Create a new doubly linked list.
        Takes O(1) time.
        """
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        new_head = DListNode(data=data, next=self.head)
        if self.head:
            self.head.prev = new_head
        self.head = new_head

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = DListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = DListNode(data=data, prev=curr)

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def remove_elem(self, node):
        """
        Unlink an element from the list.
        Takes O(1) time.
        """
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        node.prev = None
        node.next = None

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        elem = self.find(key)
        if not elem:
            return
        self.remove_elem(elem)

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        while curr:
            prev_node = curr.prev
            curr.prev = curr.next
            curr.next = prev_node
            curr = curr.prev
        self.head = prev_node.prev


""""
Trees

Trees are well known as a non-linear Data Structure. It doesn’t store data in a linear way. It organizes data in a hierarchical way.

- Root: the topmost node of the tree
- Edge: the link between 2 nodes
- Child: a node that has a parent node
- Parent: a node that has an edge to a child node
- Leaf: a node that does not have a child node in the tree
- Height: The height of a tree is the length of the longest path to a leaf.
- Depth: The depth of a node is the length of the path to its root.

Binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child

Ref --> https://medium.com/the-renaissance-developer/learning-tree-data-structure-27c6bb363051
"""
class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child:
            node = BinaryTree(value)
            node.left_child = self.left_child
            self.left_child = node
        else:
            self.left_child = BinaryTree(value)

    def insert_right(self, value):
        if self.right_child:
            node = BinaryTree(value)
            node.right_child = self.right_child
            self.right_child = node
        else:
            self.right_child = BinaryTree(value)


class Sets():
    pass


class Frozensets():
    pass


class Collections():
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

    def test_queue(self):
        queue = Queue()
        queue.enqueueCharacter("A")
        queue.enqueueCharacter("B")
        queue.enqueueCharacter("C")
        self.assertEqual(queue.dequeueCharacter(), "A")
        self.assertEqual(str(queue), "['C', 'B']")

    def test_stack(self):
        stack = Stack()
        stack.pushCharacter("A")
        stack.pushCharacter("B")
        stack.pushCharacter("C")
        self.assertEqual(stack.popCharacter(), "C")
        self.assertEqual(str(stack), "['A', 'B']")

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

    def test_heap(self):
        heap = Heap()
        heap.heappush("E")
        heap.heappush("D")
        heap.heappush("C")
        heap.heappush("B")
        self.assertEqual(heap.heappop(), "B")
        self.assertEqual(heap.heappop(), "C")
        self.assertEqual(heap.size(), 2)
        self.assertEqual(heap.heappushpop("A"), "A") # Will add A and then remove it again
        self.assertEqual(str(heap), "['D', 'E']")

        heap1 = Heap()
        heap1.heappush(9)
        heap1.heappush(2)
        heap1.heappush(1)
        heap1.heappush(7)
        heap1.heapsort()
        self.assertEqual(heap1.size(), 4)
        self.assertEqual(heap1.heapreplace(0), 1) # will remove smallest 1 then add 0
        self.assertEqual(str(heap1), '[0, 2, 7, 9]')


if __name__ == "__main__":
    unittest.main()
