class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i=='(':
                l.append(')')
            elif i=='{':
                l.append('}')
            elif i=='[':
                l.append(']')
            elif not l or l.pop()!=i:
                return False
        return not l
            
                

        
