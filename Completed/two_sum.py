from typing import List

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDict = {}
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if (difference in sumDict):
                return [sumDict[difference], i]
            else:
                sumDict[nums[i]] = i


if (__name__ == "__main__"):
    list = [2, 7, 11, 15]
    target = 9

    obj = Solution()
    print(obj.twoSum(list, target))
