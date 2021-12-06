
horizontal = 0
depth = 0

# Stuff file contents into an array
with open("day2.input") as f:
    for line in f:
        values = line.split()

        command = values[0]
        value = values[1]

        if command == "forward":
            horizontal += int(value)
        if command == "down":
            depth += int(value)
        if command == "up":
            depth -= int(value)

position = horizontal * depth

print("horizontal", horizontal)
print("depth", depth)
print("position", position)
