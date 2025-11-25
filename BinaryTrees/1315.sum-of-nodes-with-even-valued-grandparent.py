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
   def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, parent, gparent):
            nonlocal ans
            if not root:
                return 0
            if gparent%2==0:
                ans+=root.val
            dfs(root.left, root.val, parent)
            dfs(root.right, root.val, parent)
        dfs(root, -1, -1)
        return ans
# @leet end
