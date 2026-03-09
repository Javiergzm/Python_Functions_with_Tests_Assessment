'''
Complete the two functions below to show what
you've learned about writing functions in Python.
All tests must pass to receive credit.
'''
'''sum_list'''
# sum_list takes a list of integers and returns the sum
# of all numbers in the list.
#
# Examples:
#   sum_list([1, 2, 3]) -> 6
#   sum_list([5]) -> 5
#   sum_list([]) -> 0
#
# Requirements:
#   - Must use iteration (a loop)
#   - Do NOT use the built-in sum() function
#   - Do NOT print anything
#
def sum_list(numbers: list) -> int:
    answer = 0
    for char in numbers:
        answer += char
    return answer
    

'''another way to answer it'''    
'''
output = 0
idx = 0 
while index < len(numbers):
    curr_num = numbers[idx]
    output = output + curr_num
    idx += 1
return output
'''


'''count_letter'''
# count_letter takes two arguments:
# a string and a single character.
# It returns the number of times that character
# appears in the string.
#
# Examples:
#   count_letter("hello", "l") -> 2
#   count_letter("banana", "a") -> 3
#   count_letter("apple", "z") -> 0
#
# Requirements:
#   - Must use iteration (a loop)
#   - Must return an integer
#   - Do NOT use the built-in count() method
#   - Do NOT print anything
#
def count_letter(s: str, letter: str) -> int:
    output = 0
    for char in s:
        if letter == char:
            output += 1
    return output



'''another solution'''
'''
count = 0
idx = 0 
while idx < len(s):    #hello
    curr_lettter = s[idx]
    if curr_letter == letter =
        count += 1
return count

'''





''' Extra Credit Challenge'''
''' is_palindrome '''
# is_palindrome takes a string and returns True if the string
# reads the same forwards and backwards. Otherwise return False.
#
# Examples:
#   is_palindrome("racecar") -> True
#   is_palindrome("level") -> True
#   is_palindrome("hello") -> False
#
# Requirements:
#   - Return a Boolean value
#   - Do NOT use the built-in reversed() function
#   - Do NOT print anything
#
def is_palindrome(s: str) -> bool:
    check = True
    reverse_s = ""
    Ranser = ""
    index = len(s) - 1 


    while index >= 0:
        char = s[index]
        reverse_s = reverse_s + char
        index -= 1      #make the list smaller and loop it until you reach the first letter/ number
    if reverse_s == s:
        return True
    else: 
        return False
    return check