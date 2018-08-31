string=eval(input("Enter a string"))
x=string[0:1:]
y=string[1::]
z=y.replace(x,"*")
print(x+z)