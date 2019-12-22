from typing import List

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        length = len(nums)
        arithmetic_mean = int(length * (length + 1) / 2)
        for i in range(0, length):
            sum += nums[i]
        return arithmetic_mean - sum

if (__name__ == "__main__"):
    list1 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    obj = Solution()
    print("Missing Number : {}".format(obj.missingNumber(list1)))
