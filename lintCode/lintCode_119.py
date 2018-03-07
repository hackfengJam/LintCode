#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = "2018/3/6 下午2:21"


class Solution(object):
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """

    def minDistance(self, word1, word2):
        # write your code here
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        len1 = len(word1)
        len2 = len(word2)
        res = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        for i in range(1, len1 + 1):
            res[i][0] = i
        for i in range(1, len2 + 1):
            res[0][i] = i
        for i in range(1, len1 + 1):
            c1 = word1[i - 1]
            for j in range(1, len2 + 1):
                c2 = word2[j - 1]
                if c1 == c2:
                    res[i][j] = res[i - 1][j - 1]
                else:
                    res[i][j] = min(res[i - 1][j], min(res[i][j - 1], res[i - 1][j - 1])) + 1
        return res[len1][len2]


s = Solution()
print s.minDistance("mart", "karma")
