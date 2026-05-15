with open("Input.txt", "r", encoding="utf-8") as f:
    redTiles = f.read().splitlines() 
    
    
maxArea = 0
    
for i in range(0, len(redTiles)):
    tile1 = redTiles[i].split(",")
    for j in range(i+1, len(redTiles)):
        tile2 = redTiles[j].split(",")
        side1 = abs(int(tile1[0])-int(tile2[0]))+1
        
        side2 = abs(int(tile1[1])-int(tile2[1]))+1
        area = side1*side2
        
        if area > maxArea : maxArea = area
        
print(maxArea)
        
        