#list exercise
antibiotics = ['amoxicillin', 'azithromycin', 'cephalexin', 'ciprofloxacin', 'daptomycin', 'doxycycline']
print(antibiotics)

#slicing the list:
abx_1 = antibiotics[:2]
abx_2 = antibiotics[2:4]

print("The first two items in the list are:", abx_1)
print("The middle two items in the list are:", abx_2)

#using index
print('The first and last items in the list are:', antibiotics[0],',', antibiotics[5])

#Tuple exercise: menu
menu = ('tofu', 'chicken', 'beef', 'steak', 'shrimp')

#print in a loop
for food in menu:
    print(food)

#updated menu
menu = ('tofu', 'chicken', 'beef', 'pork', 'tempeh')

#print update menu
for food in menu:
    print(food)