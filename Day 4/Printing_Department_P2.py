with open("Input.txt", "r", encoding="utf-8") as f:
    grid = [list(linea) for linea in f.read().splitlines()]

count = 0


while True :
    newGrid = [fila[:] for fila in grid]
    changed = False
    for j in range(0,len(grid)):
        
        linea = grid[j]
        for i in range(0,len(linea)):
            char = linea[i]
            if(char == "@"):
                h0scoop = ""
                h1scoop = ""
                h2scoop = ""
                mi = max(0,i-1)
                ma = min(len(linea),i+2)
                if(j>0):
                    h0scoop = grid[j-1][mi:ma]
                
                h1scoop= grid[j][mi:ma]
                
                if(j<len(grid)-1):
                    h2scoop = grid[j+1][mi:ma]
                    
                rolls=0
                rolls += h0scoop.count("@")
                rolls += h1scoop.count("@")
                rolls += h2scoop.count("@")
                
                
                if(rolls<5): 
                    count+=1
                    newGrid[j][i] = "."
                    changed = True
    if(not changed) : break
    grid = newGrid

print(count)
                

            

                
            
            
            
            
            
            
