# The cost of stock on each day is given in an array A[] of size N. 
# Find all the days on which you buy and sell the stock so that in 
# between those days your profit is maximum.
a1 = [100,180,260,310,40,535,695]
# Output:
# (0 3) (4 6)
a2 = [4,2,2,2,4]
# Output:
# (3 4)
a3=[1]

a4= [11, 42, 49, 96, 23, 20, 49, 26, 26, 18, 73, 2, 53, 59, 34, 99, 25, 2]
# output = 1

def stock_buy_sell(a):
    buy_price = 0
    buy_day = 0
    sell_price = 0
    sell_day = 0
    result = []
    for i in range(len(a)):
        print("buy", buy_price)
        print("sell:", sell_price)
        if buy_price == 0:
            buy_price = a[i]
            buy_day = i
            continue
                
        if a[i] > buy_price and a[i] > sell_price:
            sell_price = a[i]
            sell_day = i

        if a[i] <= buy_price:
           if sell_price == 0:
                buy_price = a[i]
                buy_day = i
            
            
        if a[i] < sell_price or i ==len(a)-1:
            # if sell != 0:
            if sell_price !=0 and buy_price != 0:
                result.append((buy_day, sell_day))
            buy_price = a[i]
            buy_day = i
            sell_price = 0
            sell_day = 0
            
    return result        

def stock_by_sell2(price):
    result = []
    n = len(price)
    if (n == 1):
        return
    i = 0
    while (i < (n - 1)):
        while ((i < (n - 1)) and 
                (price[i + 1] <= price[i])):
            i += 1

        if (i == n - 1):
            break
        
        buy = i
        i += 1

        while ((i < n) and (price[i] >= price[i - 1])):
            i += 1
            
        sell = i - 1
        
        result.append((buy, sell))
            
    return result
        
print(stock_buy_sell(a1))
