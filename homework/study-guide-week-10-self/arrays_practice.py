# Centered Avg

"""Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
Example:

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
    """ """Arrays""""""
    nums.sort()
    nums2 = nums[1:-1]
    sum = 0
    for i in range(len(nums2)):
        sum += nums2[i]
    return sum/len(nums2)"""

# print(centered_average([-10, -4, -2, -4, -2, 0]))


##############################################################################
# LeetCode 121. Best Time to Buy and Sell Stock

""" You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

def best_time_to_buy_and_sell(prices):
    """Arrays"""
    buy = prices[0]
    profit  = 0
    # for i in range(len(prices)):
    #     if prices[i] < buy:
    #         buy = prices[i]
    #     if prices[i] - buy > profit:
    #         profit = prices[i] - buy
    # return profit

# Solution II
    for i in range(len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        profit = max(prices[i] - buy, profit)
    return profit
print (best_time_to_buy_and_sell([7,1,5,3,6,4]))