class Solution:
    def findComplement(self, num: int) -> int:
        y=1
        while y<num:
            y=(y<<1)|1
        return num^y
        

        
