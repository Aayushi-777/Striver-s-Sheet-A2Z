class Solution:
    def shortest_job_first(self, jobs):
        jobs.sort()
        wait_time=0
        total_time=0
        for job in jobs:
            wait_time+=total_time
            total_time+=job
        return wait_time/(len(jobs))

if __name__=="__main__":
    sol=Solution()
    jobs=[4, 3, 7, 1, 2]
    ans=sol.shortest_job_first(jobs)
    print(f"Average waiting time is: {ans}")