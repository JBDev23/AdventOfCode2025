import itertools
from functools import cache

with open("Input.txt", "r", encoding="utf-8") as f:
    datas = f.read().splitlines() 
    
devices = {}
for data in datas:
    clean = data.split()
    devices[clean[0].replace(":", "")] = clean[1:]
    
start = "you"
paths = []

@cache
def search(actual, dest):
    if actual == dest:
        return 1
    
    total = 0
    toExplore = devices.get(actual, [])
    
    for p in toExplore:
        total += search(p, dest)
        
    return total

startNode = "svr"
endNode = "out"
mustVisit = ["fft", "dac"]

permutaciones = list(itertools.permutations(mustVisit))

grandTotal = 0

for order in permutaciones:
    info = [startNode] + list(order) + [endNode]
    
    permutationPath = 1
    possible = True
        
    for i in range(len(info) - 1):
        origin = info[i]
        dest = info[i+1]
        
        search.cache_clear()
        
        paths = search(origin, dest)
                
        if paths == 0:
            possible = False
            break
        
        permutationPath *= paths
    
    if possible:
        grandTotal += permutationPath

print(grandTotal)  
