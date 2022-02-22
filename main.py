data = [60,61,65,63,98,99,90,95,91,96]

def standardDeviation(x):
    total = 0
    mean = 0
    stdDev = 0
    mdif = []
    total2 = 0
    for a in x:
        total += a

    mean = total/len(x)
    
    for a in x:
        mdif.append((a-mean)**2) 

    for a in mdif: 
        total2 += a

    stdDev = total2/len(mdif)

    return (stdDev)**0.5

print(standardDeviation(data))

    