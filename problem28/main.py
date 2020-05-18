dim = 1001
hdiag = int((dim-1)/2)
total = 1
for i in range(1,hdiag+1):
    initval = (((i*2+1)-2)**2) + i*2
    total = total + initval*4 + 6*(i*2)

print(total)

# Answer: 669171001