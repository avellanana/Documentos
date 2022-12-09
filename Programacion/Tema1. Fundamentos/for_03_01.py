for i in range(10):
    print(f'{i+1}\t', end='')

print()

for i in range(10):
    print(f'{2*(i+1)}\t', end='')

print()

offset = 0
for i in range(10):
    print(f'{20+offset}\t', end='')
    offset += 3

print()

offset = 0
for i in range(6):
    print(f'{10+offset}\t', end='')
    offset += 4

print()

offset = 0
for i in range(9):
    print(f'{40+offset}\t', end='')
    offset -= 5

print()