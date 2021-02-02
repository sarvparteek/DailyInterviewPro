# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

__author__ = 'sarvps'

'''
Author: Sarv Parteek Singh (sarvparteek@gmail.com)
https://towardsdatascience.com/10-algorithms-to-solve-before-your-python-coding-interview-feb74fb9bc27
Date: Jan 31, 2021
Brief: Reverses digits of an input integer '''

class ReverseIntegers:

    def __init__(self, num):
        self.num = 0
        self.reversed_int = 0
        self.reversed_str = 0
        self.updateNum(num) # All attributes will be updated here

    def updateNum(self, num):
        self.num = num
        self.reverseInt()
        self.reverseStr()

    def reverseInt(self):
        """Reverses an integer without using conversion to string """
        digits = []
        num = self.num
        if num >= 0:
            sign = 1
        else:
            sign = -1

        while (num > 0):
            digits.append(num % 10)
            num = int(num/10)

        reversed = 0
        l = len(digits)
        for i in range(l):
            reversed += digits[i] * (10 ** (l-1-i))

        reversed *= sign
        self.reversed_int = reversed

    def reverseStr(self):
        """Reverses an integer using conversion to string"""
        string = str(self.num)
        if string[0] == '-':
            sign = -1
            del string[0]
        else:
            sign = 1

        reversed_str = string[::-1]
        self.reversed_str = sign * int(reversed_str)

if __name__ == "__main__":
    num = 234053
    r = ReverseIntegers(num)
    print("Reversing ", num, " gives", r.reversed_int, ",", r.reversed_str )

    num = 3082300
    r.updateNum(num)
    print("Reversing ", num, " gives", r.reversed_int, ",", r.reversed_str )