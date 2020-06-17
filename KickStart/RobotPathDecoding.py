t = int(input())
ans=[]
for p in range(t):
    coordinate = [1,1]

    def move(x):
        if x == "E":
            coordinate[0] +=1
            if coordinate[0] >1000000000:
                coordinate[0] = 1
        elif x == "S":
            coordinate[1] +=1
            if coordinate[1] >1000000000:
                coordinate[1] = 1
        elif x == "W":
            coordinate[0] -=1
            if coordinate[0] <1:
                coordinate[0] = 1000000000
        elif x == "N":
            coordinate[1] -=1
            if coordinate[1] <1:
                coordinate[1] = 1000000000
    def progress(s):
        i = 0
        while i < len(s):
            a=0
            b=0
            if s[i].isdigit():
                a+=1
                j=i+2
                k = j
                while a!=b:
                    if s[k].isdigit():
                        a+=1
                        k=k+2
                    elif s[k] == ")":
                        b+=1
                        k=k+1
                    else:
                        k=k+1
                for z in range(int(s[i])):
                    progress(s[j:k])
                i=k
            else:
                move(s[i])
                i = i + 1
    s = input()
    progress(s)
    ans.append(coordinate)

for i in range(t):
    print("Case #" + str(i+1) + ": " + str(ans[i][0])+ " " + str(ans[i][1]))