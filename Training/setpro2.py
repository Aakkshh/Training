def find(s):
    subsets = [set()]
    for element in s:
        subsets += [item | {element} for item in subsets]
    return subsets

input_set = {1, 2, 3}
output = find(input_set)
print(output)