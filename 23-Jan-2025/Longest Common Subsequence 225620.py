# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def solve(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + solve(i + 1, j + 1)
            else:
                memo[(i, j)] = max(solve(i + 1, j), solve(i, j + 1))
            return memo[(i, j)]

        return solve(0, 0)