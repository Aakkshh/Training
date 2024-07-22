def merge(tuple1, tuple2):
    merged_tuple = tuple(sorted(tuple1 + tuple2))
    return merged_tuple

tuple1 = (1, 3, 5)
tuple2 = (2, 4, 6)
print(merge(tuple1, tuple2)) 