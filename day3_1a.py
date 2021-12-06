key = 0
gamma = ''
epsilon = ''

text_file = open("day3.input", "r")
lines = text_file.read().splitlines()

# Transpose the lines
results = [list(i) for i in zip(*lines)]

while key < len(results):
    result = [int(i) for i in results[key]]
    total = sum(result)
    length = len(result)

    if (total/length) >= 0.5:
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    else:
        gamma = gamma + '0'
        epsilon = epsilon + '1'
    key += 1

gamma_int = int(gamma, 2)
epsilon_int = int(epsilon, 2)

print("gamma binary:", gamma)
print("gamma:", gamma_int)
print("epsilon binary:", epsilon)
print("epsilon:", epsilon_int)
print("power consumption:", gamma_int * epsilon_int)
