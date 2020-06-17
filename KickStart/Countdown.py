t = int(input())
ans = []

for z in range(t):
    num = list(map(int, input().split()))
    array = list(map(int, input().split())) 
    countdown = []
    a = num[1]
    count = 0
    for i in range(num[1]):
        countdown.append(a)
        a = a-1
    i = 0
    while i < len(array):
        if array[i] == num[1]:

            if i+num[1] <= len(array) and array[i:i+num[1]] == countdown:
                count +=1
                i = i+num[1]
            else:
                i = i+1
        else:
            i= i+1
    ans.append(count)

for i in range(t):
    print("Case #" + str(i+1) + ": " + str(ans[i]))