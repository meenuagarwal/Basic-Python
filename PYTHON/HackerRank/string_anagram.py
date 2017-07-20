def number_needed(a, b):
    map_a = buildmap(a)
    map_b = buildmap(b)
    count = 0
    for key in map_a.keys():
        if key not in map_b.keys():
            count += map_a[key]
        else:
            count += max(0,map_a[key] - map_b[key])
    for key in map_b.keys():
        if key not in map_a.keys():
            count += map_b[key]
        else:
            count += max(0,map_b[key] - map_a[key])    
    return count
    
    
    
def buildmap(s):
    mapdict = {}
    for ch in s:
        if ch not in mapdict:
            mapdict[ch] = 1
        else:
            mapdict[ch] += 1
    return mapdict
            
a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
