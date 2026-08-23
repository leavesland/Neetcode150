from collections import defaultdict
#if I access a key that doesn't exist yet, automatically create an empty list for it.
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups=defaultdict(list)


        for i in strs:
            key="".join(sorted(i))
            groups[key].append(i)

        return list(groups.values())
