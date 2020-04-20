from classes import *
from setup import *
pygame.font.init()


def main():
	global snake, snack, win
	win = pygame.display.set_mode((width, height))
	pygame.display.set_caption("SNAKE")

	snake = snake((255, 0, 0), (10, 10))
	snake.addcell()

	snack = cell(food(rows, snake), color=(255, 255, 255))
	flag = True
	clock = pygame.time.Clock()

	while flag:
		pygame.time.delay(50)
		clock.tick(10)
		snake.move()
		snake_head = snake.head.pos
		if snake_head[0] > 31 or snake_head[0] < 0 or snake_head[1] > 31 or snake_head[1] < 0:
			print("Score:", len(snake.body))
			snake.reset((10, 10))

		if snake.body[0].pos == snack.pos:
			snake.addcell()
			snack = cell(food(rows, snake), color=(255, 255, 255))

		for x in range(len(snake.body)):
			if snake.body[x].pos in list(map(lambda z: z.pos, snake.body[x + 1:])):
				print("Score:", len(snake.body))
				snake.reset((10, 10))
				break

		redrawWindow()


def redrawWindow():
	global win
	win.fill((37, 37, 37))
	snake.draw(win)
	snack.draw(win)
	text_font = pygame.font.SysFont("poppins", 40)
	l = len(snake.body)
	text = text_font.render("SCORE: " + str(l), 1, (0, 255, 0))
	win.blit(text, (20, 560))
	pygame.display.update()
	pass
