ttl = 0

def check_pal(val):
    if list(reversed(val)) == list(val):
        return True
    else:
        return False

for i in range(1,1000000):
    val_10 = i
    val_2 = bin(val_10)[2:]

    if check_pal(str(val_10)) and check_pal(val_2):
        ttl += i
        
print(ttl)

# Answer: 872187