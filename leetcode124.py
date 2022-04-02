# Definition for a binary tree node.
import sys
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -sys.maxsize-1

        def dfs(node):
            if node == None:
                return 0
            left, right = max(0,dfs(node.left)), max(dfs(node.right),0)
            self.res= max(self.res,node.val+left+right)
            return node.val+max(left,right)

        dfs(root)
        return self.res

