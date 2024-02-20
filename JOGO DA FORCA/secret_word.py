arq=open('frutas.txt','r')
wordlist=arq.readlines()
for w in wordlist:
    w=w.strip('\n')
print(wordlist)

'''
class sWord:
    def __init__(self):
        pass'''