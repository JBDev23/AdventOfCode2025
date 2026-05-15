with open("Input.txt", "r", encoding="utf-8") as f:
    lineas = f.read().splitlines() 

maxJoltage = 0

for linea in lineas:
    digit1 = int(linea[0])
    digit2 = int(linea[1])
    for i in range(2, len(linea)):
        digit = int(linea[i])
        if(i!=len(linea)-1):
            if digit > digit1:
                digit1 = digit
                digit2 = -1
            elif digit > digit2:
                digit2 = digit
        else:
            if digit>digit2:
                digit2=digit
                
                
    maxJoltage += digit1*10+digit2
    
print(maxJoltage)
        

            
    
