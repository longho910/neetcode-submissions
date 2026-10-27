class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = defaultdict(list)

        for str in strs:
            cnt = [0] * 26
            for c in str:
                cnt[ord(c) - ord("a")] += 1
            _dict[tuple(cnt)].append(str)

        return list(_dict.values())
