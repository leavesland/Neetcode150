class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        lo,hi = 1, len(nums)-1
        while lo<hi:
            mid = (lo+hi)//2
            together = sum(1 for x in nums if x<=mid)
            if together  > mid:
                hi = mid
            else :
                lo=mid+1
            return lo