with open("Input.txt", "r", encoding="utf-8") as f:
    lineas = f.read().splitlines() 


total = 0
cleanlineas = list(map(str.split, lineas))
operations = cleanlineas[len(lineas)-1]

for i in range(0, len(operations)):
    result = int(cleanlineas[0][i])
    operation = operations[i]
    for j in range(1, len(lineas)-1):
        operator = int(cleanlineas[j][i])
        if operation == "+" : result += operator
        else : result *= operator
    total += result
    
print(total)
    