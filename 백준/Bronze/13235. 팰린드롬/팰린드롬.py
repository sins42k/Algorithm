palindrome = input()
palindrome_reserve = palindrome[::-1]

if palindrome == palindrome_reserve : print('true')
elif palindrome != palindrome_reserve : print('false')