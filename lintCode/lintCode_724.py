#!/usr/bin/env python
# coding=utf-8


class Solution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums
    """

    def findMin(self, nums):
        # write your code
        if nums is None or len(nums) == 0:
            return 0
        nums = sorted(nums)
        length = len(nums)
        i = 0
        res = 0
        total = 0
        while i <= length-1:
            total += nums[i]
            i += 1

"""
1 1 2 2 3 4 5
1224
135
235
1124
"""