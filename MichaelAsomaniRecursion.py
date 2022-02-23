# Author - Michael Asomani        Date - 11/17/21
# Purpose - Write a recursive function that takes a string as input 
# and returns True if the string is valid with respect to matched parentheses.

def parentheses(s):
    length = len(s)
    
    '''Recursion method for parentheses matching'''
    if length == 0: # If string is empty
        return True # then return true
    elif s[0] == ")" or length % 2 != 0: # If it starts with ) or its odd
        return False                     # then return false
    else:
        '''If the parentheses matches'''
        s = s.replace("()", "") # Deletes the parentheses
        return parentheses(s[0:]) # Calls back to the function

#test_str = input("Enter a valid string of parentheses that only has ( or ), ")

# -------------------------- Tests for parentheses
assert parentheses("()()(())")
assert not parentheses("(())))")