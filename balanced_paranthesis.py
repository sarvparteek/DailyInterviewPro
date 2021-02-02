'''
Author: Sarv Parteek Singh (sarvparteek@gmail.com)
Source: https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
Date: Jan 31, 2021
Brief: Checks whether a given expression is balanced in paranthesis
'''

from collections import deque

def is_balanced(expr):
    # Use deque instead of list because (quoting from documentation):
    # "Deques support thread - safe, memory efficient appends and pops from either side of the deque with approximately
    # the same O(1) performance in either direction. \
    # Though list objects support similar operations, they are optimized for fast fixed - length operations and incur
    # O(n) memory movement costs for pop(0) and insert(0, v) operations which change both the size and position of the
    # underlying data representation."
    stack = deque()

    for char in expr:
        if char in ["(", "[", "{"]:
            stack.append(char)
        else:
            if not len(stack) or not matches(stack.pop(), char):
                return False
    return True


def matches(char1, char2):
    if (char1 == '(' and char2 == ")" ) or (char1 == '[' and char2 == ']') or (char1 == '{' and char2 == '}'):
        return True
    else:
        return False


if __name__ == "__main__":
    expr = "{{()}[]}"
    print("For ", expr, " balancing is ", is_balanced(expr))

    expr = "{{]}"
    print("For ", expr, " balancing is ", is_balanced(expr))

    expr = "()]"
    print("For ", expr, " balancing is ", is_balanced(expr))