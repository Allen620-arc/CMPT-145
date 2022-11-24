import Stack

s = Stack.Stack()
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for v in values:
    s.push(v)

n = 0
for i in range(4):
    n = n +s.pop()

print(n)