file=open('test.txt',"r")
lines=file.read().split('\n')
for line in lines:
    for words in line.split(' '):
        word=words.strip()
        if word=="" or word==" " or len(word)<3:
            continue
        print(''.join(char for char in word if char.isalnum()))
file.close()
