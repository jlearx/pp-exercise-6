'''
Created on Sep 14, 2017

@author: jlearx
'''

def isPalindrome(inputStr):
    forward = inputStr
    backward = inputStr[::-1]
    return (forward == backward)

if __name__ == '__main__':
    userStr = input("Please enter a string: ").strip()
    palindrome = isPalindrome(userStr)
    
    if (palindrome):
        print("That string is a palindrome.")
    else:
        print("That string is NOT a palindrome.")
        