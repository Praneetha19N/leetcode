class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l=[]
        s=Counter(arr)
        for (k,v) in s.items():
            if k==v:
                l.append(k)
        if l:
            return max(l)
        else:
            return -1


        
