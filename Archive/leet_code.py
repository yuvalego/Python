# 1/150 
# TwoSum: return the indexes of the items that sum up to the target

# Solution 1 - brute force | complexity O(n^2) #
def twoSum(nums, target):
        index_array = []
        for i in range(len(nums)):
            x = nums[i]
            for j in range(i+1, len(nums)):
                y = nums[j]
                if (x + y) == target:
                    return [i, j]

# Solution 2 - hashmaps | complexity O(n) #
def twoSum(nums, target):
        prev_map = {}
        for i in range(len(nums)):
            x = nums[i]
            diff = target - x
            if diff in prev_map:
                return [prev_map[diff], i]
            else:
                prev_map[x] = i

# 2/150 
# containsDuplicate : return a boolean value of if the list contains a duplicate item

# Solution 1 - hashmaps | complexity O(n) #
def containsDuplicate(nums):
    prev_map = {}
    for i, num in enumerate(nums):
        if num in prev_map:
            return True
        else:
            prev_map[num] = i
    return False

# 3/150 
# isAnagram : return is one string has the exact same letters in a different string but in a different order #

# Solution 1 - hashmaps | complexity O(n) #
def isAnagram(self, s, t):
    if len(s) != len(t):
        return False
    
    s_count, t_count = {}, {}
    for i in range(len(s)):
        s_count[s[i]] = 1 + s_count.get(s[i], 0)
        t_count[t[i]] = 1 + t_count.get(t[i], 0)
    return s_count == t_count

# 4/150
# isPalindrome : return whether a certain string is a palindroeme or not 

# Solution 1 - two pointers | complexity O(n) #
def isPalindrome(s):
    text = ''.join([char.lower() for char in s if char.isalnum()])
    for i in range(len(text)):
        if text[i] != text[-(i+1)]:
            return False
    return True

# Solution 2 - string manipulation | complexity O(n) #
def isPalindrome(s):
    text = ''.join([char.lower() for char in s if char.isalnum()])
    if text == text[::-1]:
        return True
    return False

# 5/150 
# Single Number : returns the number which appears only once in the array

# Solution 1 - hashmap | complexity O(n) #
def singleNumber(nums):
    numbers_dict = {}
    for num in nums:
        numbers_dict[num] = 1 + numbers_dict.get(num, 0)
    for num in numbers_dict:
        if numbers_dict[num] == 1:
            return num
# Solution 2 - bit manipulation | complexity O(n) #
def singleNumber(nums):
    rem = 0
    for num in nums:
        rem = rem^num
    return rem

# 6/150 
# Palindrome Number : return wether a number is a palindrome 

# Solution 1 - math | complexity O(n) #
def isPalindrome(x):
    if x < 0:
        return False
    number = x
    reversed_number = 0 
    while number >= 10:
        reversed_number = (reversed_number * 10) + number % 10
        number //= 10
    return reversed_number == x

def topKFrequent(nums, k):
    num_count = {} # key: all numbers val: number of occurrences
    for num in nums:
        num_count[num] = 1 + num_count.get(num, 0)
    
    sorted_by_apperance = sorted(
        num_count.items(), 
        key=lambda item: item[1], 
        reverse=True
        )

    return [item[0] for item in sorted_by_apperance[:k]]



s = '[{()}][][]'
def isValid(s: str) -> bool:
    hashmap = { ")" : "(", "]" : "[", "}" : "{" }
    stack = []
    for char in s:
        if char in hashmap: # if closing bracket
            if stack and stack[-1] == hashmap[char]: # chack match from top
                stack.pop() # pop if match
                
            else: # if no match return false
                return False
        else: # if is opening, add the stack until match
            stack.append(char)
    return not stack # return true if the stack is empty and false is there are stil unmatched brckets

print(isValid(s))
