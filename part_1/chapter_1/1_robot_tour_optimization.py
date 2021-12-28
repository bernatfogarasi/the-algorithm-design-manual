import random
import math
import itertools

DIMENTION_COUNT = 2
POINT_COORDINATE_MAX = 10
POINT_COORDINATE_MIN = -10
POINT_COUNT = 5

def create_coordinate():
	return random.randint(POINT_COORDINATE_MIN, POINT_COORDINATE_MAX)

def create_point():
	return [create_coordinate() for _ in range(DIMENTION_COUNT)]

def create_points():
	return [create_point() for _ in range(POINT_COUNT)]

def calculate_distance(point_a, point_b):
	return math.sqrt(sum((point_a_coordinate - point_b_coordinate) ** 2 
		for point_a_coordinate, point_b_coordinate in zip(point_a, point_b)))

def find_nearest_point(point_start, points):
	point_nearest_index, distance_min = None, None
	for j, point in enumerate(points):
		distance = calculate_distance(point_start, point)
		if distance_min is None or distance < distance_min:
			point_nearest_index, distance_min = j, distance
	return point_nearest_index, distance_min

def solve_nearest_first(points_original): # not accurate
	points = [*points_original]
	path = [points[0]]
	distances = []
	del points[0]
	while len(points):
		point_nearest_index, distance_min = find_nearest_point(path[-1], points)
		distances.append(distance_min)
		path.append(points[point_nearest_index])
		del points[point_nearest_index]
	return path, distances, sum(distances)

def solve_exhaustive(points): # bad time complexity
	distance_sum_min = None
	for permutation_index, permutation in enumerate(itertools.permutations(points)):
		distances_current = [calculate_distance(permutation[i], permutation[i + 1]) for i in range(len(permutation) - 1)]
		distance_sum = sum(distances_current)
		if distance_sum_min is None or distance_sum < distance_sum_min:
			distance_sum_min = distance_sum
			path = list(permutation)
			distances = distances_current
	return path, distances, distance_sum_min

def main():
	points = create_points()
	print(points)
	print(solve_nearest_first(points))
	print(solve_exhaustive(points))
	# print("solve_nearest_first:", solve_nearest_first(points))
	# print("solve_exhaustive:", solve_exhaustive(points))

if __name__ == '__main__':
	main()