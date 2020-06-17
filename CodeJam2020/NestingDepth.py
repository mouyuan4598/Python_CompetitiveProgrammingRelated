def split(word): 
    return [int(char) for char in word]  

t = int(input())
ans = []
for z in range(t):
    s = input()
    s = split(s)
    start = 0
    ss = ""
    for i in range(len(s)):
        while start < s[i]:
            ss = ss + '('
            start = start + 1
        ss = ss + str(s[i]) 
        if start == s[i] and i+1 < len(s):
            j = s[i+1]
            if j == s[i]:
                pass
            elif j < s[i]:
                while j < s[i]:
                    ss = ss + ')'
                    j = j + 1
                    start = start -1
            else:
                ss = ss + '('
                j = j + 1
                start = start +1
    while start>0:
        ss = ss + ')'
        start = start -1


    ans.append(ss)

for i in range(t):
    print("Case #" + str(i+1) + ": " + ans[i])