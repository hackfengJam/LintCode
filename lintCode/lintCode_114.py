#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = "2018/3/7 下午4:23"


class Solution(object):
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # write your code here

        # 7043 ms
        # matrix = [[1 if j == 0 or i == 0 else 0 for i in range(n)] for j in range(m)]

        # 5043 ms
        # matrix = [[0 for _ in range(n)] for _ in range(m)]
        # for i in range(n):
        #     matrix[0][i] = 1
        # for i in range(m):
        #     matrix[i][0] = 1

        # 4948 ms
        matrix = []
        line = []
        for j in range(n):
            line.append(1)
        matrix.append(line)
        for i in range(1, m):
            line = [1]
            for j in range(1, n):
                line.append(0)
            matrix.append(line)

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

        return matrix[m - 1][n - 1]


s = Solution()
print s.uniquePaths(3, 3)
print s.uniquePaths(4, 5)
