#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = "2018/3/5 下午2:09"


class Solution(object):
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """

    def isInterleave(self, s1, s2, s3):
        # write your code here
        if len(s3) != (len(s1) + len(s2)):
            return False
        if len(s1) == 0:
            return s3 == s2
        if len(s2) == 0:
            return s3 == s1
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in xrange(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and (s3[i - 1] == s1[i - 1])
        for i in xrange(1, len(s2) + 1):
            dp[0][i] = dp[0][i - 1] and (s3[i - 1] == s2[i - 1])
        for i in xrange(1, len(s1) + 1):
            for j in xrange(1, len(s2) + 1):
                t = i + j
                if s1[i - 1] == s3[t - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
                if s2[j - 1] == s3[t - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]
        return dp[len(s1)][len(s2)]


c = Solution()
print c.isInterleave("aabcc", "dbbca", "aadbbcbcac")
print c.isInterleave("aabcc", "dbbca", "aadbbbaccc")
