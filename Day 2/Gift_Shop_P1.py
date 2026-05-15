with open("Input.txt", "r", encoding="utf-8") as f:
    ranges = f.read().split(",")
    
count = 0

for ranged in ranges:
    limits = ranged.split("-")
    start = limits[0]
    end = limits[1]
    for i in range(int(start), int(end)+1):
        index = str(i)
        mid = len(index)//2
        
        firsthalf = index[0:mid]
        secondhalf = index[mid:]
        if(firsthalf==secondhalf):
            count+=int(index)
            
print(count)