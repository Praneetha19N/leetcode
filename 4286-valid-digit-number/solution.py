class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        k=list(str(n))
        f=str(x)
        if k[0]!=f and f in k:
            return True
        return False
