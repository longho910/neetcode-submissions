class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        counts = Counter(tasks)
        f = max(counts.values())                          # bottleneck frequency
        m = sum(1 for c in counts.values() if c == f)     # how many tie for max
        return max((f - 1) * (n + 1) + m, len(tasks))