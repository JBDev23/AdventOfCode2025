with open("Input.txt", "r", encoding="utf-8") as f:
    lineas = f.read().splitlines() 
    
startpos = lineas[0].find("S")
beams = [0] * len(lineas[0])
beams[startpos] = 1
count = 0

for i in range(1, len(lineas)):
    linea = list(lineas[i])
    new_beams = list(beams)
    for j, x in enumerate(beams):
        if(x==1):
            if(linea[j]=="^"):
                count+=1
                if j > 0 and new_beams[j-1] != 1:
                    new_beams[j-1] = 1
                if j < len(beams) and new_beams[j+1] != 1:
                    new_beams[j+1] = 1
                new_beams[j] = 0
    beams = new_beams
print(count)