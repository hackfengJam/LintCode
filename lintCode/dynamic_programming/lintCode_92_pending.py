#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = "2018/3/7 下午5:56"


class Solution(object):
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack_1(self, m, A):
        """
        Memory Limit Exceeded
        总耗时: 3368 ms
        80 % 数据通过测试.
        """
        # write your code here
        length = len(A)
        res = [[0 for _ in range(m + 1)] for _ in range(length)]
        # for i in range(length + 1):
        #     res[i][0] = 0
        for j in range(1, m + 1):
            if A[0] <= j:
                res[0][j] = A[0]
            else:
                res[0][j] = 0
            for i in range(1, length):
                if A[i] > j:
                    res[i][j] = res[i - 1][j]
                else:
                    res[i][j] = max(res[i - 1][j - A[i]] + A[i], res[i - 1][j])
        return res[length - 1][m]

    def backPack(self, m, A):
        """
        Time Limit Exceeded
        总耗时: 5571 ms
        80% 数据通过测试.
        """
        # write your code here
        length = len(A)
        res = [0 for _ in range(m + 1)]
        for j in range(1, m + 1):
            if A[0] <= j:
                res[j] = A[0]
            else:
                res[j] = 0
        for i in range(1, length):
            # for j in range(1, m + 1):
            #     if A[i] <= m - j + 1:
            #         res[m - j + 1] = max(res[m + 1 - j - A[i]] + A[i], res[m + 1 - j])
            for j in range(m, 0, -1):
                if A[i] <= j:
                    res[j] = max(res[j - A[i]] + A[i], res[j])
        return res[m]


s = Solution()
print s.backPack(11, [2, 3, 5, 7])
