
prev_line = None
increased = 0
decreased = 0
no_change = 0

with open("day1.input") as f:
    for line in f:
        line_int = int(line)
        line = line.strip()
        if prev_line:
            if prev_line > line_int:
                decreased += 1
                print(line, "(decreased)")
            elif prev_line < line_int:
                increased += 1
                print(line, "(increased)", str(increased))
            elif prev_line == line_int:
                no_change += 1
                print(line, "(no change)")
        else:
            print(line + " (N/A)")
        prev_line = line_int

print("decreased = " + str(decreased))
print("increased = " + str(increased))
print("no_change = " + str(no_change))
