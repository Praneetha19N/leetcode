class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l=[]
        i=1
        for j in range(n):
            if i%3==0 and i%5==0:
                l.append('FizzBuzz')
            elif i%5==0:
                l.append('Buzz')
            elif i%3==0:
                l.append('Fizz')
            else:
                l.append(str(i))
            i+=1
        return l

        
