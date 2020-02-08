colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Purple", "Pink", "Brown", "Teal", "Turquois", "Peach", "Beige"]

newColors = []


for position in range(len(colors)):
    color = colors[position]
    print(color)
    if color[0] not in ["P", "B", "T"]:
        newColors.append(color)
        
colors = newColors        
print(colors)

print ("*******************Second Start*******************************")
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Purple", "Pink", "Brown", "Teal", "Turquois", "Peach", "Beige"]

for color  in colors:
    if color[0]  in ["P", "B", "T"]:
        print(color)
        colors.remove(color)
        
print(colors)    