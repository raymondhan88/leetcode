class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=0,1
        while n>0:
            n-=1
            a,b=b,a+b
        return b