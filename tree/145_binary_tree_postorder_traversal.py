from tree import Tree

class Solution(object):
    # textbook solution
    """
         4
        / \
       2   3
        \
         1

    curr = 4
    not prev
    stack = [4, 2]
    prev <- 4

    curr = 2
    prev.left == curr
    stack = [4, 2, 1]
    prev <- 2

    curr = 1
    prev.right == curr
    stack = [4, 2, 1]
    prev <- 1

    curr = 1
    ans = [1]
    stack = [4, 2]
    prev <- 1

    curr = 2
    ans = [1, 2]
    stack = [4]
    prev <- 2

    curr = 4
    curr.left == prev
    stack = [4, 3]
    prev <- 4

    curr = 3
    prev.right == curr
    prev <- 3

    curr = 3
    ans = [1, 2, 3]
    stack = [4]
    prev <- 3

    curr = 4
    ans = [1, 2, 3, 4]
    stack = []
    prev <- 4
    """
    def postorderTraversal(self, root):
        ans = []
        if not root: return ans
        prev, curr = None, root
        stack = [root]

        while stack:
            curr = stack[-1] # peek
            if not prev or prev.left == curr or prev.right == curr:
                # traverse down the tree
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
            elif curr.left == prev:
                # traverse up the tree from the left
                if curr.right: stack.append(curr.right)
            else:
                # traverse up the tree from the right
                ans.append(curr.val)
                stack.pop()

            print("curr", curr.val, "stack:", [node.val for node in stack], "ans:", ans)
            prev = curr
        return ans

    # using a hash set to remember visited nodes, time O(N), memory O(N)
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        post_order = []
        stack = [root]
        visited = {root}
        while stack:
            top = stack[-1]
            no_next = True
            if top.right and top.right not in visited:
                stack.append(top.right)
                visited.add(top.right)
                no_next = False
            if top.left and top.left not in visited:
                stack.append(top.left)
                visited.add(top.left)
                no_next = False
            if no_next:
                post_order.append(top.val)
                stack.pop()

        return post_order

    # modify from pre-order traversal
    def postorderTraversalRecLogic(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = root
        stack = []
        res = []
        while stack or node:
            if node:
                stack.append(node)
                res.insert(0, node.val)
                node = node.right
            else:
                node = stack.pop().left
        return res

    # same as above, use build forward
    def postorderTraversalRecLogic2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = root
        stack = []
        res = []
        while stack or node:
            if node:
                stack.append(node)
                res.append(node.val)
                node = node.right
            else:
                node = stack.pop().left
        return res[::-1]

    # modify from pre-order traversal
    def postorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()

            # insert instead of append
            ans.insert(0, u.val)

            # add left child first
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans

    # modify from pre-order traversal. simplified using append instead of insert
    def postorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()

            ans.append(node.val)

            # add left child first
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans[::-1]

    def postorderNary(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            u = stack.pop()

            # insert instead of append
            ans.insert(0, u.val)

            # add left child first
            for child in u.children:
                stack.append(child)
        return ans

    def postorderTraversalMorris(self, root):
        ans = []
        curr = root
        while curr:
            # if right is null, process curr and go left
            if not curr.right:
                ans.append(curr.val)
                curr = curr.left
            else:
                prev = curr.right
                # go left until left is null (no link) or is curr (link exists)
                while prev.left and prev.left != curr:
                    prev = prev.left
                if not prev.left:
                    # establish link and move right
                    prev.left = curr
                    ans.append(curr.val)
                    curr = curr.right
                else:
                    # remove link and move left
                    prev.left = None
                    curr = curr.left
        return ans[::-1]

solver = Solution()

root = Tree([4, 2, 3, None, 1]).root
print(solver.postorderTraversal(root))
print(solver.postorderTraversalMorris(root))

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

root = Tree([10,5,-3,3,2,None,11,3,-2,None,1]).root
print(solver.postorderTraversal(root))