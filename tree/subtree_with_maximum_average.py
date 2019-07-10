class Solution: # accepted
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree
    def findSubtree2(self, root):
        self.avg = -2 ** 30
        self.node = root
        def traverse(root):
            # write your code here
            if not root:
                return 0, 0

            # Leaf node is handled implicitly.
            # if not root.left and not root.right:
            #     return root.val, 1

            l_sum, l_size = traverse(root.left)
            r_sum, r_size = traverse(root.right)
            cur_sum = l_sum + r_sum + root.val
            cur_size = l_size + r_size + 1

            avg = cur_sum / cur_size
            if avg > self.avg:
                # update benchmark
                self.avg = avg
                self.node = root
            return cur_sum, cur_size

        traverse(root)
        return self.node

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree
    average, node = None, None

    def findSubtree2(self, root):
        # Write your code here
        self.helper(root)
        return self.node

    def helper(self, root):
        if root is None:
            return 0, 0

        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)

        sum, size = left_sum + right_sum + root.val, \
                    left_size + right_size + 1

        # a different way of handling initial average value
        if self.node is None or sum * 1.0 / size > self.average:
            self.node = root
            self.average = sum * 1.0 / size

        return sum, size
