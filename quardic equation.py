import cmath

a=int(input("enter the A value:"))
b=int(input("enter the B value:"))
c=int(input("enter the C value :"))

d=(b**2)-(4*a*c)
sol1=b-cmath.sqrt(d)/(2*a)
sol2=-b-cmath.sqrt(d)/(2*a)
print('the solution of quardic equation  {0} and {1} is '.format(sol1,sol2))