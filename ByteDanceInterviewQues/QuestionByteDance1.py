k=2
lines = "1 B\n2 A\n5 E\n4 B\n4 A\n2 C\n5 C\n3 B\n4 C\n2 C\0"
i=0
seq={}

while i<len(lines) and lines[i]!='\0':
    if lines[i] in seq:
        seq[lines[i]] = seq[lines[i]] +lines[i+2]
    else:
        seq[lines[i]] = lines[i+2]
    i= i+4 
print(seq)

ans={}

for x in seq:
    if len(seq[x])>=k:
        a=0
        b=a+k      
        while b <= len(seq[x]):
            if seq[x][a:b] in ans:
                ans[seq[x][a:b]] = ans[seq[x][a:b]] + 1
            else:
                ans[seq[x][a:b]] = 1
            print (seq[x][a:b])
            a=a+1
            b=a+k
maxnum = -1
maxseq = ""
for x in ans:
    if ans[x] > maxnum:
        maxnum = ans[x]
        maxseq = x

print (maxseq + ' ' + str(maxnum))