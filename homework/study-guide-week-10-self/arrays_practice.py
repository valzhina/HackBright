# Centered Avg

"""Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
Example:

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3 """

def centered_average(nums):
    """""""""Arrays"""""""""
    nums.sort()
    nums2 = nums[1:-1]
    sum = 0
    for i in range(len(nums2)): #for n in nums will also work
        sum += nums2[i] #sum of all nums in array
    return sum/len(nums2) 

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
Explanation: In this case, no transactions are done and the max profit = 0."""


#O(n)
def best_time_to_buy_and_sell(prices):
    """Arrays"""
    buy = prices[0]
    profit  = 0
    for item in prices:
        if item < buy:
            buy = item
        if item - buy > profit:
            profit = item - buy
    return profit

# Solution II //O(nlog_n)

    # profit = 0
    # i = prices.index(max(prices))
    # prices_to_use = prices[:i+1]
    # prices_to_use.sort()# O(nlog_n)
    # profit = prices_to_use[-1] - prices_to_use[0]
    # return profit

# Solution III
    # buy = prices[0]
    # profit  = 0
    # for i in range(len(prices)):
    #     if prices[i] < buy:
    #         buy = prices[i]
    #     if prices[i] - buy > profit:
    #         profit = prices[i] - buy
    # return profit

# Solution III
    # for i in range(len(prices)):
    #     if prices[i] < buy:
    #         buy = prices[i]
    #     profit = max(prices[i] - buy, profit)
    # return profit

# print (best_time_to_buy_and_sell([7,1,5,3,6,4]))


##############################################################################

"""05.27 Affoo
"""
##############################################################################

"""
06.01 Goo
Part 1
Input [22,5,8,44,60,22,23,44]  target = 22 ->  Sorted [5,8,22,22,23,44,44,60] -> index[2,3]

Given an array and target. The goal is to find the target in array, sort it and return target's index.
If the target(number) used a few times --> return all indexes, if it's empty -> return empty list []"""

def find_index_w_target(array:list, target:int):
    """Array Option 1 : Time (O(n))"""
    left = 0
    right = 0
    for item in array:
        if item < target:
            left += 1
        elif item > target:
            right += 1
    return list(range(left, len(array) - right))

    # """Array Option 2 (Slow n*log(n) option)"""
    # index = []
    # array.sort()
    # for i in range(len(array)):
    #     if array[i] == target:
    #         index.append(i) 
    #         if i < len(array)-1 and  array[i + 1] != target:
    #             break
    # return index 

# print (find_index_w_target([22,5,8,44,60,22,23,44,22], 60))


# Part 2
"""Input [22,5,8,11,23,60,22,23,44] ->  Sorted [5,8,11,22,22,23,23,44,60] -> index[3,4]

Given an array. The goal is to find the most often number in array, sort it and return it's index.
If the target(number) used a few times --> return all indexes, if it's empty -> return empty list []
if the same number happens the same number of times --> return the smollast """


def find_index(array:list):
    """Dict"""
    d ={}
    count = 0
    for item in array:
        d[item]= d.get(item, 0) + 1
        if d[item] > count:
            count = d[item]

    target = []
    for item, number in d.items():
        if count == number:
            target.append(item)
    target.sort()
    return find_index_w_target(array, target[0])

# print (find_index([5,8,11,22,22,23,23,44,60]))


##############################################################################

""" Goo Practice 
Given a collection of sorted numbers. Find a matching pair that is equal to a sum (target)
[2,7,12,33] --> Sum 8 --> False
[2,3,4,4] --> Sum 8 --> True

"""

def find_match_pair(array:list, target:int):
    """O(n^2)"""
    # for i in range(len(array)-1):
    #     for j in range(i + 1, len(array)):
    #         if array[i] + array[j] == target:
    #             return True
    #             break
    #     i += 1
    # return False

    """O(n*log(n))recursive binary search"""
    for i in range(len(array)):
        if binary_search(array[i + 1:], target - array[i]):
           return True
        i += 1
    return False

def binary_search(array:list, complement:int):
    l = 0
    r = len(array)
    while l < r:
        mid = (l + r)/2
        if array[mid] == complement:
            return True
        elif array[mid] > complement:
            r = mid
        else:
            l = mid + 1
    return False


#print (find_match_pair([2,3,4,4], 8))


##############################################################################