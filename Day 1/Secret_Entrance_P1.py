with open("Input.txt", "r", encoding="utf-8") as f:
    lineas = f.read().splitlines() 

pointer = 50

password = 0

for linea in lineas:
    direction = linea[0]

    movement = int(linea[1:])
    
    if(direction == "L"):
        pointer = (pointer-movement)%100
        
    elif (direction == "R"):
        pointer = (pointer+movement)%100
    
    if(pointer==0) : password += 1
    
print(password)
    
