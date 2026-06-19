class Solution:
    def reverseWords(self, s: str) -> str:
        m=(s.strip().split())
        l=[]
        for i in m:
            n=i[::-1]
            l.append(n)
        return " ".join(l)
            
        
        
