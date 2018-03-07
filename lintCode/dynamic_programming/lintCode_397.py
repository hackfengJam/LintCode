#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = "2018/3/7 下午5:13"


class Solution(object):
    """
    @param A: An array of Integer
    @return: an integer
    """

    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        length = len(A)
        if length == 1:
            return 1
        res = [1 for _ in range(length)]
        _max = 0
        for i in range(1, length):
            if A[i] > A[i - 1]:
                res[i] = res[i - 1] + 1
                if res[i] > _max:
                    _max = res[i]
        res = [1 for _ in range(length)]
        for i in range(2, length + 1):
            if A[length - i] > A[length - i + 1]:
                res[length - i] = res[length - i + 1] + 1
                if res[length - i] > _max:
                    _max = res[length - i]
        return _max


s = Solution()
print s.longestIncreasingContinuousSubsequence([5, 4, 2, 1, 3])
print s.longestIncreasingContinuousSubsequence([5, 1, 2, 3, 4])
