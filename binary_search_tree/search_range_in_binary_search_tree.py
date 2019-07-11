class Solution:
    """
    Given a binary search tree and a range [k1, k2],
    return node values within a given range in ascending order.

    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        result = []
        self.helper(root, k1, k2, result)
        return result

    def helper(self, node, k1, k2, result):
        if not node:
            return None

        if node.val > k1:
            self.helper(node.left, k1, k2, result)

        if k1 <= node.val <= k2:
            result.append(node.val)

        if node.val < k2:
            self.helper(node.right, k1, k2, result)

"""
trace
        20
       /  \
      8   22
     / \
    4   12
[12,20,22] between k1=10 and k2=22

___ node = 20
|

___ node = 8
|L

___ node = 12
|LR

___ None
|LRL

___ node = 12
|LR result = [12]

___ None
|LRR

__ node = 8
|L pop

___ node = 20
| result = [12, 20]

___ node = 22
|R

___ node = None
|RL

___ node = 22
|R result = [12, 20, 22]

___ node = None
|RR

___ node = 22
|R pop

___ node = 20
|R pop
"""

# BAD SOLUTION, DON'T FOLLOW
# class Solution:
#     """
#
#     @param root: The root of the binary search tree.
#     @param k1 and k2: range k1 to k2.
#     @return: Return all keys that k1<=key<=k2 in increasing order.
#     """
#     # queue method: does not append in sorted order, need to sort before return
#     def searchRange1(self, root, k1, k2):
#         # write your code here
#         ans = []
#         if root is None:
#             return ans
#         queue = [root]
#         index = 0
#         while index < len(queue):
#             if queue[index] is not None:
#                 if queue[index].val >= k1 and queue[index].val <= k2:
#                     ans.append(queue[index].val)
#
#                 queue.append(queue[index].left)
#                 queue.append(queue[index].right)
#
#             index += 1
#         return sorted(ans)
#
#     def searchRange2(self, root, k1, k2):
#         if k1 > k2:
#             return []
#
#         # IMPORTANT: memorize -----------------------
#         def searchTarget(root, target):
#             if not root:
#                 return False
#
#             if root.val == target:
#                 return True
#             elif root.val < target:
#                 return searchTarget(root.right, target)
#             else:
#                 return searchTarget(root.left, target)
#         # --------------------------------------------
#
#         res = []
#
#         for target in range(k1, k2 + 1):
#             if searchTarget(root, target):
#                 res.append(target)
#         return res
