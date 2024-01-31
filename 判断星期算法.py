import datetime
a,b,c=2024,1,10
d,e,f=2024,1,20
m,n,p=2024,2,16

year1,week1=datetime.date(a,b,c).isocalendar()[:2]
year2,week2=datetime.date(d,e,f).isocalendar()[:2]
year3,week3=datetime.date(m,n,p).isocalendar()[:2]

if year1==year2==year3:
    if week1!=week2 and week1!=week3 and week2!=week3:
        print(True)
    else:
        print(False)
elif year1==year2!=year3:
    if week1!=week2:
        print(True)
    else:
        print(False)
elif year1!=year2==year3:
    if week2!=week3:
        print(True)
    else:
        print(False)
elif year1==year3!=year2:
    if week1!=week3:
        print(True)
    else:
        print(False)



