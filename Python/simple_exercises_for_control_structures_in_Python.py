"""Simple exercises for control structures in Python."""

heights = [1.82,1.75,1.68,1.76,1.5]

# 0. Use for loop to print values from "heights" list 
print ("0. Use for loop to print values from 'heights' list")
for i in range(len(heights)):
    print (heights[i])
    
# 1. Use for loop for printing only values bigger than 1.75
print ("1. Use for loop for printing only values bigger than 1.75")
for i in range(len(heights)):
    if heights[i] > 1.75:
        print (heights[i])

# 2. Use for loop for printing all values until you find value 1.68 (included)
print ("2. Use for loop for printing all values until you find value 1.68 (included)")
for i in range(len(heights)):
    print (heights[i])
    if heights[i] == 1.68:
        break

# 3. Modify the previous loop to print all values from `"heights"` without value 1.68
print ("3. Modify the previous loop to print all values from 'heights' without value 1.68")
for i in range(len(heights)):
    if heights[i] == 1.68:
        continue
    print (heights[i])

# 4. use for loop over to iterate over `"heights"` and print "high" for values bigger than 1.75, "medium" for values between 1.68 and 1.75 and "small" for values lower than 1.68
print ("4. use for loop over to iterate over 'heights' and print 'high' for values bigger than 1.75, 'medium' for values between 1.68 and 1.75 and 'small' for values lower than 1.68") 
for i in range(len(heights)):
    if heights[i] > 1.75:
        print ("high")
    elif heights[i] < 1.68:
        print ("small")
    else:
        print ("medium")
        
# While Loop
# 1. Print out numbers from 0 to 4
print ("1. Print out numbers from 0 to 4")
i = 0
while i < 5:
    print (i)
    i += 1

# 2. use while loop to print out only even numbers lower than 15
print ("2. use while loop to print out only even numbers lower than 15")
i = 0
while i < 15:
    if i % 2 == 0:
        print (i)
    i += 1

# 3. use while loop to print all numbers lower than 15 but skip first five values
print ("3. use while loop to print all numbers lower than 15 but skip first five values")
i = 0
while i < 15:
    if i < 5:
        i += 1
        continue
    print (i)
    i += 1
    
# ACTORS
actors = [
    "Nathan Fillion",
    "Gina Torres",
    "Alan Tudyk",
    "Morena Baccarin",
    "Adam Baldwin",
    "Jewel Staite",
    "Sean Maher",
    "Summer Glau",
    "Ron Glass"
]

roles = [
    "Captain Malcolm Reynolds",
    "Zoe Washburn",
    "Hoban Washburn",
    "Inara Serra",
    "Jayne Cobb",
    "Kaylee Frye",
    "Dr. Simon Tam",
    "River Tam",
    "Derrial Book"
]
print ("Featuring:")
print ("=====================")
for i in range(len(actors)):
    print (actors[i] + " as " + roles[i])