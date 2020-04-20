import random

width = 640
height = 640

cols = width // 40
rows = height // 40


def food(rows, item):
	positions = item.body

	while True:
		x = random.randrange(1, rows - 1)
		y = random.randrange(1, rows - 1)
		if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
			continue
		else:
			break

	return (x, y)
