import numpy as np


def get_more(prices):
    if len(prices) < 2:
        return 0
    dp = [0]*len(prices)
    get = [0]*len(prices)
    for i in range(1, len(prices)):
        get[i] = prices[i]-prices[i-1]
    get[0] = -7
    # print(prices)
    dp[0] = 0
    for i in range(1, len(get)):
        dp[i] = max(dp[i-1]+get[i], get[i])
    return max(dp)


prices = np.random.randint(0, 100, 20)
print(prices)
print(get_more(prices))
