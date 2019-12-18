from builtins import str

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return 0

if (__name__ == "__main__"):
    str = "abcabcbb"

    obj = Solution(str)
    print(obj.lengthOfLongestSubstring(str))

# any two letters consecutively breaks
# set of letters(one or more) consecutively breaks
