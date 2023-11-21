def median(data):
    N = len(sorted(data))
    if N%2==1:
        return data[N//2]
    else:
        return "even"


my_list = [15,1,2,3,4,14,5,6,7,8,9,10,11,12,13]

print(median(my_list))
