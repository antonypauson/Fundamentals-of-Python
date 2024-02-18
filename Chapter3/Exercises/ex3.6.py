# Construct truth tables for the following Boolean expressions:
# a. not (A or B)
# b. not A and not B

values = [True, False]
print("NOT(A or B)")
for x in values:
    for y in values:
        result = not (x or y)
        print(f"{x} {y} => {result}")

print("not A and not B")
for x in values:
    for y in values:
        result = (not x) and (not y)
        print(f"{x} {y} => {result}")