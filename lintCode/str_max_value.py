#!/usr/bin/env python
# coding=utf-8


class Solution:
    """
    @param: : the given string
    @return: the maximum value
    """

    def calcMaxValue(self, str):
        # write your code here
        if str == "" or len(str) == 0:
            return 0
        arr = [int(x) for x in str]
        return reduce(lambda a, b: a*b if a*b > a+b else a+b, arr)


if __name__ == '__main__':
    sol = Solution()
    res = sol.calcMaxValue('891')
    print res
