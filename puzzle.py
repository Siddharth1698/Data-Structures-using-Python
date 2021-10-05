#a,b,c,d = soldiers on left, boys on left, soldier on  right, boys  on right
#e = where is boat; 0 on left, 1 on right
#If 2 boys are initially on right side
x=0

def boat(a,b,c,d,e):
    global x
    print(a,b,c,d,e)
    if(((c==(a+b+c+d)-2) and d==2) or ((c==(a+b+c+d)-2) and b==2)):
        print("Destination Reached",a,b,c,d,e)
        print("Number of Times boat travelled: ",x)
        return 0
    else:
        if (b==2 and e==0):
            print("2 Boy going right")
            x=x+1
            boat(a,b-2,c,d+2,1)
        elif (a!=0 and d==2 and e==1):
            print("1 Boy going left")
            x=x+1
            boat(a,b+1,c,d-1,0)
        elif (b==d==1 and a!=0 and e==0):
            print("1 Soilder going right")
            x=x+1
            boat(a-1,b,c+1,d,1)
        elif (b==d==1 and a!=0 and e==1):
            print("1 Boy going left")
            x=x+1
            boat(a,b+1,c,d-1,0)
        elif (b==d==1 and a==0 and e==1):
            print("1 Boy going left")
            x=x+1
            boat(a,b+1,c,d-1,0)

boat(5,2,0,0,0)
