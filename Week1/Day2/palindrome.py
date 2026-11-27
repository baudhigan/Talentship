def palindrome(text):
    reverse = text[::-1]
    if text==reverse:
        return True
    else:
        return False
    
word = input("Enter the Word:")

if palindrome(word):
    print("Palindrome")
else:
    print("Not Palindrome")