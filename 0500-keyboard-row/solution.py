class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1=set("qwertyuiop")
        r2=set("asdfghjkl")
        r3=set("zxcvbnm")
        r=[]
        for i in words:
            if set(i.lower()) <= r1:
                r.append(i)
            elif set(i.lower()) <=r2:
                r.append(i)
            elif set(i.lower()) <= r3:
                r.append(i)
        return r

        
