
print("SCRAPPY")
my_string = "aaAAa vVVvv bBBbb sSSsss lLll"
book = "books/frankenstein.txt"

counter = {}
for letter in my_string.lower():
    if letter in counter:
        counter[letter] += 1
    else:
        counter[letter] = 1
    
for k,v in counter.items():
    print(f"{k} -- {v}")


print("#### --END-- ###")

