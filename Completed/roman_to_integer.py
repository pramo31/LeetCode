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
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        subt_dict = {
            "I": ["V", "X"],
            "X": ["L", "C"],
            "C": ["D", "M"]
        }

        '''
        # Using While loop
        counter = 0
        while (counter < len(s)):
            char = s[counter]
            if (char in subt_dict.keys()):
                if (counter <= (len(s) - 2)):
                    next_char = s[counter + 1]
                    if (next_char in subt_dict[char]):
                        integer -= dict[char]
                        integer += dict[next_char]
                        counter += 1
                    else:
                        integer += dict[char]
                else:
                    integer += dict[char]
            else:
                integer += dict[char]
            counter += 1
        return integer
        '''

        for i in range(0, len(s)):
            char = s[i]
            if (char in subt_dict.keys()):
                if (i <= (len(s) - 2)):
                    next_char = s[i + 1]
                    if (next_char in subt_dict[char]):
                        integer -= dict[char]
                    else:
                        integer += dict[char]
                else:
                    integer += dict[char]
            else:
                integer += dict[char]
        return integer


if (__name__ == "__main__"):
    roman = "MCMXCIV"

    obj = Solution()
    print("Roman {} converted to integer : {}".format(roman, obj.romanToInt(roman)))
