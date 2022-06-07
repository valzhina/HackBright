"""Instructions:  write a function that takes in a list and reverses it in place. (it’s the same list)

[“cat”, “dog”, “bird”] => [“bird”, “dog”, “cat”]

sudo
find length of list 
write a for loop that takes the index of the last word, and appends that to the list
and then takes that index minus one, appends that to the list - and so forth until including i[0]
and then pop the original order of hte list out of the list

def reverse_list_in_place(given_list):
    left = 0
    right = len(given_list) - 1
    while left < right:
        temp = given_list[left]
        given_list[left] = given_list[right]
        given_list[right] = temp

        right -= 1
        left += 1

l = [8,3,7,5,9,6]
print(l)
reverse_list_in_place(l)
print(l)"""

#####################################################################################
"""Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
non-alphanumeric characters, it reads the same forward and backward.Given a string s, return true if it is a palindrome, or false otherwise.

Example 1: Input: s = "A man, a plan, a canal: Panama"  Output: true  Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2: Input: s = " " Output: true Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


class Solution:
    def isPalindrome(self, s: str) -> bool:
    """ """tbd""" """

    l = 0
    r = len(s)-1
    s = s.lower()
    s1 = ''
    for char in s:
        if char in 'qwertyuiopasdfghjklzxcvbnm1234567890':
            s1 += char
    while l < r:
        if s1[l] == s1[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

print (isPalindrome('.,'))
print (isPalindrome('amanaplanacanalpanama'))      

# Option 2
        l = 0
        r = len(s)-1
        
        while l < r:
            while s[l].lower() not in "qwertyuiopasdfghjklzxcvbnm1234567890" and l<r:
                l+= 1
            while s[r].lower() not in "qwertyuiopasdfghjklzxcvbnm1234567890" and l<r:
                r-= 1
            if s[l].lower() == s[r].lower():
                l+= 1
                r-= 1
            else:
                return False
        return True """


#####################################################################################
"""Given a string s, return the longest palindromic substring in s.
GivInput: s = "babad" Output: "bab" Explanation: "aba" is also a valid answer.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        theLongest = ""# keeps track of the longest Palindrome instance in given str
        
        #iterates through given str
        for i in range(len(s)):
            # Checking odd length palindrome at given i
            word1 = self.checkPalindrome(s, i, i)
            # Checking even length palindrome at given i
            word2 = self.checkPalindrome(s, i, i+1)
            
            #word1 will be max length word from word1 and word2
            if len(word1) >= len(word2):
                word1 = word1
            else:
                word1 = word2

            # compare word1 with current theLongest
            if len(word1) >= len(theLongest):
                theLongest = word1
            
        return theLongest

    
    def checkPalindrome(self, s, l, r):
        # expand as long as 'l' can grow to the left
        # and 'r' and grow to the right and chracters at those index match
        while s[l] == s[r] and l >= 0 and r < len(s):
            l -= 1
            r += 1
        
        # return the slice from original string that starts from our last matched index of l and r
        return s[l+1 : r]

##############################################################################
""" 06.02 Bloo 

Two words are anagrams of one another if their letters can be rearranged to form the other word.
Given two strings, check if they are anagrams. Determine the minimum number of characters to 
change to make the two strings into anagrams of one another.

'xyyx' , 'xxyxb' ->  Through exception
'aabb' , 'abba' ->  2
"""

def anagram(input1, input2):
    """Str"""
    if len(input1) != len(input2):
        raise Exception('not anagrams')
    d = {}
    count = 0
    for letter in input1:
        d[letter] = d.get(letter, 0) + 1

    for letter in input2:
        if letter in d and d[letter] > 0:
            d[letter] -= 1
        else:
            count += 1
    return count

print (anagram('xyxy', 'yxxxx'))    
        
        

##############################################################################


"""Two words are anagrams of one another if their letters can be rearranged to form the other word.
"""