with open("Input.txt", "r", encoding="utf-8") as f:
    ranges = f.read().split(",")
    
count = 0

for ranged in ranges:
    limits = ranged.split("-")
    pos1 = limits[0]
    pos2 = limits[1]
    for i in range(int(pos1), int(pos2)+1):
        index = str(i)
        j = 1
        while (j<len(index)//2+1):
            pattern = index[0:j]
            rest = index[j:len(index)]
            
            if(rest.replace(pattern, "") == ""): 
                count+=i
                break
            j+=1

print(count)