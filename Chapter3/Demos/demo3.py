# using list through for loop
for x in [1,2,3,4]:
    print(x)

print(list(range(1,5)))

for x in "Hi I am SUN":
    if x == " ":
        continue
    else: 
        print(x,end=" ")