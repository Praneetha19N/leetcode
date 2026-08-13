class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        c=numBottles
        while numBottles>=numExchange:
            d=numBottles//numExchange
            s=numBottles%numExchange
            c+=d
            numBottles=d+s
        return c        
        
