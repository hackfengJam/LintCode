#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = "2018/3/7 下午3:26"

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution(object):
    """
    @param: root: The root of binary tree.
    @return: An integer
    """

    def maxPathSum(self, root):
        # write your code here
        self.i_max = 0
        self.fun(root)
        return self.i_max

    def fun(self, root):
        if root is None:
            return 0
        left = self.fun(root.left)
        right = self.fun(root.right)

        current_sum = max(root.val, root.val + left, root.val + right)

        current_max = max(current_sum, root.val + left + right)
        if self.i_max == 0 and current_max < 0:
            self.i_max = current_max
        else:
            self.i_max = max(self.i_max, current_max)

        return current_sum
