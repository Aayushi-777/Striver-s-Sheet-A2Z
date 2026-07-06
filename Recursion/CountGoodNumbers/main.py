class Solution:
    def count_good_numbers(self, index, n):
        MOD=10**9+7
        if index==n:
            return 1
        result=0
        if index%2==0:
            even_digits=[0, 2, 4, 6, 8]
            for digit in even_digits:
                result=(result+self.count_good_numbers(index+1, n))% MOD
        else:
            prime_digits=[2, 3, 5, 7]
            for digit in prime_digits:
                result=(result+self.count_good_numbers(index+1, n))% MOD
        return result

if __name__=="__main__":
    sol=Solution()
    n=1
    index=0
    print(sol.count_good_numbers(index, n))