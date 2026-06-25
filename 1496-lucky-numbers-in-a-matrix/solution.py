class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        r=[]
        for i in matrix:
            m=min(i)
            x=i.index(m)
            n= max(matrix[j][x] for j in range(len(matrix)))

            if n==m:
                r.append(m)
        return r
        
