class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l=[]
        for i in accounts:
            s=sum(i)
            l.append(s)
        return max(l)
        
