def median(data):
    N = len(sorted(data))
    if not N:
        return None
    elif N%2==1:
        return data[N//2]
    else:
        a = data[N//2-1]
        b = data[N//2]
        return (a+b)/2



l1 = [8, 8, 8] # 8,
l2 = [14, 18, 22, 30] # 20.0
l3 = [6, 6, 6, 24, 24, 24] #15.0
l4 = [] #None

print(median(l1))
print(median(l2))
print(median(l3))
print(median(l4))
