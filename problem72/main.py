d = {}
mx = 1_000_001

for i in range(2,mx):
  d[i] = i-1

for i in range(2,mx):
  for j in range(2,mx):
    if i*j < mx:
      d[i*j] -= d[i]
    else:
      break

print(sum(d.values()))

# Answer: 303963552391