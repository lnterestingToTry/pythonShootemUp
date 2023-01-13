import pygame
import random

width = 600
height = 360
fps = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
game_surface = pygame.Surface((width, height))
pygame.display.set_caption("p")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()


window_width = window.get_width()
window_height = window.get_height()

for_scale_coefficient = width / height

def fullscreen_with_ratio():
	game_surface_local = pygame.transform.scale(game_surface, (int(window_height * for_scale_coefficient), window_height))
	new_game_width = game_surface_local.get_width()
	window.blit(game_surface_local, ((window_width / 2) - (new_game_width) / 2, 0))

def draw_text(surf, text, size, x, y, color):
	font_name = pygame.font.match_font('arial')
	font = pygame.font.Font(font_name, size)
	text_surface = font.render(text, True, color)
	text_rect = text_surface.get_rect()
	text_rect.center = (x, y)
	surf.blit(text_surface, text_rect)

class updateble_objects_manager():
	def __init__(self):
		self.objects = []

	def update(self):
		for i in self.objects:
			i.update()

class post_processing_manager():
	def __init__(self):
		self.objects = []

	def update(self):
		for i in self.objects:
			i.update()

def create_lvl_matrix(lvl_x, lvl_y, player_vis_lvl):

	lvl = []

	for i in range(0,lvl_y):
		line = []
		for i in range(0,lvl_x):
			line.append(0)
		lvl.append(line)

	y = 0
	for line in lvl:
		x = 0
		for element in line:
			randnum = random.randint(0, 100)
			if randnum > 80:
				lvl[y][x] = 1
			x += 1

		y += 1

	startpos_y = random.randint(0, lvl_y - 1)
	lvl[startpos_y][0] = "p"
	player_vis_lvl[startpos_y][0] = "p"



	return(lvl)

def build_visual_lvl_matrix(lvl):
	for i in all_sprites:
		i.kill()


	x = 0
	y = 0

	x = game.focus_offset.offset_x
	y = game.focus_offset.offset_y


	for line in lvl:
		for element in line:
			if element == 1:
				img_plate(x, y)

			if element == "p":
				img_player_plate(x, y)

			x += 16
		x = game.focus_offset.offset_x
		y += 16


class img_plate(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((16,16))
		self.image.fill((255,255,255))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		all_sprites.add(self)
	def update(self):
		pass

class img_player_plate(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((16,16))
		self.image.fill((100,100,100))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		all_sprites.add(self)
	def update(self):
		pass

class game():
	def __init__(self):

		self.matrix_x = 100
		self.matrix_y = 43

		self.focus_offset = focus_offset()
		self.game_surface_scale = game_surface_scale()

		self.press_timer = 0

		self.action_lvl_now = False

		self.player_vis_lvl = [] #player_visible_lvl
		for i in range(self.matrix_y):
			line = []
			for i in range(self.matrix_x):
				line.append(0)
			self.player_vis_lvl.append(line)


		self.lvl_matrix = create_lvl_matrix(self.matrix_x,self.matrix_y, self.player_vis_lvl)
		updateble_objects_m.objects.append(self)

	def update(self):
		press = pygame.key.get_pressed()

		if self.press_timer > 0:
			self.press_timer -= 1
		if self.action_lvl_now == False
			if press[pygame.K_d] and self.press_timer <= 0:
				self.press_timer = 20

				y = 0
				done = 0
				for line in self.lvl_matrix:
					x = 0
					for element in line:
						if element == "p":
							if 0 <= x < self.matrix_x - 1:
								if self.lvl_matrix[y][x+1] == 0:
									self.lvl_matrix[y][x] = 0
									self.lvl_matrix[y][x+1] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y][x+1] = "p"

									done = 1

								if self.lvl_matrix[y][x+1] == 1: #triger for event
									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y][x+1] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y][x+1] = "p"

									done = 1					
									print ("event num1 here")	#event

								if type(self.lvl_matrix[y][x+1]) == tuple:
									cel = create_ekshn_self.lvl_matrix(self.lvl_matrix[y][x+1], 10)
									print(cel.enemys)
									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y][x+1] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y][x+1] = "p"

									done = 1
							break
						x += 1

					if done == 1:
						break
					y += 1

				#for i in self.player_vis_lvl:
				#	print(str(i))

			if press[pygame.K_a] and self.press_timer <= 0:
				self.press_timer = 20

				y = 0
				done = 0
				for line in self.lvl_matrix:
					x = 0
					for element in line:
						if element == "p":
							if 0 < x <= self.matrix_x - 1:
								if self.lvl_matrix[y][x-1] == 0:
									self.lvl_matrix[y][x] = 0
									self.lvl_matrix[y][x-1] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y][x-1] = "p"


									done = 1
								if self.lvl_matrix[y][x-1] == 1: #triger for event
									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y][x-1] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y][x-1] = "p"

									done = 1					
									print ("event num1 here")	#event
								if type(self.lvl_matrix[y][x-1]) == tuple:
									cel = create_ekshn_self.lvl_matrix(self.lvl_matrix[y][x-1], 10)
									print(cel.enemys)
									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y][x-1] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y][x-1] = "p"

									done = 1
							break
						x += 1

					if done == 1:
						break
					y += 1

				#for i in self.player_vis_lvl:
				#	print(str(i))

			if  press[pygame.K_w] and self.press_timer <= 0:
				self.press_timer = 20

				y = 0
				done = 0
				for line in self.lvl_matrix:
					x = 0
					for element in line:
						if element == "p":
							if 0 < y <= self.matrix_y - 1:
								if self.lvl_matrix[y-1][x] == 0:
									self.lvl_matrix[y][x] = 0
									self.lvl_matrix[y-1][x] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y-1][x] = "p"

									done = 1

								if self.lvl_matrix[y-1][x] == 1: #triger for event
									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y-1][x] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y-1][x] = "p"

									done = 1					
									print ("event num1 here")	#event
								if type(self.lvl_matrix[y-1][x]) == tuple:
									cel = create_ekshn_self.lvl_matrix(self.lvl_matrix[y-1][x], 10)
									print(cel.enemys)
									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y-1][x] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y-1][x] = "p"

									done = 1
							break
						x += 1

					if done == 1:
						break
					y += 1

				#for i in self.player_vis_lvl:
				#	print(str(i))

			if  press[pygame.K_s] and self.press_timer <= 0:
				self.press_timer = 20

				y = 0
				done = 0
				for line in self.lvl_matrix:
					x = 0
					for element in line:
						if element == "p":
							if 0 <= y < self.matrix_y - 1:
								if self.lvl_matrix[y+1][x] == 0:
									self.lvl_matrix[y][x] = 0
									self.lvl_matrix[y+1][x] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y+1][x] = "p"

									done = 1
								if self.lvl_matrix[y+1][x] == 1: #triger for event
									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y+1][x] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y+1][x] = "p"

									done = 1	
									print ("event num1 here")	#event
								if type(self.lvl_matrix[y+1][x]) == tuple:
									cel = create_ekshn_self.lvl_matrix(self.lvl_matrix[y+1][x], 10)
									print(cel.enemys)
									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y+1][x] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y+1][x] = "p"

									done = 1
							break
						x += 1

					if done == 1:
						break
					y += 1

			y = 0
			for line in self.lvl_matrix:
				x = 0
				for element in line:
					if 0 <= x < self.matrix_x - 1:
						if self.lvl_matrix[y][x+1] == "p":
							self.player_vis_lvl[y][x] = element

					if 0 < x <= self.matrix_x - 1:
						if self.lvl_matrix[y][x-1] == "p":
							self.player_vis_lvl[y][x] = element

					if 0 <= y < self.matrix_y - 1:
						if self.lvl_matrix[y+1][x] == "p":
							self.player_vis_lvl[y][x] = element

					if 0 < y <= self.matrix_y - 1:
						if self.lvl_matrix[y-1][x] == "p":
							self.player_vis_lvl[y][x] = element

					if 0 < x <= self.matrix_x - 1 and 0 <= y < self.matrix_y - 1:
						if self.lvl_matrix[y+1][x-1] == "p":
							self.player_vis_lvl[y][x] = element

					if 0 < x <= self.matrix_x - 1 and 0 < y <= self.matrix_y - 1:
						if self.lvl_matrix[y-1][x-1] == "p":
							self.player_vis_lvl[y][x] = element

					if 0 <= x < self.matrix_x - 1 and 0 <= y < self.matrix_y - 1:
						if self.lvl_matrix[y+1][x+1] == "p":
							self.player_vis_lvl[y][x] = element

					if 0 <= x < self.matrix_x - 1 and 0 < y <= self.matrix_y - 1:
						if self.lvl_matrix[y-1][x+1] == "p":
							self.player_vis_lvl[y][x] = element

					x += 1
				y += 1

			build_visual_lvl_matrix(self.player_vis_lvl)


class focus_offset():
	def __init__(self):
		self.offset_x = 0
		self.offset_y = 0

		self.move_right = False
		self.move_left = False
		self.move_up = False
		self.move_down = False

		updateble_objects_m.objects.append(self)


	def update(self):
		for i in all_sprites:
			if type(i) == img_player_plate:
				if i.rect.centerx > 340:
					self.move_left = True

				if i.rect.centerx < 260:
					self.move_right = True

				if i.rect.centery < 160:
					self.move_down = True

				if i.rect.centery > 200:
					self.move_up = True

		if self.move_right:
			self.offset_x += 3
		if self.move_left:
			self.offset_x -= 3
		if self.move_up:
			self.offset_y -= 3
		if self.move_down:
			self.offset_y += 3

		self.move_right = False
		self.move_left = False
		self.move_up = False
		self.move_down = False


class game_surface_scale():
	def __init__(self):
		self.scale_coefficient = 2
		post_processing_m.objects.append(self)


	def update(self):
		global game_surface
		new_width = int(width * self.scale_coefficient)
		new_height = int(height * self.scale_coefficient)

		game_surface.blit(pygame.transform.scale(game_surface, (new_width, new_height)), (-(int((new_width-width)/2)),-(int((new_height-height)/2))))


class create_action_lvl():
	def __init__(self):
		player = player()

		updateble_objects_m.objects.append(self)

	def update(self):
		pass

class player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((16, 16))
		self.image.fill((255,255,255))
		self.rect = self.image.get_rect()
		self.rect.centerx = width / 2
		self.rect.centery = height - self.rect.height * 2
		all_sprites.add(self)

	def update(self):
		press = pygame.key.get_pressed()
		if press[pygame.K_w]:
			self.rect.y -= 2
		if press[pygame.K_s]:
			self.rect.y += 2
		if press[pygame.K_d]:
			self.rect.x += 2
		if press[pygame.K_a]:
			self.rect.x -= 2


updateble_objects_m = updateble_objects_manager()
post_processing_m = post_processing_manager()
game = game()

running = True
while running:
	clock.tick(fps)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
	
	game_surface = pygame.Surface((width, height))
	updateble_objects_m.update()
	game_surface.fill(BLACK)
	all_sprites.update()
	all_sprites.draw(game_surface)
	post_processing_m.update()

	fullscreen_with_ratio()

	real_fps = int(clock.get_fps())
	draw_text(window, str(real_fps), 20, 60, 20, (255,255,255))
	
	pygame.display.flip()