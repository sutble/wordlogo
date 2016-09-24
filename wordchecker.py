import sys

readFile = open('words.txt')
writeFile = open('finalList.txt','w')
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for line in readFile:
    max = -1;
    count = 0;
    line = line.replace("'","")
    line = line.replace("/","")
    for c in line.rstrip():
        position = alphabet.index(c)
        if(position > max):
            max = position
            count = count+1

    if(count == (len(line)-1) and (len(line)-1 >= int(sys.argv[1]))):
        writeFile.write(line)
readFile.close()
writeFile.close()
