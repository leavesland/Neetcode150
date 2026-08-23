class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=0
            freq[i]+=1
        return sorted(freq, key=freq.get, reverse=True)[:k]
#sorted always sort the keys of freq

