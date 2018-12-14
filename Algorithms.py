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


    def Result(self):
        return self.Search(self.arr, self.target, 0, len(self.arr)-1)

    def Search(self, arr, target, left_bound, right_bound):
        if right_bound >= left_bound:

            mid = int(left_bound + ((right_bound-left_bound) / 2))

            if arr[mid] == target:
                return mid

            elif arr[mid] > target:
                return self.Search(arr, target, left_bound, mid-1)

            elif arr[mid] < target:
                return self.Search(arr, target, mid + 1, right_bound)

        else:
            # Element not exist
            return -1


class Test(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(BinarySearch([1,2,3,4,5,6,7,8,9,10], 30).Result(), -1)
        self.assertEqual(BinarySearch([1,2,3,4,5,6,7,8,9,10], 20).Result(), -1)
        self.assertEqual(BinarySearch([1,2,3,4,5,6,7,8,9,10], 1).Result(), 0)
        self.assertEqual(BinarySearch([1,2,3,4,5,6,7,8,9,10], 2).Result(), 1)
        self.assertEqual(BinarySearch([1,2,3,4,5,6,7,8,9,10], 3).Result(), 2)
        self.assertEqual(BinarySearch([1,2,3,4,5,6,7,8,9,10], 4).Result(), 3)
        self.assertEqual(BinarySearch([1,2,3,4,5,6,7,8,9,10], 5).Result(), 4)
        self.assertEqual(BinarySearch([1,2,3,4,5,6,7,8,9,10], 6).Result(), 5)
        self.assertEqual(BinarySearch([1,2,3,4,5,6,7,8,9,10], 7).Result(), 6)
        self.assertEqual(BinarySearch([1,2,3,4,5,6,7,8,9,10], 8).Result(), 7)
        self.assertEqual(BinarySearch([1,2,3,4,5,6,7,8,9,10], 9).Result(), 8)
        self.assertEqual(BinarySearch([1,2,3,4,5,6,7,8,9,10], 10).Result(), 9)


if __name__ == "__main__":
    unittest.main()
