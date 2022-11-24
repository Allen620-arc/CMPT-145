import node as N

x = N.node(5, None)
y = N.node(1, x)
z = N.node(8, y)

print(z.get_next().get_data())