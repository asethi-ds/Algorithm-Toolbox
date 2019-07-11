import Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        flat = []

        def inOrder(node, ):
            if not node:
                return

            inOrder(node.left)
            flat.append(node.val)
            inOrder(node.right)

        inOrder(root)
        print(flat)

        for i in range(1, len(flat)):
            if flat[i] <= flat[i - 1]:
                return False
        return True

    # BAD! Cannot backtrack
    # def isValidBSTBacktrack(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     self.prev = None
    #
    #     def inOrder(node):
    #         if not node:
    #             return True
    #
    #         return inOrder(node.left)
    #
    #         if self.prev and node.val <= prev.val:
    #             return False
    #         self.prev = node
    #
    #         return inOrder(node.right)
    #
    #     return inOrder(root)


class Solution:
    def isValidBSTStack(self, root):
        result, stack = [], [(root, False)]
        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    if len(result) > 0 and cur.val <= result[-1]:
                        return False
                    result.append(cur.val)
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))
        return True

class Solution:
    """
    Iterative in-order traversal
    """
    def isValidBST(self, root):
        path, stack = [], []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            if path and node.val <= path[-1].val:
                return False
            path.append(node)

            node = node.right

        return True

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidBSTRec(root, lower=float('-inf'), upper=float('inf')):
            if not root:
                return True
            # valid: lower < root.val < upper
            if root.val <= lower or root.val >= upper:
                return False
            return isValidBSTRec(root.left, lower, root.val) and \
                   isValidBSTRec(root.right, root.val, upper)

        return isValidBSTRec(root)

treeVals = [2, 1, 3]
# treeVals = []
tree = Tree.Tree(treeVals)
root = tree.root

solver = Solution()
print(solver.isValidBSTStack(root))
