class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def traverse(node):
            if not node:
                return [0, 0]

            inc = 1
            dec = 1
            if node.left:
                l_inc, l_dec = traverse(node.left)
                if node.val == node.left.val + 1:
                    dec = l_dec + 1
                elif node.val == node.left.val - 1:
                    inc = l_inc + 1

            if node.right:
                r_inc, r_dec = traverse(node.right)
                if node.val == node.right.val + 1:
                    dec = max(dec, r_dec + 1)
                elif node.val == node.right.val - 1:
                    inc = max(inc, r_inc + 1)

            # do not double count curret node
            # note that if no condition is met, streak is 1
            self.ans = max(self.ans, dec + inc - 1)
            return inc, dec
        traverse(root)
        return self.ans

from tree import Tree

 #     3
 #    / \
 #   2   4
 #  / \   \
 # 3   1   5
 #     \    \
 #      4    6
treeVals = [3, 2, 4, 3, 1, None, 5, None, None, None, 4, None, None, None, 6]
# treeVals = []
tree = Tree.Tree(treeVals)
root = tree.root

solver = Solution()
print(solver.longestConsecutive(root))
