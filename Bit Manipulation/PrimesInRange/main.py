class Solution:
    def prime_in_range(self, ranges):
        max_val=max(r for _, r in ranges)
        is_prime=[True]*(max_val+1)
        is_prime[0]=is_prime[1]=False
        for i in range(2, int(max_val**0.5)+1):
            if is_prime[i]:
                for j in range(i*i, max_val+1, i):
                    is_prime[j]=False
        prefix=[0]*(max_val+1)
        for i in range(1, max_val+1):
            prefix[i]=prefix[i-1]+is_prime[i]
        return [prefix[r]-prefix[l-1] for l, r in ranges]

if __name__=="__main__":
    sol=Solution()
    ranges=[[2, 5], [4, 7]]
    print(sol.prime_in_range(ranges))