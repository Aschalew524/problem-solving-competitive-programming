# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = defaultdict(int)
        pairs = 0

        for num in arr:
            rem = (num % k + k) % k
            complement = (k - rem) % k

            if cnt[complement]:
                cnt[complement] -= 1
                pairs += 1
            else:
                cnt[rem] += 1
        
        return pairs == len(arr) // 2