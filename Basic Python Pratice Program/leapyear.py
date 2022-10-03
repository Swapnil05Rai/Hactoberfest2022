y=int(input())
if (y%100==0 and y%400==0) or y%4==0: 
    print("The entered year is a leap year")
else: 
    print("The entered year is not a leap year")
