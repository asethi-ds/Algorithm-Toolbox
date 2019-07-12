class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sliding window, O(N) time, O(1) space
        globMax = tempMax = sum(nums[:k])
        for i in range(k, len(nums)):
            tempMax += (nums[i] - nums[i-k])
            globMax = max(tempMax, globMax)
        return globMax / k
