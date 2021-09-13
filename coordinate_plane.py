def coordinate_calc(first_coordinate, second_coordinate, x_val):
	x1, x2 = first_coordinate[0], second_coordinate[0]
	y1, y2 = first_coordinate[1], second_coordinate[1]
	slope = (y2 - y1) / (x2 - x1)
	y_val = slope*(x_val - x1) + y1
	return y_val
