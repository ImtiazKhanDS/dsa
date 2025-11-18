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
    def isMirrorImage(self,r1:TreeNode, r2:TreeNode):
        if not r1 and not r2:
            return True
        elif not r1 or not r2:
            return False
        return r1.val==r2.val and self.isMirrorImage(r1.left, r2.right) and self.isMirrorImage(r1.right, r2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirrorImage(root.left, root.right)

        
# @leet end
