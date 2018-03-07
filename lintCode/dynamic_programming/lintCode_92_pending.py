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

    def backPack(self, m, A):
        # write your code here
        length = len(A)
        res = [[0 for _ in range(length + 1)] for _ in range(length + 1)]
        for i in range(length):
            res[0][i] = A[i]
            res[i][0] = A[i]



        for i in range(length):
            if res[i - 1] + A[i] < m:
                res[i] = res[i - 1] + A[i]
        pass
