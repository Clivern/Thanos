import unittest

"""
Implement an algorithm to determine if a string has all unique characters.
"""
class Problem1():

    def has_duplicates1(self, text):
        letters = {}
        for letter in text:
            index = ord(letter)
            if index in letters.keys():
                return True
            letters[index] = True

        return False


    def has_duplicates2(self, text):
        if len(text) > 128:
            return False

        letters = [False]*128
        for letter in text:
            index = ord(letter)
            if letters[index]:
                return True
            letters[index] = True

        return False


"""

Steve has a string of lowercase characters in range ascii[‘a’..’z’].
He wants to reduce the string to its shortest length by doing a series of operations.
In each operation he selects a pair of adjacent lowercase letters that match, and he deletes them.
For instance, the string aab could be shortened to b in one operation.

Steve’s task is to delete as many characters as possible using this method and print the resulting string.
If the final string is empty, print Empty String

https://www.hackerrank.com/challenges/reduced-string/problem
"""
class Problem2():

    def superReducedString(self, s):
        stack = []
        for i in range(len(s)):
            if len(stack) == 0 or s[i] != stack[-1]:
                stack.append(s[i])
            else:
                stack.pop()
        return 'Empty String' if len(stack) == 0 else ''.join(stack)


"""
Calculate Words on camelCase

https://www.hackerrank.com/challenges/camelcase/problem
"""
class Problem3():

    def camelcase(self, s):
        i = 1 if s else 0
        for letter in s:
            if letter.isupper():
                i += 1
        return i


"""
Louise joined a social networking site to stay in touch with her friends.
The signup page required her to input a name and a password. However, the password must be strong.
The website considers a password to be strong if it satisfies the following criteria:

Its length is at least .
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length  in the password field but wasn't sure if it was strong.
Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

https://www.hackerrank.com/challenges/strong-password/problem
"""
class Problem4():

    def minimumNumber(self, password):
        # Return the minimum number of characters to make the password strong
        points = {
            "lower": 0,
            "upper": 0,
            "special": 0,
            "digit": 0
        }
        for letter in password:
            if letter.isdigit():
                points["digit"] += 1
            if letter.islower():
                points["lower"] += 1
            if letter.isupper():
                points["upper"] += 1
            if letter in "!@#$%^&*()-+":
                points["special"] += 1

        needed = 0
        for key, value in points.items():
            if value == 0:
                needed += 1
        if len(password) >= 6:
            return needed
        else:
            return needed if (6-len(password)) < needed else (6-len(password))


"""
Consider a staircase of size :

   #
  ##
 ###
####
Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .

https://www.hackerrank.com/challenges/staircase/problem
"""
class Problem5():

    def staircase(self, n):
        for i in range(n):
            print(("#" * (i+1)).rjust(n, " "))


"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

https://www.hackerrank.com/challenges/mini-max-sum/problem
"""
class Problem6():

    def minMax(self, arr):
        arr.sort()
        return sum(arr[:-1]), sum(arr[1:])


"""
You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age.
When she blows out the candles, she’ll only be able to blow out the tallest ones.
Your task is to find out how many candles she can successfully blow out.

Sample Input 0
3 2 1 3

Sample Output 0
2

https://www.hackerrank.com/challenges/birthday-cake-candles/problem
"""
class Problem7():

    def birthdayCakeCandles(self, ar):
        ar.sort(reverse=True)
        return ar.count(ar[0])

class Problem8():

    def solution(self, A, B):
        # brute force solution
        # holds intervals that overlap and don't overlap (disjoint)
        pairs = []
        # pairs that already overlap with another pairs
        overlapped = []
        i = 0
        for item in A:
            x, y = A[i], B[i]
            h = i + 1
            disjoint = True
            for other in A[h:]:
                z, k = A[h], B[h]
                if ((x >= z and x <= k) or (y >= z and y <= k)) and ((z, k) not in overlapped):
                    disjoint = False
                    # add to overlapped pairs
                    overlapped.append((z,k))
                    # add the union to intervals that overlap
                    pairs.append((min(x, z), max(y, k)))
                h += 1
            # Check if it is a disjoint and didn't overlap before
            if disjoint and ((x,y) not in overlapped):
                # add to the disjoint itervals
                pairs.append((x,y))
            i += 1
        return len(pairs)


"""
Binary gap calculator

https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
"""
class Problem9():

    def solution(self, N):
        bin_rep = str(bin(N))
        bin_rep = bin_rep.strip("0b")
        max_len = 0
        for zeros in bin_rep.split("1"):
            if len(zeros) > max_len:
                max_len = len(zeros)
        return max_len


"""
OddOccurrencesInArray

https://www.programiz.com/java-programming/bitwise-operators
https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
"""
class Problem10():

    def solution(self, A):
        result = 0
        for number in A:
            result ^= number
        return result


"""
CyclicRotation

https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
"""
class Problem11():

    def solution(self, A, K):
        # write your code in Python 3.6
        i = 0
        new = list(range(len(A)))
        for item in A:
            position = i+K
            if position >= len(A):
                while position >= len(A):
                    position = position-len(A)
                new[position] = item
            else:
                new[i+K] = item
            i += 1
        return new


"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3,
which leads to [1,2,3,1,2,3]
"""
class Problem12():

    def solution(self, arr, n):
        result = []
        for i in arr:
            if result.count(i) < n:
                result.append(i)
        return result


"""
There is a parking lot with only one empty spot. Given the initial state
of the parking lot and the final state. Each step we are only allowed to
move a car
out of its place and move it into the empty spot.
The goal is to find out the least movement needed to rearrange
the parking lot from the initial state to the final state.

Say the initial state is an array:

[1, 2, 3, 0, 4],
where 1, 2, 3, 4 are different cars, and 0 is the empty spot.

And the final state is

[0, 3, 2, 1, 4].
We can swap 1 with 0 in the initial array to get [0, 2, 3, 1, 4] and so on.
Each step swap with 0 only.

Edit:
Now also prints the sequence of changes in states.
Output of this example :-

initial: [1, 2, 3, 0, 4]
final:   [0, 3, 2, 1, 4]
Steps =  4
Sequence :
0 2 3 1 4
2 0 3 1 4
2 3 0 1 4
0 3 2 1 4
"""
class Problem13():

    def solution(self, initial, final):
        pass


"""
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
"""
class Problem14():

    def solution(self):
        pass


"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)
"""
class Problem15():

    def solution(self):
        pass


"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
    move_zeros([false, 1, 0, 1, 2, 0, 1, 3, "a"])
    returns => [false, 1, 1, 2, 1, 3, "a", 0, 0]
The time complexity of the below algorithm is O(n).
"""
class Problem16():

    def solution(self):
        pass


"""
Find the index of 0 to be replaced with 1 to get
longest continuous sequence
of 1s in a binary array.
Returns index of 0 to be
replaced with 1 to get longest
continuous sequence of 1s.
If there is no 0 in array, then
it returns -1.
e.g.
let input array = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
If we replace 0 at index 3 with 1, we get the longest continuous
sequence of 1s in the array.
So the function return => 3
"""
class Problem17():

    def solution(self):
        pass


"""
Given a string, find the length of the longest substring
without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""
class Problem18():

    def solution(self):
        pass


"""
This algorithm receives an array and returns most_frequent_value
Also, sometimes it is possible to have multiple 'most_frequent_value's,
so this function returns a list. This result can be used to find a
representative value in an array.
This algorithm gets an array, makes a dictionary of it,
 finds the most frequent count, and makes the result list.
For example: top_1([1, 1, 2, 2, 3, 4]) will return [1, 2]
(TL:DR) Get mathematical Mode
Complexity: O(n)
"""
class Problem19():

    def solution(self):
        pass


"""
Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators (not unary) +, -, or *
between the digits so they prevuate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""
class Problem20():

    def solution(self, nums, result):
        pass


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
        return str(self.data)


class DListNode():

    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return str(self.data)

class Problem21():

    def append(self, head, data):
        if not head:
            return SListNode(data)
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = SListNode(data)
        return head

    def insert(self, head, data):
        if not head:
            return SListNode(data)
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = SListNode(data)
        return head

    def prepend(self, head, data):
        if not head:
            return SListNode(data)
        node = SListNode(data)
        node.next = head
        return node

    def repr(self, head):
        nodes = []
        curr = head
        while curr:
            nodes.append(str(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def reverse(self, head):
        #
        # https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem
        #
        # def reverse(head):
        #     n = None
        #     while head:
        #         node = DoublyLinkedListNode(head.data)
        #         node.prev = head.prev
        #         node.next = n
        #         n = node
        #         head = head.next
        #     return n
        #
        if not head:
            return None
        n = None
        curr = head
        while curr:
            node = SListNode(curr.data)
            node.next = n
            n = node
            curr = curr.next
        return n

    def remove_duplicates(self, head):
        if not head:
            return None
        curr = head
        while curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

    def remove_data(self, head, data):
        if not head:
            return None
        curr = head
        if curr.data == data:
            return head.next if head.next else None
        while curr.next:
            if curr.next.data == data:
                if curr.next.next:
                    curr.next = curr.next.next
                else:
                    curr.next = None
                break
            curr = curr.next
        return head

    def remove_position(self, head, position, start=0):
        if not head:
            return None
        curr = head
        if start == position:
            if head.next:
                return head.next
            else:
                return None
        start += 1
        while curr.next:
            if position == start:
                if curr.next.next:
                    curr.next = curr.next.next
                else:
                    curr.next = None
                break
            start += 1
            curr = curr.next
        return head

    def insert_at_position(self, head, data, position, start=0):
        pass

    def find_data_position(self, head, data, start=0):
        if not head:
            return -1
        curr = head
        while curr:
            if curr.data == data:
                return start
            start += 1
            curr = curr.next
        return -1


"""
Key Based Sort
"""

class Problem22():

    def sort(self, data, callable, reverse=False):
        return sorted(data, key=callable, reverse=reverse)


"""
Tree: Preorder, Inorder and Postorder Traversal

https://www.hackerrank.com/challenges/tree-preorder-traversal/problem
https://www.hackerrank.com/challenges/tree-inorder-traversal/problem
https://www.hackerrank.com/challenges/tree-postorder-traversal/problem
"""
class Problem23():

    def preOrder(self, root):
        print(str(root.info) + " ", end="")
        if root.left:
            self.preOrder(root.left)
        if root.right:
            self.preOrder(root.right)

    def inOrder(self, root):
        if root.left:
            self.inOrder(root.left)
        print(str(root.info) + " ", end="")
        if root.right:
            self.inOrder(root.right)

    def postOrder(self, root):
        if root.left:
            self.postOrder(root.left)
        if root.right:
            self.postOrder(root.right)
        print(str(root.info) + " ", end="")


"""
Binary Tree Height

https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
"""
class Problem24():

    def height(self, root):
        if root:
            return 1 + max(
                self.height(root.left),
                self.height(root.right)
            )
        else:
            return -1


class Test(unittest.TestCase):

    def test_problem_1(self):
        for item in [('abcd'), ('s4fad'), ('')]:
            self.assertFalse(Problem1().has_duplicates1(item))

        for item in [('abacd'), ('s4f4ad'), ('dffgr')]:
            self.assertTrue(Problem1().has_duplicates1(item))

        for item in [('abcd'), ('s4fad'), ('')]:
            self.assertFalse(Problem1().has_duplicates2(item))

        for item in [('abacd'), ('s4f4ad'), ('dffgr')]:
            self.assertTrue(Problem1().has_duplicates2(item))

    def test_problem_2(self):
        self.assertEqual(Problem2().superReducedString("aaabccddd"), "abd")
        self.assertEqual(Problem2().superReducedString("aa"), "Empty String")
        self.assertEqual(Problem2().superReducedString("baab"), "Empty String")

    def test_problem_3(self):
        self.assertEqual(Problem3().camelcase("camelCase"), 2)

    def test_problem_4(self):
        self.assertEqual(Problem4().minimumNumber("Ab1"), 3)

    def test_problem_6(self):
        self.assertEqual(Problem6().minMax([1, 2, 3, 4, 5]), (10, 14))

    def test_problem_7(self):
        self.assertEqual(Problem7().birthdayCakeCandles([3, 2, 1, 3]), 2)

    def test_problem_8(self):
        self.assertEqual(Problem8().solution([1, 12, 42, 70, 36, -4, 43, 15], [5, 15, 44, 72, 36, 2, 69, 24]), 5)

    def test_problem_9(self):
        self.assertEqual(Problem9().solution(529), 4)

    def test_problem_10(self):
        self.assertEqual(Problem10().solution([9, 3, 9, 3, 9, 7, 9]), 7)

    def test_problem_11(self):
        self.assertEqual(Problem11().solution([1, 2, 3, 4, 5, 6, 7, 8], 1), [8, 1, 2, 3, 4, 5, 6, 7])

    def test_problem_12(self):
        self.assertEqual(Problem12().solution([1,2,3,1,2,1,2,3], 2), [1, 2, 3, 1, 2, 3])

    def test_problem_21(self):
        llist = None
        llist = Problem21().append(llist, 1) # add to end
        llist = Problem21().insert(llist, 2) # add to end
        llist = Problem21().append(llist, 3) # add to end
        llist = Problem21().prepend(llist, 0) # add to start

        self.assertEqual(Problem21().repr(llist), "[0, 1, 2, 3]")
        self.assertEqual(Problem21().repr(Problem21().reverse(llist)), "[3, 2, 1, 0]")

        # Remove duplicates
        llist = None
        llist = Problem21().append(llist, 1)
        llist = Problem21().append(llist, 1)
        llist = Problem21().append(llist, 2)
        llist = Problem21().append(llist, 3)
        llist = Problem21().append(llist, 4)
        llist = Problem21().append(llist, 4)
        llist = Problem21().append(llist, 4)
        llist = Problem21().append(llist, 5)
        self.assertEqual(Problem21().repr(llist), "[1, 1, 2, 3, 4, 4, 4, 5]")
        llist = Problem21().remove_duplicates(llist)
        self.assertEqual(Problem21().repr(llist), "[1, 2, 3, 4, 5]")

        # remove value
        llist = None
        llist = Problem21().append(llist, 1) # add to end
        llist = Problem21().insert(llist, 2) # add to end
        llist = Problem21().append(llist, 3) # add to end
        llist = Problem21().prepend(llist, 0) # add to start
        self.assertEqual(Problem21().repr(llist), "[0, 1, 2, 3]")
        llist = Problem21().remove_data(llist, 0)
        self.assertEqual(Problem21().repr(llist), "[1, 2, 3]")
        llist = Problem21().remove_data(llist, 1)
        self.assertEqual(Problem21().repr(llist), "[2, 3]")
        llist = Problem21().remove_data(llist, 2)
        self.assertEqual(Problem21().repr(llist), "[3]")
        llist = Problem21().remove_data(llist, 3)
        self.assertEqual(Problem21().repr(llist), "[]")

        llist = None
        llist = Problem21().append(llist, 1) # add to end
        llist = Problem21().insert(llist, 2) # add to end
        llist = Problem21().append(llist, 3) # add to end
        llist = Problem21().prepend(llist, 0) # add to start
        self.assertEqual(Problem21().find_data_position(llist, 0), 0)
        self.assertEqual(Problem21().find_data_position(llist, 1), 1)
        self.assertEqual(Problem21().find_data_position(llist, 2), 2)
        self.assertEqual(Problem21().find_data_position(llist, 3), 3)
        self.assertEqual(Problem21().find_data_position(llist, 4), -1)

        llist = None
        llist = Problem21().append(llist, 1) # add to end
        llist = Problem21().insert(llist, 2) # add to end
        llist = Problem21().append(llist, 3) # add to end
        llist = Problem21().prepend(llist, 0) # add to start
        llist = Problem21().remove_position(llist, 3)
        self.assertEqual(Problem21().repr(llist), "[0, 1, 2]")
        llist = Problem21().remove_position(llist, 2)
        self.assertEqual(Problem21().repr(llist), "[0, 1]")
        llist = Problem21().remove_position(llist, 1)
        self.assertEqual(Problem21().repr(llist), "[0]")
        llist = Problem21().remove_position(llist, 0)
        self.assertEqual(Problem21().repr(llist), "[]")

    def test_problem_22(self):
        data = [
            {"id": 3, "title": "B", "rate": 3},
            {"id": 2, "title": "A", "rate": 9},
            {"id": 1, "title": "C", "rate": 8},
            {"id": 9, "title": "E", "rate": 5},
            {"id": 7, "title": "D", "rate": 4},
            {"id": 8, "title": "F", "rate": 6},
            {"id": 6, "title": "G", "rate": 7},
            {"id": 5, "title": "H", "rate": 1},
            {"id": 4, "title": "I", "rate": 2},
            {"id": 10, "title": "J", "rate": 10}
        ]
        self.assertEqual(Problem22().sort(data, lambda x: x['id']), [
            {'id': 1, 'title': 'C', 'rate': 8},
            {'id': 2, 'title': 'A', 'rate': 9},
            {'id': 3, 'title': 'B', 'rate': 3},
            {'id': 4, 'title': 'I', 'rate': 2},
            {'id': 5, 'title': 'H', 'rate': 1},
            {'id': 6, 'title': 'G', 'rate': 7},
            {'id': 7, 'title': 'D', 'rate': 4},
            {'id': 8, 'title': 'F', 'rate': 6},
            {'id': 9, 'title': 'E', 'rate': 5},
            {'id': 10, 'title': 'J', 'rate': 10}
        ])
        self.assertEqual(Problem22().sort(data, lambda x: x['title']), [
            {'id': 2, 'title': 'A', 'rate': 9},
            {'id': 3, 'title': 'B', 'rate': 3},
            {'id': 1, 'title': 'C', 'rate': 8},
            {'id': 7, 'title': 'D', 'rate': 4},
            {'id': 9, 'title': 'E', 'rate': 5},
            {'id': 8, 'title': 'F', 'rate': 6},
            {'id': 6, 'title': 'G', 'rate': 7},
            {'id': 5, 'title': 'H', 'rate': 1},
            {'id': 4, 'title': 'I', 'rate': 2},
            {'id': 10, 'title': 'J', 'rate': 10}
        ])
        self.assertEqual(Problem22().sort(data, lambda x: x['rate']), [
            {'id': 5, 'title': 'H', 'rate': 1},
            {'id': 4, 'title': 'I', 'rate': 2},
            {'id': 3, 'title': 'B', 'rate': 3},
            {'id': 7, 'title': 'D', 'rate': 4},
            {'id': 9, 'title': 'E', 'rate': 5},
            {'id': 8, 'title': 'F', 'rate': 6},
            {'id': 6, 'title': 'G', 'rate': 7},
            {'id': 1, 'title': 'C', 'rate': 8},
            {'id': 2, 'title': 'A', 'rate': 9},
            {'id': 10, 'title': 'J', 'rate': 10}
        ])
        self.assertEqual(Problem22().sort(data, lambda x: x['rate'], True), [
            {'id': 10, 'title': 'J', 'rate': 10},
            {'id': 2, 'title': 'A', 'rate': 9},
            {'id': 1, 'title': 'C', 'rate': 8},
            {'id': 6, 'title': 'G', 'rate': 7},
            {'id': 8, 'title': 'F', 'rate': 6},
            {'id': 9, 'title': 'E', 'rate': 5},
            {'id': 7, 'title': 'D', 'rate': 4},
            {'id': 3, 'title': 'B', 'rate': 3},
            {'id': 4, 'title': 'I', 'rate': 2},
            {'id': 5, 'title': 'H', 'rate': 1}
        ])


if __name__ == "__main__":
    unittest.main()
