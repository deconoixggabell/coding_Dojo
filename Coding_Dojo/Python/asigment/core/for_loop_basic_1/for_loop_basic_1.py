# save
for i in range(0,151):
    print(i)

for i in range(5,1001,5):
    print(i)

for i in range(1,101):
    print(i)
    if i in range(5,101,5):
        print("Coding")
    if i in range(10,101,10):
        print("Coding Dojo")

sum = 0
for i in range(0,500001, 2):
    sum += i
print(sum)

for i in range(2018,0,-4):
    print(i)

lownum = 2
highnum = 9
mult = 3
for i in range(lownum, highnum +1 ):
    if i % mult == 0:
        print(i)