from tree import Tree
root = Tree.Tree([2, 1, 3]).root

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        cur = root
        stack = []
        found = False
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            if found is True:
                return cur

            if cur == p:
                found = True

            cur = cur.right
        return None

solver = Solution()
solver.inorderSuccessor(root, root.left)
