n = 5
k = 18
start = -1
end = -1
good = False
for i in range(n+1):
    if k == i*n:
        start = i
        good = True
    if k>i*n and k<(i+1)*n:
        start = i
        end = i+1
        break
trace =[]
impossible = True
for i in range(n):
    trace.append(start)

if not good:
    for i in range(2,n-1):
        temptrace=[]
        for q in trace:
            temptrace.append(q)
        for j in range(i):
            temptrace[j] = temptrace[j]+1

        
        if sum(temptrace) == k:
            trace = temptrace
            impossible = False
            break
else:
    impossible = False
        
if not impossible:
    print(trace)
    mat = []

    for i in range(n):
        mat.append([])
        for j in range(n):
            if i == j:
                mat[i].append(trace[i])
            else:
                mat[i].append(0)
        
    
    print (mat)



else:
    print("IMPOSSIBLE")
