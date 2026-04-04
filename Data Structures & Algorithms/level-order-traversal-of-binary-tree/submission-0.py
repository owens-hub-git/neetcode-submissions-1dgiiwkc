# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()

        if root:
            q.append(root)
        else:
            return []
        res = []

        while len(q) > 0:
            alt_res = []
            for i in range(len(q)):
                curr = q.popleft()
                alt_res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(alt_res)
        return res
