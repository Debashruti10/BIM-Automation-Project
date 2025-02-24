bta=float(input("enter the net floor area: "))
cost_ass=float(input("enter the cost assessment: "))
d=0.1*cost_ass
r=float(input("enter the net discount rate: "))
n=float(input("enter the amount of year: "))
pvf=(1-((1+r)**-n)/r)
ic=float(input("enter the initial cost"))
kwh=float(input("enter the kilowatt hour"))
e=1*kwh
o=250*bta
m=100*bta
s=float(input("enter the costs fordowntime: "))
env=float(input("enter the CO2 equivalence: "))*0.72
LCC=(ic+e+o+m+s+env+d)*pvf
print("the present value factor is:",pvf)
print("the life cycle cost is",LCC,"SKR")






