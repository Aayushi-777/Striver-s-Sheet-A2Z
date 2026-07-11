class Solution:
    def max_meetings(self, start, end):
        meetings=[(end[i], start[i], i+1) for i in range(len(start))]
        meetings.sort()
        last_end=-1
        result=[]
        for e, s, idx in meetings:
            if s>last_end:
                result.append(idx)
                last_end=e
        return result

if __name__=="__main__":
    sol=Solution()
    start=[1, 3, 0, 5, 8, 5]
    end=[2, 4, 6, 7, 9, 9]
    ans=sol.max_meetings(start, end)
    print(f"The meetings that can be conducted are:", *ans)
