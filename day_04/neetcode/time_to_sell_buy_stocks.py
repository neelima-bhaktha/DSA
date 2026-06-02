def max_profit(profit):
    l, r = 0, 1
    maxP =0
    while r<len(profit):
        if profit[l]<profit[r]:
            price = profit[r] - profit[l]
            maxP = max(price, maxP)
        else:
            l=r
        r+=1
    return maxP


assert max_profit([10,1,5,6,7,1])==6
print("all pass")