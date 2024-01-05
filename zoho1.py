a = input("Enter the string:")
open_braces = 0
close_braces = 0

for hari in a:
    if hari == "(":
        open_braces += 1
    elif hari == ")":
        close_braces += 1
    else:
        pass
if open_braces == close_braces:
    print("Open braces=",open_braces,"Close braces=",close_braces)
    print("Balanced")
else:
    print("Open braces=",open_braces,"Close braces=",close_braces)
    print("Not balanced")
