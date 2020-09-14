myStr = "Hello world"
mySta = "Yes"

print("My name is" + myStr)
print(f"My name is {myStr}") #Otra forma de concatenar una funcion es con f
print("My name is {} because {}".format(myStr,mySta))

dir(myStr)

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
myStr.replace("Hello","Bye")
myStr.count("l")

print(myStr.startswith("hola"))
print(myStr.endswith('world'))

myStr.split('o') #separa apartir de lo que tu metas en el parametro
myStr.find('o')

print(len(myStr))
print(myStr.index('e'))

print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[4])
