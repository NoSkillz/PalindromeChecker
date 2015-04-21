__author__ = 'VerDe'


def palindrome_checker(s):
    new_string = ""
    for i in range(len(s), 0, -1):
        new_string += s[i-1]
    return new_string

done = False
while not done:
    user_string = input("Enter a string to check if it's a palindrome, or 'quit' to exit: ").lower()
    if user_string == "quit":
        done = True
    else:
        reversed_string = palindrome_checker(user_string)
        if reversed_string == user_string:
            print("'{0}' is a palindrome.".format(user_string))
        else:
            print("'{0}' backwards is '{1}'. It's not a palindrome".format(user_string, reversed_string))

