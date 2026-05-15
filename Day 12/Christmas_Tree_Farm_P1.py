with open("Input.txt", "r", encoding="utf-8") as f:
    rawBlock = f.read().strip().split("\n\n") 
    
presentBlocks = rawBlock[0:-1]
regions = rawBlock[-1].strip().splitlines()
presents = []
presentAreas = []

for presentBlock in presentBlocks:
    areaCount = 0
    lines = presentBlock.splitlines()    
    grid = [list(row) for row in lines[1:]]
    for row in lines[1:]:
        areaCount += row.count("#")
    presentAreas.append(areaCount)
    
    presents.append(grid)
       
def gridToCoords(grid):
    coords = []
    
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "#":
                coords.append((r,c))
                
    if not coords : return []
    
    minR, minC = sorted(coords)[0]
    
    normalized = []
    for r, c in coords:
        normalized.append((r - minR, c - minC))
        
    return tuple(normalized)
    
def getAllRotations(grid):
    def rotate_grid(g):
        return [list(row) for row in zip(*g[::-1])]
    
    def flip_grid(g):
        return [row[::-1] for row in g]
    
    variations = set()
    currentGrid = grid
    
    for _ in range(4):
        coords = gridToCoords(currentGrid)
        coordsSorted = tuple(sorted(coords))
        variations.add(coordsSorted)
        
        currentGrid = rotate_grid(currentGrid)
        
    currentGrid = flip_grid(grid)
    for _ in range(4):
        coords = gridToCoords(currentGrid)
        variations.add(tuple(sorted(coords)))
        currentGrid = rotate_grid(currentGrid)
        
    return sorted(list(variations)) 
        
presentsData = []

for i, grid in enumerate(presents):
    area = presentAreas[i]
    
    rotaciones = getAllRotations(grid)
    
    presentsData.append({
        'id': i,
        'area': area,
        'rotations': rotaciones
    })    
    
def solve(board, pool, H, W, leftBoardArea):

    if len(pool) == 0:
        return True

    gapR, gapC = -1, -1
    find = False
    
    for r in range(H):
        for c in range(W):
            if board[r][c] == 0:
                gapR, gapC = r, c
                find = True
                break
        if find: break
            
    if not find:
        return False
        
    area_pool = sum(p[0] for p in pool)
    if area_pool > leftBoardArea:
        return False

    for i in range(len(pool)):
        if i > 0 and pool[i][0] == pool[i-1][0] and pool[i][2] == pool[i-1][2]:
            continue
        
        area, id, rotaciones = pool[i]
        
        for coords in rotaciones:
            fit = True
            coordsToPaint = []
            
            for row, column in coords:
                nr, nc = gapR + row, gapC + column
                if not (0 <= nr < H and 0 <= nc < W) or board[nr][nc] != 0:
                    fit = False
                    break
                coordsToPaint.append((nr, nc))
                
            if fit:
                for pr, pc in coordsToPaint:
                    board[pr][pc] = 1
                    
                newPool = pool[:i] + pool[i+1:]
                
                if solve(board, newPool, H, W, leftBoardArea - area):
                    return True
                
                for pr, pc in coordsToPaint:
                    board[pr][pc] = 0


    if leftBoardArea > area_pool:
        board[gapR][gapC] = -1 

        if solve(board, pool, H, W, leftBoardArea - 1):
            return True
            
        board[gapR][gapC] = 0
                    
    return False
            
    
count = 0
for regionStr in regions:
    region = regionStr.split()
    quantity = list(map(int, region[1:]))
    
    size = region[0].replace(":","").split("x")
    W = int(size[0])
    H = int(size[1])
    area = W*H
    targetArea = 0
    for i in range(len(quantity)):
        targetArea += quantity[i]*presentAreas[i]
        
    if targetArea > area: continue
    
    piecesPool = []
    for i in range(len(quantity)):
        cant = quantity[i]
        if cant > 0:
            data = presentsData[i]
            
            for _ in range(cant):
                piecesPool.append((data['area'], data['id'], data['rotations']))
                    
    piecesPool.sort(key=lambda x: x[0], reverse=True)
    
    board = [[0] * W for _ in range(H)]
    
    if solve(board, piecesPool, H, W, area):
        count += 1
        
print(count)