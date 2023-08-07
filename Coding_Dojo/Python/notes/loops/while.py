# while loops
# count = 0
# while count <= 5:
#     print(count)
#     count += 1

# password tries
password_attampt = 3
while password_attampt > 0:
    print(f"you " int(password_attampt) " left")
    password_attampt = password_attampt - 1
else:
    print("you are out of attampts")