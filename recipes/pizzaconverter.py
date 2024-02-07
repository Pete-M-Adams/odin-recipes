flour = int(float(input("How many grams of flour do you have? ")))

water = float(flour * .6)
salt = float(flour * .03)
yeast = float(flour * .015)
oil = float(flour * .04)
sugar = float(flour * .01)     

print(" Flour = " + str(flour) + "g \n", "Water = " + str(water) + "g \n", "Salt = " + str(salt) + "g \n", "Yeast = " + str(yeast) + "g \n" , "Olive Oil = " + str(oil) + "g \n", "Sugar = " + str(sugar) + "g \n")