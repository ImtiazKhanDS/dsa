# @leet imports start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
from typing import *
# @leet imports end

# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root:Optional[TreeNode]):
            if not root:
                return float("inf")
            if not root.left and not root.right:
                return 1

            left = dfs(root.left)
            right = dfs(root.right)
            return 1 + min(left, right)
        ans = dfs(root)
        if ans == float("inf"):
            return 0
        return ans        
# @leet end
