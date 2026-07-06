class Solution:
    def is_prime(self, n):
        count=0
        for i in range(1, int(n**0.5)+1):
            if n%i==0:
                count+=1
                if n//i!=i:
                    count+=1
        if count==2:
            print(f"The number {n} is a prime number.")
        else:
            print(f"The number {n} is not a prime number.")
if __name__=="__main__":
    sol=Solution()
    n=1483
    sol.is_prime(n)