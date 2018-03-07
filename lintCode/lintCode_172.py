#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = "2018/3/7 下午3:14"


class Solution(object):
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """

    def removeElement(self, A, elem):
        # write your code here
        B = []
        for i in xrange(len(A)):
            val = A[i]
            if val != elem:
                B.append(val)
        return B


s = Solution()
print s.removeElement([0, 4, 4, 0, 0, 2, 4, 4], 4)
