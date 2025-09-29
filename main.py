ch = input("Enter a char: ")

if len(ch) != 1:
    print("please enter a character:")
elif '0' <= ch <= '9':
    print("your char is number.")