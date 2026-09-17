class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maximum = 0
        while right < len(prices):

            if  prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]

                if profit > maximum:
                    maximum = profit
            right +=1
        return maximum