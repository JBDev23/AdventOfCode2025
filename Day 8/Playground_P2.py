with open("Input.txt", "r", encoding="utf-8") as f:
    junctions = f.read().splitlines() 
    
mindist = float("inf")
points = []
 
puntos = [list(map(int, j.split(","))) for j in junctions]

connections = []

puntos.sort(key=lambda p: p[0]) 
 
for i in range(0, len(puntos)):
    for j in range(i+1, len(puntos)):
        dist = (puntos[i][0]-puntos[j][0])**2 + (puntos[i][1]-puntos[j][1])**2 + (puntos[i][2]-puntos[j][2])**2
        connections.append((dist, i, j))
        
connections.sort()
        
parent = list(range(len(puntos)))

num_sets = len(puntos)

def find(i):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i])
    return parent[i]

def union(i, j):
    root_i = find(i)
    root_j = find(j)
        
    if root_i != root_j:
        parent[root_j] = root_i
        return True
    return False


for _, pos1, pos2 in connections:
    if union(pos1,pos2) : num_sets -=1
    
    if num_sets == 1:
        pont1 = puntos[pos1]
        point2 = puntos[pos2]
        print(pont1[0]*point2[0])
        break
        
