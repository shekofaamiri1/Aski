ch = input("Enter a char: ")

if len(ch) != 1:
    print("please enter a character:")
elif '0' <= ch <= '9':
    print("your char is number.")
elif 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
    print("your char is letter.")
else:
    print("other!")
