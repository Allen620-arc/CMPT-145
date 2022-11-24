import Stack as S

data = S.Stack()

for v in range(1, 6):
    data.push(v)

while not data.is_empty():
    d = data.pop()
    print(d)