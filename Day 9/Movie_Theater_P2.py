with open("Input.txt", "r", encoding="utf-8") as f:
    raw_lines = f.read().splitlines() 
            
            
redTiles = []
for line in raw_lines:
    if line.strip():
        x, y = map(int, line.split(","))
        redTiles.append((x, y))

Hwalls = [] 
Vwalls = []
            
for i in range(0, len(redTiles)):
    t1 = redTiles[i]
    t2 = redTiles[(i+1)%len(redTiles)]
    
    if (t1[0] == t2[0]):
        minY = min(t1[1], t2[1])
        maxY = max(t1[1], t2[1])
        
        Vwalls.append((minY,maxY,t1[0]))
    else :
        minX = min(t1[0], t2[0])
        maxX = max(t1[0], t2[0])
        
        Hwalls.append((minX,maxX,t1[1]))
        
def checkValid(t1,t2):
    minRx = min(t1[0], t2[0])
    minRy = min(t1[1], t2[1])
    maxRx = max(t1[0], t2[0])
    maxRy = max(t1[1], t2[1])
    
    for minY, maxY, wx in Vwalls:
        if minRx < wx < maxRx:
            if not (maxY <= minRy or minY >= maxRy):
                return False
    
    for minX, maxX, wy in Hwalls:
        if minRy < wy < maxRy:
            if not (maxX <= minRx or minX >= maxRx):
                return False
            
    cx = (minRx + maxRx) / 2
    cy = (minRy + maxRy) / 2
    
    cruces = 0
    
    for minY, maxY, wx in Vwalls:
        if wx > cx:
            if minY <= cy <= maxY:
                cruces+=1
    
    return (cruces%2) != 0
                
        
        
maxArea = 0            
for i in range(0, len(redTiles)):
    tile1 = redTiles[i]
    for j in range(i+1, len(redTiles)):
        tile2 = redTiles[j]
        
        side1 = abs(tile1[0]-tile2[0])+1
        side2 = abs(tile1[1]-tile2[1])+1
            
        area = side1*side2
            
        if area <= maxArea:
            continue
            
        if checkValid(tile1, tile2):
            maxArea = area
            
print(maxArea)