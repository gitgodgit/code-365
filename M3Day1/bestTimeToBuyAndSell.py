def maxProfit(prices: List[int]) -> int:
    maximum = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[j] - prices[i] > maximum:
                maximum = prices[j] - prices[i]

    return  maximum

def maxProfit(prices):
    maximum = 0
    min_price = prices[0]

    #linear time approach
    for price in prices:
        min_price = min(price, min_price)
        maximum = (maximum, price - min_price)
        
    return maximum