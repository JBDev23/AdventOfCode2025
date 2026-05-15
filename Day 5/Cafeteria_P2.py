with open("Input.txt", "r", encoding="utf-8") as f:
    content = f.read().split("\n\n")
    

count = 0
ranges = content[0].splitlines()
ingredients = content[1].splitlines()
intervals = []

for r in ranges:
    start, end = map(int, r.split("-"))
    intervals.append((start, end))
    
intervals.sort(key=lambda pair:pair[0])
    
mergedIntervals = [intervals[0]] 

for currentstart, currentend in intervals[1:]:
    lastStart, lastEnd = mergedIntervals[-1]
    
    if(currentstart <= lastEnd + 1):
        mergedIntervals[-1] = (lastStart, max(lastEnd, currentend))
    else:
        mergedIntervals.append((currentstart, currentend))
    
for start, end in mergedIntervals:
    count+=end-start+1

print(count)