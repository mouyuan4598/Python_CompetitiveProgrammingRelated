t = int(input())
ans = []
for z in range(t):
    n = int(input())
    time = []
    sortedtime = []
    for i in range(n):
        time.append([])
    for i in range(n):
        for x in input().split():
            time[i].append(int(x))
    for i in time:
        sortedtime.append(i)
    
    for i in range(1,len(sortedtime)):
        key = sortedtime[i]
        key_value = sortedtime[i][0]
        j = i-1
        while (j>-1 and sortedtime[j][0] > key_value):
            sortedtime[j+1] = sortedtime[j]
            j = j-1
        sortedtime[j+1] = key

    j_free = -1
    c_free = -1
    work = {'j': [], 'c':[]}
    answer = ''
    imp = False
    for i in sortedtime:
        if c_free <=i[0]:
            c_free = -1
        if j_free <=i[0]:
            j_free = -1

        if c_free == -1:
            c_free = i[1]
            work['c'].append(i)
        else:
            if j_free == -1:
                j_free = i[1]
                work['j'].append(i)
            else:
                imp = True

    print (work)

    for i in time:
        
        if imp == True:
            answer = "IMPOSSIBLE"
            break
        elif i in work['c']:
            k=0
            for j in work['c']:
                if j == i:
                    work['c'].pop(k)
                k = k + 1
            answer = answer + "C"
        elif i in work['j']:
            k=0
            for j in work['c']:
                if j == i:
                    work['j'].pop(k)
                k = k + 1
            answer = answer + "J"
        
    ans.append(answer)

for i in range(t):
    print("Case #" + str(i+1) + ": " + ans[i])
