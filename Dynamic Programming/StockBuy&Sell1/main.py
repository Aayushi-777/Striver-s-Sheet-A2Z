class Solution:
    def stock_buy_sell(self, prices):
        max_profit=0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit=prices[j]-prices[i]
                max_profit=max(max_profit, profit)
        return max_profit
if __name__=="__main__":
    sol=Solution()
    prices=[7, 1, 5, 3, 6, 4]
    max_profit=sol.stock_buy_sell(prices)
    print(max_profit)
