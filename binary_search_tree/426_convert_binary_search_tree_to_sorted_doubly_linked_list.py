from tree import Tree
root = Tree([4, 2, 5, 1, 3]).root

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""

class SolutionStack(object):
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        Note tht head points to smallest element, not root node of BST
        :param root:
        :return:
        """
        if not root: return
        # do in-order traversal, use a lagging variable to keep track of previous node
        head, prev, cur = None, None, root
        stack = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            if prev:
                # splice with previous node
                prev.right, cur.left = cur, prev
            else:
                head = cur

            prev = cur

            cur = cur.right

        head.left, prev.right = prev, head
        return head

class SolutionStack2(object):
    # stack solution, modified from in-order traversal
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        result, stack = [], [(root, False)]
        prev = None
        head = None
        while stack:
            cur, ready = stack.pop()
            if ready:
                if prev:
                    prev.right = cur
                    cur.left = prev
                else:
                    head = cur
                prev = cur
            else:
                if cur.right:
                    stack.append((cur.right, False))
                stack.append((cur, True))
                if cur.left:
                    stack.append((cur.left, False))
        head.left = cur
        cur.right = head
        return head

solver = SolutionStack2()
head = solver.treeToDoublyList(root)
print(head.val)

class SolutionStackRec(object):
    # recursive solution
    def treeToDoublyListRec(self, root):

        def helper(curr):
            # if no left child or right child
            head, tail = curr, curr

            # doubly link to left child
            # practice:
            # visualize how it handles
                # leaf nodes
                # immediate parent of leaf (lhead == ltail)
                # ancester with more than two level of subtrees (lhead != ltail != rhead != rtail
            if curr.left:
                lhead, ltail = helper(curr.left)
                ltail.right = curr
                curr.left = ltail
                head = lhead
            if curr.right:
                rhead, rtail = helper(curr.right)
                rhead.left = curr
                curr.right = rhead
                tail = rtail
            return head, tail

        if root:
            head, tail = helper(root)

            # make it circualar
            head.left = tail
            tail.right = head
            return head
        else:
            # corner case
            return None
