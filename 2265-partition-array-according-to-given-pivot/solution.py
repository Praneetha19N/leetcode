class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left=[]
        right=[]
        p=[]
        for i in nums:
            if i<pivot:
                left.append(i)
            elif i==pivot:
                p.append(i)
            else:
                right.append(i)
        return left+p+right
        
