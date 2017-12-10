def main():
    userYear = input("Please enter a year after 1900: ")
    a = det_a(userYear)
    printout(a,userYear)
    
def printout(a, year):
    a=a+1
    if a == 7:
        k = 1
    elif a==6:
        k = 7
    elif a==5:
        k = 6
    elif a==4:
        k = 5
    elif a==3:
        k = 4 
    elif a==2:
        k = 3
    elif a==1:
        k = 2
        
    for i in range(1,13):
        month =["January","February","March","April","May","June","July","August","September","October","November","December"]
        print month[i-1]
        print
        printDay()        
        for q in range(k-1):
            print "\t",
        monthN = i 
        d = detMonth(year,monthN)
        day = 1
        while day <d+1:
            if k>=1 and k<=7: 
                print "%2d\t"%day,
                k+=1
            else:
                k=1
                print "\n"
                print "%2d\t"%day,
                k+=1
            day+=1
        print "\n\n\n"

def printDay():

    day = ["Sun","Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
    for i in range(7):
        print "%s\t" %day[i],
    print "\n\n",

def detMonth(year,month):
    day = 0
    thirtyone = [1,3,5,7,8,10,12]
    thirty = [4,6,9,11]
    for b in thirtyone:
        if month == b:
            day = 31
            return day
            break
    for b in thirty:
        if month == b:
            day = 30
            return day
            break
    if month ==2:     
        if year%4==0:
            day = 29
            return day                
        else:
            day = 28
            return day
        
def det_a(year):
    a = 0
    day=0
    for i in range (1900,year):
        for j in range(1,13):
            month =j
            year = i
            day = detMonth(year,month)            
            d=1
            while d< day+1:
                if a>=1 and a<=6:
                    a+=1
                else:
                    a=1  
                d+=1
    return a-1

main()
