class Solution:
    def XOR_till_N(self, n):
        if n % 4==1:
            return 1
        if n % 4==2:
            return n+1
        if n % 4==3:
            return 0
        return n
    def XOR_in_range(self, l, r):
        return self.XOR_till_N(l-1) ^ self.XOR_till_N(r)
    
if __name__=="__main__":
    sol=Solution()
    l=3
    r=5
    ans=sol.XOR_in_range(l, r)
    print(f"The XOR in between of range {l} and {r} is: {ans}")