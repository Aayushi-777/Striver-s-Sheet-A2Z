class Solution:
    def rotate_string(self, s, goal):
        if len(s)!=len(goal):
            return False
        doubled_s=s+s
        if goal in doubled_s:
            return True
        return False
    
if __name__=="__main__":
    sol=Solution()
    s="rotation"
    goal="tionrota"
    ans=sol.rotate_string(s, goal)
    print(f"Is goal possible after needed rotations of the string?: {ans}")