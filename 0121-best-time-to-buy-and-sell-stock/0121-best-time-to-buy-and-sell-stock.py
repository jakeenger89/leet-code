class Solution(object):
    def maxProfit(self, prices):
        maxprofit = 0
        lowprice = float('inf')
        
        for stock in prices:
            if stock< lowprice:
                lowprice = stock
            else:
                maxprofit = max(maxprofit, stock - lowprice)
        return maxprofit