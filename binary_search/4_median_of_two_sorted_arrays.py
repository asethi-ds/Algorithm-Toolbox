class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) <= len(nums2):
            x, y = nums1, nums2
        else:
            x, y = nums2, nums1

        l, r = 0, len(x)

        while l <= r:
            i = (l + r) // 2
            j = (len(nums1) + len(nums2) + 1) // 2 - i

            xLeftMax = x[i - 1] if i != 0 else float("-inf")
            xRightMin = x[i] if i != len(x) else float("inf")
            yLeftMax = y[j - 1] if j != 0 else float("-inf")
            yRightMin = y[j] if j != len(y) else float("inf")

            print(i, j, xLeftMax, xRightMin, yLeftMax, yRightMin)
            if xLeftMax <= yRightMin and yLeftMax <= xRightMin:
                # partition is right, return median
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(xLeftMax, yLeftMax) + min(xRightMin, yRightMin)) / 2
                else:
                    return max(xLeftMax, yLeftMax)
            elif xLeftMax > yRightMin:
                r = i - 1
            else:  # yLeftMax > xRightMin
                l = i + 1
solver = Solution()

# ans: 13.5
x = [23,26,31,35]
y = [3,5,7,9,11,16]
print(solver.findMedianSortedArrays(x, y))

# ans: 11
x = [1,3,8,9,15]
y = [7,11,18,19,21,25]
print(solver.findMedianSortedArrays(x, y))
