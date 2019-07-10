import Tree
treeVals = [1, 2, 5, 3, 4, None, 6]
# treeVals = []
tree = Tree.Tree(treeVals)
root = tree.root

#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6

# ouput:
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

class Solution(object):
    def flatten(self, root: TreeNode) -> None:
        """
        Stack solution
        node    stack       connect right
        1       5, 2        1 -> 2
        2       5, 4, 3     2 -> 3
        3       5, 4        3 -> 4
        4       5           4 -> 5
        5       6           5 -> 6
        6       break
        """
        if not root: return

        # warning: if root is None,
        # [None] will trigger while loop
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)

            node.left = None
            node.right = stack[-1] if stack else None
            # <- breakpoint
            
class Solution2(object):
    """
        1
       / \
      2   5
     / \   \
    3   4   6
    self.r_child = None
    ___
        1
       / \
      2   5
     / \   \
    3   4   6
    self.r_child = 6
    ___
        1
       / \
      2   5
     / \   \
    3   4   6
    self.r_child = 5
    ___
        1
       / \
      2   5
     / \   \
    3   4   6
         \
          5
           \
            6
    self.r_child = 4
    ___
        1
       / \
      2   5
     / \   \
    3   4   6
     \   \
      4   5
       \   \
        5   6
         \
          6
    self.r_child = 3

    ___
        1
       / \
      2   5
     / \   \
    X   3   6
         \
          4
           \
            5
             \
              6
    self.r_child = 2
    ___
        1
       / \
      X   2
           \   
            3   
             \
              4
               \
                5
                 \
                  6
    self.r_child = 1

    """
    r_child = None
    def flatten(self, root):
        """
        Post-order
        """
        if root is None: return

        # post-order traversal
        self.flatten(root.right)
        self.flatten(root.left)

        # all left children must be None, right child is set to the flattened subtree
        # which grows overtime
        root.left = None
        root.right = self.r_child
        self.r_child = root

        # <- breakpoint


class Solution3(object):
    """
    |
    root = 1
        1
       / \
      2   5
     / \   \
    3   4   6
    self.last = 1
    right = 5
             \
              6
    ___
    |L
    root = 2
        1
       / \
      X   2
         / \
        3   4
    self.last = 2
    right = 4

    ___
    |LL
    root = 3
        1
       / \
      X   2
         / \
        X   3
    self.last = 3
    right = None

    ___
    |LLL base case

    ___
    |LLR base case

    ___
    |LL pop

    ___
    |LR
    root = 4
        1
       / \
      X   2
         / \
        X   3
           / \
          X   4
    self.last = 4
    right = None

    ___
    |LRL base case

    ___
    |LRR base case

    ___
    |LR pop

    ___
    |L pop


    ___
    |R
    root = 5
            \
             6
        1
       / \
      X   2
         / \
        X   3
           / \
          X   4
             / \
            X   5
    right = 6

    ___
    |RL base case

    ___
    |RR
    root = 6
        1
       / \
      X   2
         / \
        X   3
           / \
          X   4
             / \
            X   5
               / \
              X   6
    right = None

    ___
    |RRL base case

    ___
    |RRR base case

    ___
    |RR return

    ___
    |R return

    ___
    | return

    """
    last = None
    def flatten(self, root: TreeNode) -> None:
        """
        Pre-order
        """
        if not root: return

        if self.last:
            self.last.left = None
            self.last.right = root

        self.last = root
        # need to setup a pointer to right child
        # which is overwritten during recursion
        right = root.right
        # <- breakpoint
        self.flatten(root.left)
        self.flatten(right)

solver = Solution()
solver.flatten(root)
