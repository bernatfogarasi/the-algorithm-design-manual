import random

DAY_COUNT = 10
MOVIE_COUNT = 4

def create_movie():
	return sorted([random.randint(0, DAY_COUNT - 1), random.randint(0, DAY_COUNT - 1)])

def create_movies():
	return [create_movie() for _ in range(MOVIE_COUNT)]

def visualize_movie(movie):
	print("", "-" * movie[0] + "#" * (movie[1] - movie[0] + 1) + "-" * (DAY_COUNT - movie[1] - 1))

def visualize_movies(movies):
	for movie_index, movie in enumerate(movies):
		print(movie_index, end="")
		visualize_movie(movie)
	print()

def solve_accept_earliest_start(movies):
	day_index = 0
	movies = sorted(movies)
	movies_accepted = []
	for movie in movies:
		if day_index <= movie[0]:
			movies_accepted.append(movie)
			day_index = movie[1] + 1
	return movies_accepted

def solve_exhaustive(movies):

	return
		
def main():
	movies = create_movies()
	print(movies, end="\n\n")
	print("  " + "".join([str(i) for i in range(DAY_COUNT)]))
	visualize_movies(movies)
	solution_accept_first = solve_accept_earliest_start(movies)
	visualize_movies(solution_accept_first)

if __name__ == '__main__':
	main()