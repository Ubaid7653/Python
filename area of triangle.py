
#taking input from the user :
a=float(input("enter your a value:"))
b=float(input("enter your b value:"))
c=float(input("enter your c value:"))
#calculate a semi premeter    
s=(a+b+c)/2
#calculate area of triangle:
lenght=(s*(s-a)*(s-b)*(s-c)) ** 0.5
print('the area of triangle is %0.2f ' %lenght)