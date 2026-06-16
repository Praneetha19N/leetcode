class Solution:
    def clearDigits(self, s: str) -> str:
        p=[]
        for i in s:
            if i.isdigit():
                p.pop()
            else:
                p.append(i)
        return "".join(p)
        
