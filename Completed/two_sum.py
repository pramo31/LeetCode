from typing import List


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
