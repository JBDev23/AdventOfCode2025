with open("Input.txt", "r", encoding="utf-8") as f:
    lineas = f.read().splitlines() 

count = 0

for j in range(0,len(lineas)):
    linea = lineas[j]
    for i in range(0,len(linea)):
        char = linea[i]
        if(char == "@"):
            h0scoop = ""
            h1scoop = ""
            h2scoop = ""
            mi = max(0,i-1)
            ma = min(len(linea),i+2)
            
            if(j>0):
                h0scoop = lineas[j-1][mi:ma]
                
            h1scoop= linea[mi:ma]
            
            if(j<len(lineas)-1):
                h2scoop = lineas[j+1][mi:ma]
        
            rolls=0
            rolls += len(h0scoop.replace(".", ""))
            rolls += len(h1scoop.replace(".", ""))
            rolls += len(h2scoop.replace(".", ""))
      
            if(rolls<5): count+=1
      
print(count)