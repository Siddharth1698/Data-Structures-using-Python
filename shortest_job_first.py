#CPU scheduling
#Non preemptive sjf
def schedule(l):
    l.sort()
    x=0
    for i in range(0,len(l)):
        x=x+l[i]
        print("Job",i+1," completed in",x)

schedule([5,3,2,6,11,4])
