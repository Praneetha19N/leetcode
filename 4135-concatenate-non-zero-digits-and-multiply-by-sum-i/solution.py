class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=str(n)
        l=[x for x in s if x!="0"]
        if not l:
            return 0
        p="".join(l)
        d=sum(int(i) for i in p)
        return int(p)*d

        
