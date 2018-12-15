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


if __name__ == "__main__":
    unittest.main()
