# Write code below 💖

print('''
=======================
Area Calculator
=======================
''')


shape = 0
area = 0

print('''
1. Triangle
2. Rectangle
3. Square
4. Circle
5. Quit

 ''')

shape = int(input("Choose your shape (1-5): "))

while shape in [1,2,3,4]:
  base = int(input("Base: "))
  height = int(input("Height: "))
  if shape == 1:
    area = base ** 2
    print("The area of the shape is " + str(area) + ".")
  elif shape == 2:
    area = base * height
    print("The area of the shape is " + str(area) + ".")
  elif shape == 3:
    area = (height * base)/2
    print("The area of the shape is " + str(area) + ".")
  elif shape == 4:
    area = 3.14 * (.5 * base)**2
    print("The area of the shape is " + str(area) + ".")
  else:
    print("Sorry, try again.")

if shape == 5:
  print("Ok, see you later.")



