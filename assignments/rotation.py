def rotate(list_to_rotate, number_to_rotate_with):
    number_to_rotate_with = number_to_rotate_with % len(list_to_rotate)
    return list_to_rotate[number_to_rotate_with:] + list_to_rotate[:number_to_rotate_with]


result = rotate([2, 3, 5, 6], 2)
print(result)


def rotate2(list_to_rotate: list[int], rotate_by: int) -> list[int]:
    rotate_by = rotate_by % len(list_to_rotate)
    return list_to_rotate[rotate_by:] + list_to_rotate[:rotate_by]


result = rotate([2, 3, 5, 6], 2)
print(result)
