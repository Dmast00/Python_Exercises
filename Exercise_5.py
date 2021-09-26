File_name = input('File Name: ')
open_fn  = open(File_name+'.txt','r')
count = 0
val =0
for lines in open_fn:
    word = lines.split()
    if not lines.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        val = val+ float(word[1])
        count+=1

total = val/count
print(f'Average Spam Confidence: {total}')
