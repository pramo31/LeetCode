"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D",
                900: "CM", 1000: "M"}
        num_list = dict.keys()
        num_list = sorted(num_list)
        roman = ""
        index = len(num_list) - 1
        while (num > 0):
            found = False
            while (not found):
                if (num_list[index] <= num):
                    found = True
                else:
                    index -= 1
            roman += dict[num_list[index]]
            num -= num_list[index]
        return roman


if (__name__ == "__main__"):
    integer = 1994
    # MCMXCIV
    obj = Solution()
    print("Integer {} converted to roman : {}".format(integer, obj.intToRoman(integer)))
