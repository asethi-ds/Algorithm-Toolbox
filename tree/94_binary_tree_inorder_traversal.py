from tree import Tree

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        def traverse(node, l):
            if node is None:
                return
            traverse(node.left, l)
            ans.append(node.val)
            traverse(node.right, l)
        traverse(root, ans)

        return ans

    def inorderTraversalStack1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if root is None:
        #     return []
        # output = []
        # return printInorder(root, output)

        result = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()

            # do something --------
            result.append(cur.val)
            # ---------------------

            cur = cur.right
        return result

    # compare to def preorderTraversal3(self, root): in 144 Preorder Traversak
    def inorderTraversalStack2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if root is None:
        #     return []
        # output = []
        # return printInorder(root, output)

        result = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()

                # do something --------
                result.append(cur.val)
                # ---------------------

                cur = cur.right
        return result

    def inorderTraversalFlat(self, root):

        # if not root:
        #     return []
        #
        # result, stack = [], [(root, False)]
        #
        # while stack:
        #     cur, visited = stack.pop()
        #     if visited:
        #         result.append(cur.val)
        #     else:
        #         if cur.right:
        #             stack.append((cur.right, False))
        #         stack.append((cur, True))
        #         if cur.left:
        #             stack.append((cur.left, False))
        # return result

        result, stack = [], [(root, False)]

        while stack:
            cur, visited = stack.pop()
            # either check existence here, or check existence before appending left & right child
            # also, if input is null, the exception is handled gracefully
            if cur:
                if visited:
                    # do something --------
                    result.append(cur.val)
                    # ---------------------
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))
        return result

    def inorderTraversalMorris(self, root):
        """
        Edge case:
            when input is null
            when child node is null
        """
        ans = []
        curr = root
        while curr:
            # if left is null, process curr and go right
            if not curr.left:
                ans.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                # go right until right is null (no link) or is curr (link exists)
                while prev.right and prev.right != curr:
                    prev = prev.right
                if not prev.right:
                    # establish link and move left
                    prev.right = curr
                    curr = curr.left
                else:
                    # remove link and move right
                    prev.right = None
                    ans.append(curr.val)
                    curr = curr.right
        return ans


solver = Solution()

root = Tree([1, None, 2, None, None, 3]).root
ans = solver.inorderTraversalMorris(root)
print(ans)

root = Tree([4, 2, 5, 1, 3, None, 6]).root
print(solver.inorderTraversalMorris(root))

# root = Tree([1, 2, 3, 4, 5, 6]).root
# ans = solver.inorderTraversalFlat(root)
# print(ans)
