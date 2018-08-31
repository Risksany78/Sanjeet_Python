string=eval(input("Enter a string containing bad followed by not \n"))
x=string.find("not")
y=string.find("bad")
new=string[x:y+3:]
print(string.replace(new,"good"))

