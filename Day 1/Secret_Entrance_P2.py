with open("Input.txt", "r", encoding="utf-8") as f:
    lineas = f.read().splitlines() 

pointer = 50

password = 0

for linea in lineas:
    direction = linea[0]

    movement = int(linea[1:])
    
    password += movement // 100
    
    rest = movement % 100
    
    if(direction == "L"):
        if(pointer != 0 and rest>=pointer) : password+=1
            
        pointer = (pointer-movement)%100
        
    elif (direction == "R"):
        dist = 100 - pointer
        if(rest >= dist) : password+=1
        
        pointer = (pointer+movement)%100
        
print(password)
    
