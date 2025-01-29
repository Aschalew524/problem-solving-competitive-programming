# Problem: Minimum Size Subarray in Infinite Array - https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:

  
        rows = target//sum(nums)
        total = rows * sum(nums)
        right, minLen = 0, float('inf')

        for idxL, left in enumerate(nums):
            while total < target:
                total += nums[right]
                if right == len(nums) -1:
                    right = 0
                    rows+=1
                else: right += 1
            if total == target:
                minLen = min(minLen, (rows * len(nums)) + right -idxL)
            total -= left
        return minLen if minLen != float('inf') else -1          