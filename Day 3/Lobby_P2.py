with open("Input.txt", "r", encoding="utf-8") as f:
    lineas = f.read().splitlines() 

maxJoltage = 0

for linea in lineas:
    pos = 0
    size = 12
    while pos < len(linea):
        digit = int(linea[pos])
        digitRange = len(linea) - size + 1
        digitRange = min(digitRange, (len(linea)))
        maxDigit = digit
        maxpos = pos
        
        for z in range(pos+1, digitRange):
            if(int(linea[z])>maxDigit):
                maxDigit = int(linea[z])
                maxpos = z
        
        pos=maxpos+1
        size-=1
        
        maxJoltage += (10**size)*maxDigit
        if(size==0) : break
    

print(maxJoltage)