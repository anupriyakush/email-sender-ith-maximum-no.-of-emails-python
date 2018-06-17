# email-sender-ith-maximum-no.-of-emails-python

file = input("Enter file name: ")
fileContent = open(file)
fileRead = fileContent.read()
words = fileRead.split()

#for j in range(0,(len(words)-1)):
 #   print(words[j])
dictionary1 = dict()
for i in range(0,(len(words)-1)):
    if words[i]=='From':
        dictionary1[words[i+1]] = dictionary1.get(words[i+1],0)+1


maximum1 = max(dictionary1.values())

for k,v in dictionary1.items():
    if v==maximum1:
        print(k,v)


#Desired Output
#cwen@iupui.edu 5
