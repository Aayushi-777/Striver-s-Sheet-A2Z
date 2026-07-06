class Solution:
    def gcd(self, a, b):
        if b==0:
            return a
        else:
            return self.gcd(b, a%b)
if __name__=="__main__":
    sol=Solution()
    a=12
    b=16
    gcd=sol.gcd(a, b)
    print(f"GCD of {a} and {b} is: {gcd}")