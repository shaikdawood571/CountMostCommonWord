# open the file
file1 = open(input("Enter the file name : "))
# read the file
s1 = file1.read()
# split the content in the file
words = s1.split()
# create an empty dictionary
di = dict()
# loop through the words
for w in words:
    di[w] = di.get(w, 0) + 1

# print the dictionary
#print(di)

# take counter number
largest = -1
word = None
# loop through the dictionary
for k, v in di.items():
    if v > largest:
        largest = v
        word = k

# print the largest word and count
print(word, largest)
    
# close the file
file1.close()