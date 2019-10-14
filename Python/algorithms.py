# -*- coding: utf-8 -*-

import unittest

"""
Compare x with the middle element.
If x matches with middle element, we return the mid index.
Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
Else (x is smaller) recur for the left half.
"""
class BinarySearch():

    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def result(self):
        return self.__search(self.arr, self.target, 0, len(self.arr)-1)

    def __search(self, arr, target, left_bound, right_bound):
        if right_bound >= left_bound:

            mid = int(left_bound + ((right_bound-left_bound) / 2))

            if arr[mid] == target:
                return mid

            elif arr[mid] > target:
                return self.__search(arr, target, left_bound, mid-1)

            elif arr[mid] < target:
                return self.__search(arr, target, mid + 1, right_bound)

        else:
            # Element not exist
            return -1


"""
A simple approach is to do linear search, i.e

Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
If x matches with an element, return the index.
If x doesn’t match with any of elements, return -1.
"""

class LinearSearch():

    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def result(self):
        return self.__search(self.arr, self.target)

    def __search(self, arr, target):
        for i in range(len(self.arr)):
            if self.arr[i] == self.target:
                return i
        return -1


class Test(unittest.TestCase):

    def test_binary_search(self):
        arr = [x for x in range(100)];
        for i in range(100):
            self.assertEqual(BinarySearch(arr, i).result(), i)
        for i in range(100):
            i += 200
            self.assertEqual(BinarySearch(arr, i).result(), -1)

    def test_linear_search(self):
        arr = [x for x in range(100)];
        for i in range(100):
            self.assertEqual(LinearSearch(arr, i).result(), i)
        for i in range(100):
            i += 200
            self.assertEqual(LinearSearch(arr, i).result(), -1)


if __name__ == "__main__":
    unittest.main()
