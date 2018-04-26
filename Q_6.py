#filename = "test.txt"
file1 = open ("test.txt", "r")#open file in read mode

str2 = file1.read() #store data into str2
print str2 # print that file data
if (str2 == file1.read()):  # compare both file data test == str2
    print ('both string was same ')
else:
    print ('both are different ')#??????
file1.close()
