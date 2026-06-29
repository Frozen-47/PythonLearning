string = input("Enter a String :")
reverse = string[:2:-1]
if(string == reverse):
    print("Palindrome")
else:
    print("Not a palindrome")