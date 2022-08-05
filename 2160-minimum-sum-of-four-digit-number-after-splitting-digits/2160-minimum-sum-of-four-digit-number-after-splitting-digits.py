class Solution:
    def minimumSum(self, num: int) -> int:
        num=list(map(int,str(num)))
        num.sort()
        a=str(num[0])+str(num[2])
        b=str(num[1])+str(num[3])
        return int(a)+int(b)
      
        
        
        