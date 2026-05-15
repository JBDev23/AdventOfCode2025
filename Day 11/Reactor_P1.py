with open("Input.txt", "r", encoding="utf-8") as f:
    datas = f.read().splitlines() 
    
devices = {}
for data in datas:
    clean = data.split()
    devices[clean[0].replace(":", "")] = clean[1:]
    
start = "you"
paths = []

def search(actual, dest, path):
    if actual == dest:
        paths.append(path)
        return
    
    
    toExplore = devices.get(actual, [])
    
    for p in toExplore:
        if p not in path:
            search(p, dest, path+[p])
 
           
search("you", "out", ["you"])

print(len(paths))         
