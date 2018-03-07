#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = "2018/3/5 上午11:42"


class Solution(object):
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, nums, target):
        # write your code here
        i = 0
        length = len(nums)
        for val in nums:
            j = self.fun(target - val, nums, i + 1, length - 1)
            if j is not None:
                return i + 1, j + 1
            i += 1

    def fun(self, val, nums, l, h):
        # mid = (h - l) / 2 + l
        while l < h:
            mid = (h + l) / 2
            k = nums[mid]
            if val == k:
                return mid
            elif val < k:
                # return self.fun(k, nums, mid + 1, h)
                h = mid
            else:
                l = mid + 1
                # return self.fun(k, nums, l, mid)
        if l == h:
            if val == nums[l]:
                return l
            else:
                return None


s = Solution()
print s.twoSum([2, 7, 11, 15], 9)
print s.twoSum([2, 3], 5)
