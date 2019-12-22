from typing import List

"""
Given an array of strings, group anagrams together.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for word in strs:
            sorted_word = "".join(sorted(list(word)))
            if (sorted_word in anagram_dict.keys()):
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
        return anagram_dict.values()


if (__name__ == "__main__"):
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    obj = Solution()
    print("Grouped Anagrams : {}".format(obj.groupAnagrams(strs)))
