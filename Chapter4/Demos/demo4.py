#substring with "in" operator
if ".txt" in "file.txt":
    print("Yes")
filenames = ["myfile.txt",
             "yourfile.txt",
             "myvideo.mp4",
             "mypdf.pdf"]
for filename in filenames:
    if ".txt" in filename:
        print(filename)