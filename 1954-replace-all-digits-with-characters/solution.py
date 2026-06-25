class Solution:
    def replaceDigits(self, s: str) -> str:
        s=list(s)
        for i in range(len(s)):
            if i%2==1:
                x=ord(s[i-1])
                s[i]=chr(x+int(s[i]))
        return "".join(s)


