class Solution:
    def findMaxAverage(self, nums, k):
        l, r = min(nums), max(nums)
        s = [0 for _ in range(len(nums) + 1)]
        while r - l >= 1e-5:
            m = (l + r) / 2

            # (sum(i) - sum(j - 1)) / (i - j + 1) >= 0.5
            # (sum[i] - sum[j - 1]) - (i - j + 1) * 0.5 >= 0
            # s2[i] <- 0 + nums[0] - 0.5 + nums[1] - 0.5  + ... nums[i - 1] - m
            check = False

            # 最小前缀
            prevMin = s[0]
            for i in range(1, len(s)):
                # reduced sum array
                s[i] = s[i - 1] + nums[i - 1] - m

                # prevMin is s[j], j < i
                # s[i] - s[j - 1] >= 0 and j <= i - k + 1
                if s[i] - prevMin >= 0 and i >= k:
                    check = True
                    break

                # i - j + 1 >= k
                if i >= k:
                    prevMin = min(prevMin, s[i - k + 1])

            if check:
                # subarray average can be bigger than m
                l = m
            else:
                r = m

        # l, r converge
        return l

solver = Solution()
# k = 4, ans = 12.75
print(solver.findMaxAverage([1,12,-5,-6,50,3], 4))
