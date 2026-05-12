def wavesorting(arr):
    s = len(arr)
    frequence = {}
    for i in arr:
        if  not i in  frequence:
            frequence[i] = 0
        frequence[i] += 1
    m = max(frequence.values())
    return "true" if m < (s/2) else "false" 

print(wavesorting([2,0,4,1,1,4]))
print(wavesorting([2,4,4,1,1,4]))