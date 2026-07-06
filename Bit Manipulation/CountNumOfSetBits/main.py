class Solution:
    def count_set_bits(self, n):
        count=0
        while n:
            n &=(n-1)
            count+=1
        return count

if __name__=="__main__":
    sol=Solution()
    n=29
    ans=sol.count_set_bits(n)
    print(f"The number of set bits are: {ans}")   