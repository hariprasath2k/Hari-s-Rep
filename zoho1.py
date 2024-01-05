a = input("Enter the string:")
count_a = 0
count_b = 0

for hari in a:
    if hari == "(":
        count_a += 1
    elif hari == ")":
        count_b += 1
    else:
        continue
if count_a == count_b:
    print("Open braces=",count_a,"Close braces=",count_b)
    print("Balanced")
else:
    print("Open braces=",count_a,"Close braces=",count_b)
    print("Not balanced")
