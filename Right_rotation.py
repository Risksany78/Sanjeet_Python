string1=eval(input("Enter first string"))
string2=eval(input("Enter the Second string"))
x=string1+string1
if(string2 in x):
	print(string2+ " Is right rotation of " +string1)
else:
	print(string2+" Is NOT right rotation of "+string1)
