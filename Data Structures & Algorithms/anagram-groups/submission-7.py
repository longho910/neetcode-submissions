class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for word in strs:
            count = {}
            for char in word:
                count[char] = 1 + count.get(char, 0)
            res[tuple(sorted(count.items()))].append(word)

        return list(res.values())