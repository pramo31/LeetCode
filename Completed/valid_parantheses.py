from collections import deque

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = deque()

        for i in range(0, len(s)):
            elem = s[i]
            if (elem in dict.keys()):
                stack.append(elem)
            elif(elem in dict.values()):
                if (not stack):
                    return False
                else:
                    compare = stack.pop()
                    if (dict[compare] != elem):
                        return False
        if (stack):
            return False
        else:
            return True


if (__name__ == "__main__"):
    input = "()[]{}"

    obj = Solution()
    print("Is Valid Parantheses : {}".format(obj.isValid(input)))
