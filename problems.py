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




class Test(unittest.TestCase):

    def test_problem_a(self):
        for item in [('abcd'), ('s4fad'), ('')]:
            self.assertFalse(Problem1().has_duplicates1(item))

        for item in [('abacd'), ('s4f4ad'), ('dffgr')]:
            self.assertTrue(Problem1().has_duplicates1(item))

        for item in [('abcd'), ('s4fad'), ('')]:
            self.assertFalse(Problem1().has_duplicates2(item))

        for item in [('abacd'), ('s4f4ad'), ('dffgr')]:
            self.assertTrue(Problem1().has_duplicates2(item))

if __name__ == "__main__":
    unittest.main()
