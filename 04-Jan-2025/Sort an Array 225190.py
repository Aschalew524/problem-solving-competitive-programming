# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        heapify(nums)
        for i in range(n):
            num=heappop(nums)
            print(num)
            ans.append(num)
        return ans

        