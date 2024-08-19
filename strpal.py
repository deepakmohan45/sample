str="malayalam"
str=str.casefold()
reverse=reversed(str)
if list(str)==list(reverse):
    print("string is palindrome")
else:
    print("string is not palindrome")    
