file = open('words.txt','r')
count = 0
for lines in file:
    print(lines.strip())
    count+=1

print(f'Lines : {count}')