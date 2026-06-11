class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count=0
        s=set()
        for i in nums:
            if i in s:
                count+=1
            else:
                s.add(i)
        if count>=1:
            return True
        else:
            return False

        
