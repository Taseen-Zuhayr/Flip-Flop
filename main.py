x = input("Enter something : ")
def palindrome(x):
    y = len(x)-1
    z = 0
    while z<y:
        if (x[z] != x[y]):
            return False
        z += 1
        y -= 1
    return True

if (palindrome(x)):
    print("That is indeed a palindromic something.")
else:
    print("That is NOT a palindromic something.")

