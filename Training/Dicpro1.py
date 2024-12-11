def invert_dict(d):
    return {v: k for k, v in d.items()}

input_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = invert_dict(input_dict)
print(inverted_dict)