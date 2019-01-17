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


print(solution([1, 12 ,42,70,36,-4,43,15], [5,15,44,72,36,2,69,24]))
   
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


if __name__ == "__main__":
    unittest.main()
