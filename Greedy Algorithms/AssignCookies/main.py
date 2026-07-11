class Solution:
    def assign_cookies(self, student, cookies):
        student.sort()
        cookies.sort()
        stu_ind=0
        cookie_ind=0
        while stu_ind<len(student) and cookie_ind<len(cookies):
            if cookies[cookie_ind]>=student[stu_ind]:
                stu_ind+=1
            cookie_ind+=1
        return stu_ind

if __name__=="__main__":
    sol=Solution()
    student=[1, 2, 3]
    cookies=[1, 1]
    ans=sol.assign_cookies(student, cookies)
    print(f"The maximum students that are content are: {ans}")
