from typing import List

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_counter = 0
        nums2_counter = 0
        nums1_count = len(nums1)
        nums2_count = len(nums2)
        final_list = []
        while (nums1_counter < nums1_count and nums2_counter < nums2_count):
            if (nums1[nums1_counter] < nums2[nums2_counter]):
                final_list.append(nums1[nums1_counter])
                nums1_counter += 1
            elif (nums1[nums1_counter] > nums2[nums2_counter]):
                final_list.append(nums2[nums2_counter])
                nums2_counter += 1
            else:
                final_list.append(nums1[nums1_counter])
                final_list.append(nums2[nums2_counter])
                nums1_counter += 1
                nums2_counter += 1
        if (nums1_counter < nums1_count):
            for i in range(nums1_counter, nums1_count):
                final_list.append(nums1[i])
        if (nums2_counter < nums2_count):
            for i in range(nums2_counter, nums2_count):
                final_list.append(nums2[i])
        length = len(final_list)
        median = length // 2
        if (length % 2 == 1):
            return final_list[median]
        else:
            return (final_list[median] + final_list[median - 1]) / 2


if (__name__ == "__main__"):
    nums1 = [1, 2, 3]
    nums2 = [2, 4]

    obj = Solution()
    print("Median : {}".format(obj.findMedianSortedArrays(nums1, nums2)))
