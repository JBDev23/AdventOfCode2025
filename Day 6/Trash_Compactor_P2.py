with open("Input.txt", "r", encoding="utf-8") as f:
    lineas = f.read().splitlines() 


columnas = list(zip(*lineas[0:len(lineas)-1]))
operations = lineas[len(lineas)-1].split()

total = 0
op = 0
result = None
i = 0
while i < len(columnas):
    columna = columnas[i]
    if(len(columna) == columna.count(" ")) : 
        total += result
        op += 1
        result = None
        i+=1
        continue
    
    operator = int("".join(columna))
    if result == None: result=operator
    elif operations[op] == "+" : result += operator
    else : result *= operator
    i += 1
            
total+=result
print(total)
    
    
    
    