class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s=[0]*(2*n)
        for i in range(n):
            s[i]=nums[i]
            s[i+n]=nums[i]
        return s
        
        