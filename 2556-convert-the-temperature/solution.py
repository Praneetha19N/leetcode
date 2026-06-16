class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        p=[]
        a=celsius+273.15
        b=celsius*1.80+32.00
        p.append(a)
        p.append(b)
        return p
        
