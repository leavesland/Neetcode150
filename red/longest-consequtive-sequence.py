class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        answer=[]
        seen=set(nums)
        for i in seen:
            if i-1 not in seen:
                curr=i
                length=1
                while curr+1 in seen:
                    curr+=1
                    length+=1
                answer.append(length)
        return max(answer   )