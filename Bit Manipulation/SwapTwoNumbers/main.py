class Solution:
    def swap_numbers(self, a, b):
        a=a ^ b
        b= a ^ b
        a= a ^ b
        return a, b

if __name__=="__main__":
    sol=Solution()
    a, b=5, 10
    print(f"Before swapping: a={a}, b={b}")
    a, b=sol.swap_numbers(a, b)
    print(f"After swapping: a={a}, b={b}")