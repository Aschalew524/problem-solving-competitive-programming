# Problem: Array Partition I
(Easy) - https://leetcode.com/problems/array-partition-i/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        l=[]
        m=0
        for i in nums:
            if len(l)==0:
                l.append(i)
            elif len(l)==1:
                l.append(i)
                m=m+min(l)
            elif len(l)==2:
                l.clear()
                l.append(i)
        return m


        