count = 0
def binarySearch (arr, l, r, x):
    global count 
    if r >= l: 
        mid = l + (r - l) // 2
        if arr[mid] == x: 
            for i in arr:
                if i==x:
                    count +=1 

            print ("found")
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid + 1, r, x) 

num = input()
array = list(map(int, input().split())) 
array = sorted(array)

sumup = sum(array)
x = 0 
while x*x <=sumup:
    x+=1
target = []
for i in range(x):
    target.append(i*i)

sublist = []
for i in range(len(array) + 1): 
    for j in range(i + 1, len(array) + 1): 
        sub = array[i:j] 
        sublist.append(sub) 
print(sublist)
sub = sorted(sub)

for i in target:
    binarySearch (sub, 0, len(sub), i)

print (count)
