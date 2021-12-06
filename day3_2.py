key = 0
matches = []
oxygen_value = None
co2_value = None

text_file = open("day3.input", "r")
lines = text_file.read().splitlines()

# # Transpose the lines
results = [list(i) for i in zip(*lines)]

oxy_remaining = lines
co2_remaining = lines

while key <= len(results):

    # Oxygen
    if len(oxy_remaining) > 1:
        # Transpose the lines
        results = [list(i) for i in zip(*oxy_remaining)]
        result = [int(i) for i in results[key]]
        total = sum(result)
        length = len(result)

        if (total/length) >= 0.5:
            oxy_bit = 1
        else:
            oxy_bit = 0

        oxy_matches = []
        for item in oxy_remaining:
            if item[key] == str(oxy_bit):
                oxy_matches.append(item)

        oxy_matches_count = len(oxy_matches)
        print("pos:", key, "oxy_bit:", oxy_bit, "oxy_matches_count:", oxy_matches_count)
        oxy_remaining = oxy_matches
    elif not oxygen_value:
        oxygen_value = oxy_matches[0]

    # co2
    if len(co2_remaining) > 1:
        results = [list(i) for i in zip(*co2_remaining)]
        result = [int(i) for i in results[key]]
        total = sum(result)
        length = len(result)

        if (total/length) >= 0.5:
            co2_bit = 0
        else:
            co2_bit = 1

        co2_matches = []
        for item in co2_remaining:
            if item[key] == str(co2_bit):
                co2_matches.append(item)

        co2_matches_count = len(co2_matches)
        print("pos:", key, "co2_bit:", co2_bit, "co2_matches_count:", co2_matches_count)
        co2_remaining = co2_matches
    elif not co2_value:
        co2_value = co2_matches[0]

    key += 1

print(oxygen_value)
print(co2_value)
print("oxygen:",int(oxygen_value,2))
print("co2:",int(co2_value,2))
print(int(oxygen_value,2) * int(co2_value,2))
