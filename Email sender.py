file = 'C:/Users/anupr/.PyCharmCE2018.3/config/scratches/email-sender-ith-maximum-no.-of-emails-python/Dataset.txt'

fileContent = open(file)
fileRead = fileContent.read()
words = fileRead.split()

dictionary1 = dict()
for i in range(0,(len(words)-1)):
    if words[i]=='From':
        dictionary1[words[i+1]] = dictionary1.get(words[i+1],0)+1


maximum1 = max(dictionary1.values())

for k,v in dictionary1.items():
    if v==maximum1:
        print(k,v)
