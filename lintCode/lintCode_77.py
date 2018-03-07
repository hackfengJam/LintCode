#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = "2018/3/6 下午2:21"


class Solution(object):
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here

        # write your code here
        if len(A) == 0:
            return len(B)
        if len(B) == 0:
            return len(A)
        len1 = len(A)
        len2 = len(B)
        res = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if A[i - 1] == B[j - 1]:
                    res[i][j] = res[i - 1][j - 1] + 1
                else:
                    res[i][j] = max(res[i][j - 1], res[i - 1][j])
        return res[len1][len2]


s = Solution()
print s.longestCommonSubsequence("mart", "karma")
