age = input("Cuantos años tienes? ")
new_age = int(age) + 11

print("Mi edad es: {}".format(new_age))


#--------------------------------------------- LIST -------------------------------------------------------------

demo_list = [1, "hello", 1.34, True,[1,2,3,4]]

colors = ["red", "green", "blue"]

numbers_list = list((1,2,3,4))
#print(numbers_list)

r = list(range(1,10))
print(r)

colors.append("violet")

colors.sort()

colors.extend(("black","pink"))

colors.pop(
colors.index()
)
