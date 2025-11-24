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
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(root, max_value):
            nonlocal count
            if not root:
                return
            if root.val>=max_value:
                count+=1
            new_max_value = max(max_value, root.val)
            dfs(root.left, new_max_value)
            dfs(root.right, new_max_value)
        dfs(root, root.val)
        return count
        
# @leet end
