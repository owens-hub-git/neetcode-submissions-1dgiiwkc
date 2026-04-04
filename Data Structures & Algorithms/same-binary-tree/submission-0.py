# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []

        def dfs(root, res):
            if not root:
                return
            
            res.append(root.val)

            if root.left and not root.right:
                res.append(-1)

            dfs(root.left, res)
            dfs(root.right, res)

        dfs(p, res1)
        dfs(q, res2)
        print(res1, res2)
        if res1 == res2:
            return True
        return False