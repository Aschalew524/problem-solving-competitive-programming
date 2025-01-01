# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        if len(nums1) < len(nums2):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp
        if len(nums1) % 2 != 0 and len(nums2) % 2 != 0:
            index = 0
            while index < len(nums2):
                res = nums1[index]^nums2[index]^res
                index += 1
            while index < len(nums1):
                res = nums1[index]^res
                index+=1
        elif len(nums1) % 2 != 0:
            for num in nums2:
                res = res^num
        elif len(nums2) % 2 != 0:
            for num in nums1:
                res = res^num
        return res