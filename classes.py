import pygame


class cell():
	w = 640
	rows = w // 20

	def __init__(self, start, direction_x=1, direction_y=0, color=(255, 0, 100)):
		self.pos = start
		self.direction_x = direction_x
		self.direction_y = direction_y
		self.color = color

	def move(self, direction_x, direction_y):
		self.direction_x = direction_x
		self.direction_y = direction_y
		self.pos = (self.pos[0] + self.direction_x, self.pos[1] + self.direction_y)

	def draw(self, surface, eyes=False):
		dis = self.w // self.rows
		i = self.pos[0]
		j = self.pos[1]

		pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
		if eyes:
			centre = dis // 2
			radius = 3
			circleMiddle = (i * dis + centre - radius, j * dis + 8)
			circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
			pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
			pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)


class snake():
	body = []
	turns = {}

	def __init__(self, color, pos):
		self.color = color
		self.head = cell(pos)
		self.body.append(self.head)
		self.direction_x = 0
		self.direction_y = 1

	def move(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			keys = pygame.key.get_pressed()
			for key in keys:
				if keys[pygame.K_LEFT]:
					self.direction_x = -1
					self.direction_y = 0
					self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]
				elif keys[pygame.K_RIGHT]:
					self.direction_x = 1
					self.direction_y = 0
					self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]
				elif keys[pygame.K_UP]:
					self.direction_y = -1
					self.direction_x = 0
					self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]
				elif keys[pygame.K_DOWN]:
					self.direction_y = 1
					self.direction_x = 0
					self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]

		for i, c in enumerate(self.body):
			p = c.pos[:]
			if p in self.turns:
				turn = self.turns[p]
				c.move(turn[0], turn[1])
				if i == len(self.body)-1:
					self.turns.pop(p)
			else:
				c.move(c.direction_x, c.direction_y)

	def reset(self, pos):
		self.head = cell(pos)
		self.body = []
		self.body.append(self.head)
		self.turns = {}
		self.direction_x = 0
		self.direction_y = 1

	def addcell(self):
		tail = self.body[-1]
		dx, dy = tail.direction_x, tail.direction_y

		if dx == 1 and dy == 0:
			self.body.append(cell((tail.pos[0]-1, tail.pos[1])))
		elif dx == -1 and dy == 0:
			self.body.append(cell((tail.pos[0]+1, tail.pos[1])))
		elif dx == 0 and dy == 1:
			self.body.append(cell((tail.pos[0], tail.pos[1]-1)))
		elif dx == 0 and dy == -1:
			self.body.append(cell((tail.pos[0], tail.pos[1]+1)))

		self.body[-1].direction_x = dx
		self.body[-1].direction_y = dy

	def draw(self, surface):
		for i, c in enumerate(self. body):
			if i == 0:
				c.draw(surface, True)
			else:
				c.draw(surface)