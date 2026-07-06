class Solution:
    def stock_buy_sell(self, arr):
        min_price=float('inf')
        max_profit=0
        for price in arr:
            if price<min_price:
                min_price=price
            else:
                max_profit=max(max_profit, price-min_price)
        return max_profit
    
if __name__=="__main__":
    sol=Solution()
    arr=[7, 1, 5, 3, 6, 4] 
    max_profit=sol.stock_buy_sell(arr)
    print(f"The maximum profit is: {max_profit}")