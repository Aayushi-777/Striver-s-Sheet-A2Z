class Solution:
    def fractional_knapsack(self, values, weights, capacity):
        items=[]
        for i in range(len(values)):
            ratio=values[i]/weights[i]
            items.append((values[i], weights[i], ratio))
        items.sort(key=lambda x:x[2], reverse=True)
        total_value=0
        for value, weight, ratio in items:
            if capacity>=weight:
                total_value+=value
                capacity-=weight
            else:
                total_value+=ratio*capacity
        return total_value

if __name__=="__main__":
    sol=Solution()
    values=[60, 100, 120]
    weights=[10, 20, 30]
    capacity=50
    ans=sol.fractional_knapsack(values, weights, capacity)
    print(f"The maximum value is: {ans:.2f}")