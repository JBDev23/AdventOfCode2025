with open("Input.txt", "r", encoding="utf-8") as f:
    machines = f.read().splitlines() 
 
total = 0   

for machine in machines:
    params = machine.split()
    indicators = list(params[0])[1:-1]
    buttons = params[1:-1]
    numLights = len(indicators)
    
    targetM = [0] * numLights
    for i in range(numLights):
        if indicators[i] == "#" : targetM[i] = 1
    
    buttonsM = []
    
    for i in range(len(buttons)):
        clean = buttons[i].replace("(", "").replace(")", "").split(",")
        buttonM = [0] * numLights
        for j in range(len(clean)):
            pos = int(clean[j])
            buttonM[pos] = 1
        
        buttonsM.append(buttonM)
        
    numButtons = len(buttonsM) 
    
    minPresses = float('inf')
    found = False
    
    for i in range((2**numButtons)):
        currentState = [0] * numLights
        pressCount = 0
        
        for j in range(numButtons):
            if (i >> j) & 1:
                pressCount += 1

                for k in range(numLights):
                    currentState[k] ^= buttonsM[j][k]
                    
        if currentState == targetM:
            found = True
            if pressCount < minPresses:
                minPresses = pressCount
                
    if found : total += minPresses
    
print(total)