import Queue as Q

data = Q.Queue()

for v in range(1, 6):
    data.enqueue(v)

while not data.is_empty():
    d = data.dequeue()
    print(d)