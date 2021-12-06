
depths = []
key = 0
increased = 0
decreased = 0
no_change = 0

# Stuff file contents into an array
with open("day1.input") as f:
    for line in f:
        depths.append(int(line))

# print(len(depths))

# Iterate over array
while key <= len(depths):

    # Try to get current windows
    try:
        window1 = int(depths[key]) + int(depths[key+1]) + int(depths[key+2])
    except IndexError:
        print("Reached end window1. Position:", key)
        break

    try:
        window2 = int(depths[key+1]) + int(depths[key+2]) + int(depths[key+3])
    except IndexError:
        print("Reached end window2. Position:", key)
        break

    # Compare windows
    if window1 > window2:
        decreased += 1
        output = "(decreased)"
    elif window1 < window2:
        increased += 1
        output = "(increased)"
    elif window1 == window2:
        no_change += 1
        output = "(no change)"
    else:
        output = "WIERD!"

    print(str(window1), str(window2), output)

    key += 1

print("decreased = " + str(decreased))
print("increased = " + str(increased))
print("no_change = " + str(no_change))
