class Solution:
    def count_bits(self, start, goal):
        bits=start^goal
        count=0
        while bits:
            bits &= (bits-1)
            count+=1
        return count

if __name__=="__main__":
    sol=Solution()
    start=3
    goal=4
    ans=sol.count_bits(start, goal)
    print(f"The number of bits to be flipped in start to reach the goal is: {ans}")
