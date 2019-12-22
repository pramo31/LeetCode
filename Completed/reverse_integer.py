from collections import deque

"""
Given a 32-bit signed integer, reverse digits of an integer.
"""


class Solution:
    def reverse(self, x: int) -> int:
        '''
        max = 2 ** 31 - 1
        min = -1 * 2 ** 31
        if (not min < x < max):
            return 0
        isNegative = False
        if (x < 0):
            isNegative = True
            x = x * -1
        str_x = str(x)[::-1]
        num = int(str_x)
        num = num * -1 if isNegative else num
        return 0 if not min < num < max else num
        '''

        isNegative = False
        if (x < 0):
            isNegative = True
            x = x * -1

        lst = deque()
        while (x != 0):
            lst.append(x % 10)
            x = x // 10

        length = len(lst)
        num = 0
        for i in range(0, length):
            num += lst.pop() * 10 ** i

        max = 2 ** 31 - 1
        min = -1 * 2 ** 31

        if (isNegative):
            num = num * -1
        else:
            num = num

        if (not min <= num <= max):
            return 0
        else:
            return num


if (__name__ == "__main__"):
    num = 1534236469

    obj = Solution()
    print(obj.reverse(num))
