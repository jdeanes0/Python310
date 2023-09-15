import stack

stackyboi = stack.Stack(15)

stackyboi.pushList([1, 2, 3, 4, 5, 6])

print(stackyboi)

print(stackyboi.pop())
print(stackyboi.pop())
print(stackyboi.pop())
print(stackyboi.pop())
print(stackyboi.pop())
print(stackyboi.pop())

print(f"Count: {stackyboi.count()}")

stackyboi.push(3)
stackyboi.push(4)
stackyboi.push(5)
stackyboi.push(88)
stackyboi.push(0)
stackyboi.push(444)

print(stackyboi)
print(f"Count: {stackyboi.count()}")
print(f"Top: {stackyboi.peek()}")

