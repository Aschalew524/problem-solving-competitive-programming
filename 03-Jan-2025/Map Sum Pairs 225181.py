# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class MapSum:

    def __init__(self):
        self.m = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        self.m[key] = val

    def sum(self, prefix: str) -> int:
        total = 0
        for v in self.m:
            if prefix == v[:len(prefix)]:
                total += self.m[v]
        return total


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)