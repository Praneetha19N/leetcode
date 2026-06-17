class Solution:
    def removeDuplicates(self, s: str) -> str:
        s1=[]
        for i in s:
            if s1 and s1[-1]==i:
                s1.pop()
            else:
                s1.append(i)

        return''.join(s1)
        
