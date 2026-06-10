def buySellStocks(price):
    buy=price[0]
    maxProfit = 0
    for i in range(len(price)):
        # if price[i] < buy :
        #     buy = price[i]
        # else:
        buy = min(buy,price[i])
        maxProfit = max(maxProfit,price[i]-buy)
    return maxProfit

price = [7,1,5,3,6,4,12]
print(buySellStocks(price))

# tc= o(n)
# sc = o(1)