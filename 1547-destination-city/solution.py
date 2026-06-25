class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s=set()
        for i,j in paths:
            s.add(i)
        for i,j in paths:
            if j not in s:
                return j
        

        
