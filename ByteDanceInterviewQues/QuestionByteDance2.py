score=0
follows=[("A","B"),("B","C"),("C","A")]
if(follows[0][0]==follows[-1][1]):
    a=1
else:
    a=0
b=0
for i in range(len(follows)-1):
    if(follows[i][1]==follows[i+1][0]):
        b=b+1
    else:
        pass
result=a+b
print(result)
if(result==len(follows)):
    print(1)