t = int(input())
ans = []
for z in range(t):
    mat = []
    mat2 = []
    n = int(input())

    for i in range(n):
        mat.append([])
        mat2.append([])

    for i in range(n):
        k = 0
        for j in input().split():
            mat[i].append(int(j))
            mat2[k].append(int(j))
            k = k + 1
    trace = 0
    r = 0 
    while mat:
        a = mat.pop()
        n = n -1
        trace = trace + a[n]
        while a:
            b = a.pop()
            if b in a:
                r = r + 1
                break
    c = 0
    while mat2:
        a = mat2.pop()
        while a:
            b = a.pop()
            if b in a:
                c = c + 1
                break
    ans.append([0,0,0])
    ans[z][0] = trace
    ans[z][1] = r
    ans[z][2] = c

for i in range(t):
    print("Case #" + str(i) + ": " + str(ans[i][0]) + ' ' + str(ans[i][1]) + ' ' + str(ans[i][2]))