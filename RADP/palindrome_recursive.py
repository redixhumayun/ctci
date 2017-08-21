def isPalindrome(string):
    '''
    A method that will recursively decide if a string is a palindrome
    '''
    if len(string) < 2:
        return True
    if string[0] != string[-1]:
        return False
    return isPalindrome(string[1:-1])




if __name__ == "__main__":
    string = 'anna'
    result =  isPalindrome(string)
    print(result)
