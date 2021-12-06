
horizontal = 0
depth = 0
aim = 0

with open("day2.input") as f:
    for line in f:
        values = line.split()

        command = values[0]
        value = int(values[1])

        if command == "forward":
            horizontal += value
            depth += value * aim
        if command == "down":
            aim += value
        if command == "up":
            aim -= value

        print("command", command)
        print("value", value)
        print("h", horizontal)
        print("depth", depth)
        print("aim", aim)

position = horizontal * depth

print("horizontal", horizontal)
print("depth", depth)
print("position", position)
