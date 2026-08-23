class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        answer=[]
        for index, i in enumerate(nums):
            diff=target-i
            if diff in seen:
                return [seen[diff],index]

            seen[i]=index