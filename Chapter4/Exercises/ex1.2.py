# Assume that the variable data refers to the string "myprogram.exe". Write the 
# expressions that perform the following tasks:
data = "myprogram.exe"
# a. Extract the substring "gram" from data.
print(data[5:9])
# b. Truncate the extension ".exe" from data.
print(data[9:])
# c. Extract the character at the middle position from data
print(data[round(len(data) / 2)])
