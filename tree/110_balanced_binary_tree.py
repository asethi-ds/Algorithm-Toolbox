from tree import Tree
treeVals = [3, 9, 20, None, None, 15, 7]
tree = Tree(treeVals)
root = tree.root

class Solution():
    # use a global variable to track if any subtree is unbalanced
    ans = True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node):
            if node is None:
                return 0

            l_depth = helper(node.left)
            r_depth = helper(node.right)

            if abs(l_depth - r_depth) > 1:
                self.ans = False

            return max(l_depth, r_depth) + 1

        helper(root)
        return self.ans

# without using class property: return tuple instead
class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(node):
            if not node:
                return 0, True

            leftDepth, leftBalanced = helper(node.left)
            rightDepth, rightBalanced = helper(node.right)
            depth = max(leftDepth, rightDepth) + 1

            if abs(leftDepth - rightDepth) > 1:
                return depth, False

            return depth, leftBalanced and rightBalanced
        return helper(root)[1]

solver = Solution()
print(solver.isBalanced(root))
