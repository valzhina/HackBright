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
06.01 Go
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

""" Go/ Practice 
Given a collection of sorted numbers. Find a matching pair that is equal to a sum (target)
[2,7,12,33] --> Sum 8 --> False
[2,3,4,4] --> Sum 8 --> True
"""

def find_match_pair_sorted(array:list, target:int):
    """Option I *** O(n^2)"""
    # for i in range(len(array)-1):
    #     for j in range(i + 1, len(array)):
    #         if array[i] + array[j] == target:
    #             return True
    #             break
    #     i += 1
    # return False

    """Option III *** O(n)"""
    low = 0
    hi = len(array)-1
    while low < hi:
        sum_of_n = array[low] + array[hi]
        if sum_of_n == target:
           return True
        elif sum_of_n < target:
            low += 1
        else:
            hi -=1
    return False

    """Option II *** O(n*log(n)) binary search"""
    # for i in range(len(array)-1):
    #     if binary_search(array[i + 1:], target - array[i]):
    #        return True
    #     i += 1
    # return False

# def binary_search(array:list, complement:int):
#     """searches for target"""
#     index_l = 0
#     index_r = len(array)
#     while index_l < index_r:
#         index_mid = (index_l + index_r)//2
#         if array[index_mid] == complement:
#             print (f"index_mid= {index_mid}")
#             return True
#         elif array[index_mid] > complement:
#             index_r = index_mid
#             print (f"index_r= {index_r}")
#         else:
#             index_l = index_mid + 1
#             print (f"index_l= {index_l}")
#     return False

# print (find_match_pair_sorted([2,3,4,4], 8))
# print (find_match_pair_sorted([2,3,4,9], 8))


"""
Given a collection of not sorted numbers. Find a matching pair that is equal to a sum (target)
[2,7,12,33] --> Sum 8 --> False
[2,3,4,4] --> Sum 8 --> True
"""

def find_match_pair(array:list, target:int):
    """Option I *** O(n*log(n)) solution if I sorted first and use a function Option 3 from above"""
    # array.sort() #O(n*log(n))
    # return find_match_pair_sorted(array, target) #O(n)

    """Option II *** O(n) solution """
    complements = set()
    for item in array: 
        if target - item in complements:
            return True
        else:
            complements.add(target - item)
    return False

    """Option III *** O(n) solution if index ever needed"""
    # complements = set()
    # for i in range(len(array)): 
    #     if target - array[i] in complements:
    #         return True
    #     else:
    #         complements.add(target - array[i])
    # return False

# print (find_match_pair([2,3,4,4], 8))
# print (find_match_pair([2,3,4,9], 8))


##############################################################################
# Max Font Leed Code
##############################################################################

"""
06.23 Go
Part 1
Given a paper with a given width, height [10x10] and supported min/max font size[7,1,3,5,12], determine the max font a given string can be displayed in.
Word or character can’t be broken. Imagine a method getWidth(char c, int fontSize) and getHeight(int fontSize) are given.

   3   3   3  1
3 111 111 111 1
3 111 111 111 1
3 111 111 111 1
1  1   1   1

   3   3   3  1
1 1T1 1h1 1e1 1
2 1*1 1s1 1k1 1
3 1y1 111 111 1 --> True

     7     3
7 111t111 111
3 111         --> False
"""

def fit_check(sentence, font_size, paper):
    length = len(sentence)
    
    possible_char_w = paper[0] % font_size # 10//3 --> 3
    possible_char_h = paper[1] % font_size # 10//3 --> 3

    if possible_char_w * possible_char_h >= length:
        return True
    return False

def find_max(sentence, font_size, paper):
    result = fit_check(sentence, font_size, paper)


##############################################################################
# Plank
##############################################################################
"""Given an array: 

A road with potholes: [=,o,=,=,o,=,o,=,=,o,o,o,=,o]
Another array plank that can cover some road:[x], For example [7]
Plank:                [=,=,=,=,=,=,=]
Result1:                            [ , ,o,o,o, ,o] --> 4 potholes stay ancovered
Result2:                          [ ,o, ]+[o,o, ,o] --> 4 potholes stay ancovered
Result3:                            [ ,o, , ,o, ,o] --> 3 potholes stay ancovered --> Best Result Return

"""
def planks(street, plank[int]):
    
    i = 0
    result = len(street) # chose max len possible
 
    while i<len(street)-plank:
        if street[i]== True: # if we use line 25 we need it if we don't use line 25 we dont need it
            potholes = check_potholes(street, i, plank)
            result = min(result, potholes)
            while i<len(street) and street[i]==True: # here we pass all true values YOU NEED IT
                i+=1
        i+=1 
    return result


def check_potholes(street, i, plank):
    s1 = street.copy() # not to modify original street
    
    while i < len(s1) and plank > 0:
        s1[i]=False
        plank-=1
        i+=1
    
    return sum(s1)


##############################################################################
# Go  
##############################################################################
'''
c. Given multiple unsorted lists, how can you quickly merge them?

a. find the longest substring with n different letters
"aababcd", n=3 => "aababc"

b. find number who has a pair in array (even negative number)

[1,2,3,4,5,-5] => return 5

given two binary trees, return true/false if one is a subtree of another.

coding question on birthday candle problem.

Binary search tree problem, A lot of string problems

DSA

a knapsack problem

What is the time complexity of Djikstra's Algorithm

Linked list version of the "Island Counting" problem

Why should one use merge sort over quick sort and vice-versa?



'''