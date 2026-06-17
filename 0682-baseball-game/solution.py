class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]
        for symbol in operations:
            if symbol=='+':
                l.append(l[-1]+l[-2])
            elif symbol=='D':
                l.append(l[-1]*2)
            elif symbol=='C':
                l.pop()
            else:
                l.append(int(symbol))
        return sum(l)
        
