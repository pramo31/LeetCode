"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""


class Solution:
    def myAtoi(self, str: str) -> int:
        result = ""
        foundFirstNonWhitespace = False
        isPositive = True
        isValid = True
        for char in str:
            if (char == " "):
                if (foundFirstNonWhitespace):
                    break
            else:
                if (not foundFirstNonWhitespace):
                    if (char == "-" or char == "+"):
                        if (char == "-"):
                            isPositive = False
                    elif (char.isdigit()):
                        result += char
                    else:
                        isValid = False
                        break
                    foundFirstNonWhitespace = True
                else:
                    if (char.isdigit()):
                        result += char
                    else:
                        break

        if (result == "" or not isValid):
            return 0
        else:
            max = 2 ** 31 - 1
            min = -1 * 2 ** 31
            num = int(result)
            if (not isPositive):
                num = num * -1
            if (not min <= num <= max):
                if (not isPositive):
                    return min
                else:
                    return max
            else:
                return num


if (__name__ == "__main__"):
    string = "+"

    obj = Solution()
    print("Integer : {}".format(obj.myAtoi(string)))
