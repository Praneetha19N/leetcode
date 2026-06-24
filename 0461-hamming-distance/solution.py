class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count=0
        num=x^y
        while num:
            count+=num&1
            num>>=1
        return count
        
