negative_coordinates = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]
# negative_coordinates = [(-2, 3), (4, -5), (-1, -1), (0, 0), (-3, 2)]


def convert_positive(negative_coordinates):
    min_x = abs(min(negative_coordinates, key=lambda x: x[0])[0])
    min_y = abs(min(negative_coordinates, key=lambda x: x[1])[1])
    positive_coordinate = [(c[0] + min_x, c[1] + min_y) for c in negative_coordinates]
    return positive_coordinate


print(convert_positive(negative_coordinates))
