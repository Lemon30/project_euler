def get_set(val):
    val_str = str(val)
    val_set = list(val_str)
    return set(val_set)

for i in range(1,1_000_000):
    if get_set(i*2) == get_set(i*3) == get_set(i*4) == get_set(i*5) == get_set(i*6):
        print(i)
        break

# Answer: 142857