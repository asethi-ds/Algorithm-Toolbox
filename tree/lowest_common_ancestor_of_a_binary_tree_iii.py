import copy
class Solution:
    """
    @param {TreeNode} root The root of the binary tree.
    @param {TreeNode} A and {TreeNode} B two nodes
    @return Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        aExist, bExist, lca = self.helper(root, A, B)
        if aExist and bExist:
            return lca
        else:
            return None

    def helper(self, root, A, B):
        if root is None:
            return False, False, None

        left_a, left_b, left_node = self.helper(root.left, A, B)
        right_a, right_b, right_node = self.helper(root.right, A, B)

        a = left_a or right_a or root == A # track whether A exists in tree
        b = left_b or right_b or root == B # track whether B exists in tree

        # current node is one of the targets
        if root == A or root == B:
            return a, b, root

        if left_node and right_node:
            # A, B in two subtrees, root is LCA
            return a, b, root
        if left_node:
            # LCA is in left subtree, LCA may not exist
            return a, b, left_node
        if right_node:
            # LCA is in right subtree, LCA may not exist
            return a, b, right_node

        return a, b, None
