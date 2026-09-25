class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        m=nums[0]
        for i in nums:
            if abs(i)<abs(m):
                m=i
            elif abs(i)==abs(m) and i>m:
                m=i
        return m
        