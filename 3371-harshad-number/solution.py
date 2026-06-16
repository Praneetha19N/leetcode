class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum=0
        s=str(x)
        for i in s:
            sum+=int(i)
        if int(x)%sum==0:
                return sum
        return -1
        
