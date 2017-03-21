import sys
def finalPrice(prices):
    cost = 0
    n = len(prices)
    dis_list = [0]*n
    non_dis = []
    dis = dict()
    tem = []
    # for i in range(n):
    #     max = max(sort_price)
    #     for j in range(n-i-1):
    #         if prices[i]>=prices[j+i+1]:
    #             dis_list[i]=prices[j+i+1]
    #             break
    for index, price in enumerate(prices):
        while tem and tem[-1][1]>=price:
            ind, pri =tem.pop()
            dis[ind] = price
        tem.append((index,price))

    for index, price in enumerate(prices):
        if index in dis:
            dis_list[index]=dis[index]

    for i in range(n):
        curr_dis = dis_list[i]
        cost+= prices[i]-curr_dis
        if curr_dis==0:
            non_dis.append(i)
    print cost
    for item in non_dis:
        print item,

prices = [1,3,3,2,5]
finalPrice(prices)

