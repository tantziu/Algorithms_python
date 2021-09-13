def maxProfit(a):
    profit = 0
    buy = a[0]
    result = 0
    for i in range(1, len(a)):
        if a[i] - buy > profit:
            profit = a[i] - buy
            print('profit:', profit)
            # if i == len(a)-1:
            #     result += profit
        if a[i] - buy < profit:
            buy = a[i]
            print('min_el:', buy)
            result += profit
            profit = 0
        if a[i] < buy and profit < 0:
            buy = a[i]
    result+= profit
    return result


list1 = [7,7,1,5,3,6,4,5]
list2=[1,9,6,9,1,7,1,1,5,9,9,9]
# output: 7
print(maxProfit(list2))
