class Solution:
    def isPalindrome(self, x: int) -> bool:
       r=str(x)
       a=r[::-1]
       return r==a
            
