with open("Input.txt", "r", encoding="utf-8") as f:
    lineas = f.read().splitlines() 
    
startpos = lineas[0].find("S")
beams = [0] * len(lineas[0])
beams[startpos] = 1
count = 0

for i in range(1, len(lineas)):
    linea = list(lineas[i])
    new_beams = [0] * len(lineas[0])
    for j, cantidad in enumerate(beams):
        if cantidad== 0: continue
        if linea[j] == "^" :
            if j>0 : new_beams[j-1] += cantidad
            if j<len(lineas)-1 : new_beams[j+1] += cantidad
        else:
            new_beams[j] += cantidad
    beams = new_beams
            
total = sum(beams)

print(total)