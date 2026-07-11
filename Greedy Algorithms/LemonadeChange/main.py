class Solution:
    def lemonade_change(self, bills):
        five=0
        ten=0
        for bill in bills:
            if bill==5:
                five+=1
            elif bill==10:
                if five>0:
                    five-=1
                    ten+=1
                else:
                    return False
            else:
                if five>0 and ten>0:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True

if __name__=="__main__":
    sol=Solution()
    bills=[5, 5, 5, 10, 20]
    ans=sol.lemonade_change(bills)
    print(f"Is it possible to provide change to all customers?: {ans}")