class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        allowed_set=set(allowed)
        for i in words:
            consistent=True
            for j in i:
                if j not in allowed_set:
                    consistent=False
                    break
            if consistent:
                count+=1
        return count
