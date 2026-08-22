from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups=defaultdict(list)


        for i in strs:
            key="".join(sorted(i))
            groups[key].append(i)

        return list(groups.values())
