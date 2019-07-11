class Solution:
    """
    input: 2, 4
          0
         /
        1
       / \
      2   3
         /
        4

    ___ root = 0
    |

    ___ root = 1
    |L

    ___ root = 2
    |LL return 2

    ___ root = 1
    |L
    l = 2

    ___ root = 3
    |LR

    ___ root = 4
    |LRL return 4

    ___ root = None
    |LRR return None

    ___ root = 3
    |LR
    l = 4
    r = None
    return 4

    ___ root = 1
    |L
    l = 2
    r = 4
    found LCA, return 1

    ___ root = 0
    |
    l = 4

    ___ root = None
    |R return None

    ___ root = 0
    |
    l = 4
    r = None
    return l = 4
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Divide and conquer.
        """
        if not root or root == p or root == q: return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # this is LCA: one node is in left, one node is in right
        if l and r: return root

        # return LCA to parent stack
        if l: return l # one node is found in left subtree
        if r: return r # one node is found in right subtree

        # none of p or q is root's children
        return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        """
        First build a map linking child to parent.
        When construct entire path from p to root.
        Traverse starting with q, end when first node is found in common.
        """
        parent = {root : None}
        queue = [root]
        while p not in parent or q not in parent:
            node = queue.pop()
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
        path = set()
        while p:
            path.add(p)
            p = parent[p]
        while q not in path:
            q = parent[q]
        return q
