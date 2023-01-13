import pygame
import random
from os import path
from os import listdir

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

def revers_list(lvl_matrix):
	list_ = []
	for i in lvl_matrix:
		list_.insert(0, i)

	return list_

this_directory = path.join(path.dirname(__file__))

class game_graphics():
	def __init__(self):
		self.player = pygame.image.load(path.join(this_directory, "g\\player\\ship\\ship1_for_matrix.png")).convert_alpha()
		self.player_al = pygame.image.load(path.join(this_directory, "g\\player\\ship\\ship1.png")).convert_alpha()

		self.gun1mod1 = pygame.image.load(path.join(this_directory, "g\\player\\guns\\gun1\\mod1\\gun1mod1.png")).convert_alpha()
		self.gun1mod2 = pygame.image.load(path.join(this_directory, "g\\player\\guns\\gun1\\mod2\\gun1mod2.png")).convert_alpha()
		self.gun1mod3 = pygame.image.load(path.join(this_directory, "g\\player\\guns\\gun1\\mod3\\gun1mod3.png")).convert_alpha()

		self.gun2mod1 = pygame.image.load(path.join(this_directory, "g\\player\\guns\\gun2\\mod1\\gun2mod1.png")).convert_alpha()
		self.gun2mod2 = pygame.image.load(path.join(this_directory, "g\\player\\guns\\gun2\\mod2\\gun2mod2.png")).convert_alpha()
		self.gun2mod3 = pygame.image.load(path.join(this_directory, "g\\player\\guns\\gun2\\mod3\\gun2mod3.png")).convert_alpha()

		self.gun3mod1 = pygame.image.load(path.join(this_directory, "g\\player\\guns\\gun3\\mod1\\gun3mod1.png")).convert_alpha()
		self.gun3mod2 = pygame.image.load(path.join(this_directory, "g\\player\\guns\\gun3\\mod2\\gun3mod2.png")).convert_alpha()
		self.gun3mod3 = pygame.image.load(path.join(this_directory, "g\\player\\guns\\gun3\\mod3\\gun3mod3.png")).convert_alpha()
		self.gun3mod4 = pygame.image.load(path.join(this_directory, "g\\player\\guns\\gun3\\mod4\\gun3mod4.png")).convert_alpha()

		self.gun4mod1 = pygame.image.load(path.join(this_directory, "g\\player\\guns\\gun4\\mod1\\gun4mod1.png")).convert_alpha()
		self.gun4mod2 = pygame.image.load(path.join(this_directory, "g\\player\\guns\\gun4\\mod2\\gun4mod2.png")).convert_alpha()
		self.gun4mod3 = pygame.image.load(path.join(this_directory, "g\\player\\guns\\gun4\\mod3\\gun4mod3.png")).convert_alpha()

		self.matrix_plate9_1 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant1\\fog1.png")).convert_alpha()
		self.matrix_plate9_1_anim = []
		for i in listdir(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant1\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant1\\anim\\{}".format(i))).convert_alpha()
			self.matrix_plate9_1_anim.append(img)
			print(i)

		self.matrix_plate9_2 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant2\\fog2.png")).convert_alpha()
		self.matrix_plate9_2_anim = []
		for i in listdir(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant2\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant2\\anim\\{}".format(i))).convert_alpha()
			self.matrix_plate9_2_anim.append(img)
			print(i)

		self.matrix_plate9_3 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant3\\fog3.png")).convert_alpha()
		self.matrix_plate9_3_anim = []
		for i in listdir(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant3\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant3\\anim\\{}".format(i))).convert_alpha()
			self.matrix_plate9_3_anim.append(img)
			print(i)


		self.matrix_plate9_4 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant4\\fog4.png")).convert_alpha()
		self.matrix_plate9_4_anim = []
		for i in listdir(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant4\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant4\\anim\\{}".format(i))).convert_alpha()
			self.matrix_plate9_4_anim.append(img)
			#print(i)

		self.matrix_plate_9_border_up1 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\border_fog\\b_fog_up1.png")).convert_alpha()
		self.matrix_plate_9_border_down1 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\border_fog\\b_fog_down1.png")).convert_alpha()
		self.matrix_plate_9_border_left1 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\border_fog\\b_fog_left1.png")).convert_alpha()
		self.matrix_plate_9_border_right1 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\border_fog\\b_fog_right1.png")).convert_alpha()

		self.test_enemy = pygame.image.load(path.join(this_directory, "g\\enemys\\test_enemy\\ship.png")).convert_alpha()

		self.planet1 = pygame.image.load(path.join(this_directory, "g\\background\\planets\\planet1.png")).convert_alpha()
		self.planet2 = pygame.image.load(path.join(this_directory, "g\\background\\planets\\planet2.png")).convert_alpha()
		self.planet3 = pygame.image.load(path.join(this_directory, "g\\background\\planets\\planet3.png")).convert_alpha()

		self.star1 = pygame.image.load(path.join(this_directory, "g\\background\\stars\\star1.png")).convert_alpha()
		self.star2 = pygame.image.load(path.join(this_directory, "g\\background\\stars\\star2.png")).convert_alpha()
		self.star3 = pygame.image.load(path.join(this_directory, "g\\background\\stars\\star3.png")).convert_alpha()

		self.enemy_1 = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_1\\enemy_1.png")).convert_alpha()
		self.enemy_1_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_1\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_1\\shoot_anim\\{}".format(i))).convert_alpha()
			self.enemy_1_shoot_anim.append(img)

		self.enemy_2 = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_2\\enemy_2.png")).convert_alpha()
		self.enemy_2_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_2\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_2\\shoot_anim\\{}".format(i))).convert_alpha()
			self.enemy_2_shoot_anim.append(img)

		self.enemy_3 = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_3\\enemy_3.png")).convert_alpha()
		self.enemy_3_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_3\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_3\\shoot_anim\\{}".format(i))).convert_alpha()
			self.enemy_3_shoot_anim.append(img)
		self.enemy_3_mine = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_3\\mine\\mine.png")).convert_alpha()
		self.enemy_3_mine_light_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_3\\mine\\light_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_3\\mine\\light_anim\\{}".format(i))).convert_alpha()
			self.enemy_3_mine_light_anim.append(img)

		self.enemy_4 = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_4\\enemy_4.png")).convert_alpha()
		self.enemy_4_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_4\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_4\\shoot_anim\\{}".format(i))).convert_alpha()
			self.enemy_4_shoot_anim.append(img)

		self.enemy_4_rocket = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_4\\rocket\\rocket.png"))
		self.enemy_4_rocket_init_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_4\\rocket\\init_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_4\\rocket\\init_anim\\{}".format(i)))
			self.enemy_4_rocket_init_anim.append(img)
		self.enemy_4_rocket_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_4\\rocket\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_4\\rocket\\shoot_anim\\{}".format(i)))
			self.enemy_4_rocket_shoot_anim.append(img)

		self.enemy_5 = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_5\\enemy_5.png")).convert_alpha()
		self.enemy_5_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_5\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_5\\shoot_anim\\{}".format(i))).convert_alpha()
			self.enemy_5_shoot_anim.append(img)

		self.enemy_6 = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_6\\enemy_6.png")).convert_alpha()
		self.enemy_6_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_6\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_6\\shoot_anim\\{}".format(i))).convert_alpha()
			self.enemy_6_shoot_anim.append(img)

		self.enemy_7 = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_7\\enemy_7.png")).convert_alpha()
		self.enemy_7_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_7\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_7\\shoot_anim\\{}".format(i))).convert_alpha()
			self.enemy_7_shoot_anim.append(img)
		self.enemy_7_reload_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_7\\reload_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_7\\reload_anim\\{}".format(i))).convert_alpha()
			self.enemy_7_reload_anim.append(img)

		self.enemy_8 = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_8\\enemy_8.png")).convert_alpha()
		self.enemy_8_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_8\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_8\\shoot_anim\\{}".format(i))).convert_alpha()
			self.enemy_8_shoot_anim.append(img)

		self.enemy_9 = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_9\\enemy_9.png")).convert_alpha()
		self.enemy_9_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_9\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_9\\shoot_anim\\{}".format(i))).convert_alpha()
			self.enemy_9_shoot_anim.append(img)
		self.enemy_9_shield = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_9\\shield\\shield.png"))
		self.enemy_9_shield_init_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_9\\shield\\init_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_9\\shield\\init_anim\\{}".format(i))).convert_alpha()
			self.enemy_9_shield_init_anim.append(img)
		self.enemy_9_shield_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_9\\shield\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_9\\shield\\anim\\{}".format(i))).convert_alpha()
			self.enemy_9_shield_anim.append(img)
		self.enemy_9_shield_kill_anim = revers_list(self.enemy_9_shield_init_anim)

		self.hp = pygame.Surface((20,20))
		self.hp.fill((255,0,0))

gg = game_graphics()

def absolute_number(num): #модуль числа
	if num < 0:
		num = num * (-1)
		return(num)
	else:
		return num

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
				lvl[y][x] = (9, 9)#random.choice([(0, 0), (random.randint(0, 2), random.randint(0, 2) )])
			if randnum < 5:
				lvl[y][x] = random.randint(1, 3)
			x += 1
		print(line)
		y += 1
	

	startpos_y = random.randint(0, lvl_y - 1)
	lvl[startpos_y][0] = "p"
	player_vis_lvl[startpos_y][0] = "p"

	return(lvl)

def update_visual_lvl_matrix(lvl, player_rotate, owner):
	x = 0
	y = 0

	x = game.focus_offset.offset_x
	y = game.focus_offset.offset_y


	for line in lvl:
		for element in line:

			if element == "p":
				plate = img_player_plate(x, y, player_rotate)
				owner.matrix_plates_list.append(plate)
				index = 0
				for i in owner.matrix_plates_list:
					if type(i) != img_player_plate and i.rect.x == x and i.rect.y == y:
						del owner.matrix_plates_list[index]
						#plate = img_player_plate(x, y, player_rotate)
						#owner.matrix_plates_list.append(plate)
					
					if type(i) == img_player_plate and i.rect.x != x or type(i) == img_player_plate and i.rect.y != y:
						del owner.matrix_plates_list[index]
					index += 1

			if element == 0:
				index = 0
				for i in owner.matrix_plates_list:
					if i.rect.x == x and i.rect.y == y:
						del owner.matrix_plates_list[index]
						break
					index += 1

			if element == 1:
				index = 0
				for i in owner.matrix_plates_list:
					if type(i) != mechanic_plate and i.rect.x == x and i.rect.y == y:
						del owner.matrix_plates_list[index]
						plate = mechanic_plate(x, y, 1)
						owner.matrix_plates_list.append(plate)

					index += 1

			if element == 2:
				index = 0
				for i in owner.matrix_plates_list:
					if type(i) != mechanic_plate and i.rect.x == x and i.rect.y == y:
						del owner.matrix_plates_list[index]
						plate = mechanic_plate(x, y, 2)
						owner.matrix_plates_list.append(plate)

					index += 1

			if element == 3:
				index = 0
				for i in owner.matrix_plates_list:
					if type(i) != mechanic_plate and i.rect.x == x and i.rect.y == y:
						del owner.matrix_plates_list[index]
						plate = mechanic_plate(x, y, 3)
						owner.matrix_plates_list.append(plate)

					index += 1


			if type(element) == tuple:
				index = 0
				for i in owner.matrix_plates_list:
					if type(i) != img_plate_with_enemys and i.rect.x == x and i.rect.y == y:
						del owner.matrix_plates_list[index]
						plate = img_plate_with_enemys(x, y, element)
						owner.matrix_plates_list.append(plate)

					index += 1

		


			x += 16
		x = game.focus_offset.offset_x
		y += 16

def build_visual_lvl_matrix(lvl, player_rotate, owner):

	x = 0
	y = 0

	#x = game.focus_offset.offset_x
	#y = game.focus_offset.offset_y

	lenx_matrix = len(lvl[0]) - 1
	leny_matrix = 43 - 1
	print(leny_matrix)
	print(len(lvl))


	for line in lvl:
		for element in line:

			if element == 1:
				plate = mechanic_plate(x, y, 1)
				owner.matrix_plates_list.append(plate)

			if element == 2:
				plate = mechanic_plate(x, y, 2)
				owner.matrix_plates_list.append(plate)

			if element == 3:
				plate = mechanic_plate(x, y, 3)
				owner.matrix_plates_list.append(plate)

			if element == "p":
				plate = img_player_plate(x, y, player_rotate)
				owner.matrix_plates_list.append(plate)

			if element == 9:
				plate = img_plate(x, y)
				owner.matrix_plates_list.append(plate)
				if x == 0:
					plate = img_plate_border(x - 16, y, 1)
					owner.matrix_plates_list.append(plate)
				if x == lenx_matrix * 16:
					plate = img_plate_border(x + 16, y, 2)
					owner.matrix_plates_list.append(plate)
				if y == 0:
					plate = img_plate_border(x, y - 16, 4)
					owner.matrix_plates_list.append(plate)
				if y == leny_matrix * 16:
					plate = img_plate_border(x, y + 16, 3)
					owner.matrix_plates_list.append(plate)


			if type(element) == tuple:
				plate = img_plate_with_enemys(x, y, element)
				owner.matrix_plates_list.append(plate)

			x += 16
		#x = game.focus_offset.offset_x
		x = 0
		y += 16


class img_plate(pygame.sprite.Sprite):
	imgs = [(gg.matrix_plate9_1, gg.matrix_plate9_1_anim), (gg.matrix_plate9_2, gg.matrix_plate9_2_anim),
	(gg.matrix_plate9_3, gg.matrix_plate9_3_anim), (gg.matrix_plate9_4, gg.matrix_plate9_4_anim)]

	def __init__(self, x, y):

		pygame.sprite.Sprite.__init__(self)
		self.images_pack = random.choice(img_plate.imgs)
		self.image =  self.images_pack[0]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.anim = self.images_pack[1]
		self.anim_len = len(self.anim)
		self.is_anim = False
		self.curent_anim_frame = 0
		self.frame_timer = 0

		self.anim_reload = random.randint(0, 1500)
		self.anim_reload_timer = 0

	def update(self):
		if self.anim_reload_timer > self.anim_reload and self.is_anim == False:
			self.is_anim = True
			self.anim_reload = random.randint(100, 1300)
			self.anim_reload_timer = 0
		else:
			self.anim_reload_timer += 1

		if self.is_anim == True:
			if self.frame_timer > 25:
				self.image = self.anim[self.curent_anim_frame]
				self.curent_anim_frame += 1
				self.frame_timer = 0
				if self.anim_len <= self.curent_anim_frame:
					self.curent_anim_frame = 0
					self.is_anim = False
			else:
				self.frame_timer += 1


		
class img_plate_with_enemys(pygame.sprite.Sprite):
	def __init__(self, x, y, tuple_enemys_id):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((16,16))
		self.image.fill((255,255,255))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.enemys = tuple_enemys_id
	def update(self):
		pass


class img_player_plate(pygame.sprite.Sprite):
	def __init__(self, x, y, rotate):
		pygame.sprite.Sprite.__init__(self)
		self.image = gg.player
		self.image = pygame.transform.rotate(self.image, rotate)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	def update(self):
		pass


class mechanic_plate(pygame.sprite.Sprite):
	def __init__(self, x, y, qual):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((16,16))
		self.image.fill((255,255,0))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.qualification = qual

	def update(self):
		pass

class img_plate_border(pygame.sprite.Sprite):
	img_left = [gg.matrix_plate_9_border_left1]
	img_right = [gg.matrix_plate_9_border_right1]
	img_down = [gg.matrix_plate_9_border_down1]
	img_up = [gg.matrix_plate_9_border_up1]
	def __init__(self, x, y, l_r_d_u):
		pygame.sprite.Sprite.__init__(self)
		self.left_right_down_up = l_r_d_u
		if self.left_right_down_up == 1:
			self.image = img_plate_border.img_left[0]
		if self.left_right_down_up == 2:
			self.image = img_plate_border.img_right[0]
		if self.left_right_down_up == 3:
			self.image = img_plate_border.img_down[0]
		if self.left_right_down_up == 4:
			self.image = img_plate_border.img_up[0]

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self):
		pass

class planet_bg(pygame.sprite.Sprite):
	imgs = [gg.planet1, gg.planet2, gg.planet3]
	def __init__(self, size):
		pygame.sprite.Sprite.__init__(self)
		self.size = size
		self.image = random.choice(planet_bg.imgs)
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image, (self.rect.width * self.size, self.rect.height * self.size))
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(0, width - self.rect.width)
		self.rect.y = random.randint(0, height - self.rect.height)
	def update(self):
		pass


class background_manager():
	def __init__(self):
		self.to_spawn = [planet_bg]

		self.back_obj_layer1 = []
		self.back_obj_layer2 = []
		self.back_obj_layer3 = []

		objs_num = 10
		for i in range(objs_num):
			obj = random.choice(self.to_spawn)(1)
			self.back_obj_layer1.append(obj)

	def update(self):
		for i in self.back_obj_layer1:
			i.update()
			game_surface.blit(i.image, (i.rect.x, i.rect.y))
		for i in self.back_obj_layer2:
			i.update()
			game_surface.blit(i.image, (i.rect.x, i.rect.y))
		for i in self.back_obj_layer2:
			i.update()
			game_surface.blit(i.image, (i.rect.x, i.rect.y))




class game():
	def __init__(self):

		self.matrix_x = 100
		self.matrix_y = 43

		self.player_gun = gun3
		self.player_gun_mod = 0
		self.player_health = 10

		self.resours1 = 999
		self.resours2 = 999
		self.resours3 = 999

		self.all_enemys = [enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6, enemy_7, enemy_8, enemy_9]

		self.game_surface_scale = game_surface_scale()

		self.press_timer = 0

		self.action_lvl_now = False

		self.lvl_changed = True

		self.player_on_map_rotate = 270

		self.player_vis_lvl = [] #player_visible_lvl
		for i in range(self.matrix_y):
			line = []
			for i in range(self.matrix_x):
				line.append(9)
			self.player_vis_lvl.append(line)

		self.lvl_matrix = create_lvl_matrix(self.matrix_x,self.matrix_y, self.player_vis_lvl)
		updateble_objects_m.objects.append(self)

		self.background_m = background_manager()

		self.matrix_plates_list = []
		self.matrix_plates_in_draw_distance_list = []

		build_visual_lvl_matrix(self.player_vis_lvl, self.player_on_map_rotate, self)

		self.focus_offset = focus_offset(self)

	def update(self):

		self.background_m.update()


		press = pygame.key.get_pressed()
		if self.press_timer > 0:
			self.press_timer -= 1
		if self.action_lvl_now == False:
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

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 270

								if self.lvl_matrix[y][x+1] == 1 or self.lvl_matrix[y][x+1] == 2 or self.lvl_matrix[y][x+1] == 3: #triger for event

									self.action_lvl_now = True
									self.kill()				
									self.mechanic_upgrade = mechanic_upgrade_window(self.lvl_matrix[y][x+1], self)

									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y][x+1] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y][x+1] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 270

								if type(self.lvl_matrix[y][x+1]) == tuple:

									self.action_lvl_now = True
									self.kill()				
									self.action_lvl = action_lvl(self, self.get_enemy_name(self.lvl_matrix[y][x+1]))

									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y][x+1] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y][x+1] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 270
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

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 90

								if self.lvl_matrix[y][x-1] == 1 or self.lvl_matrix[y][x-1] == 2 or self.lvl_matrix[y][x-1] == 3: #triger for event

									self.action_lvl_now = True
									self.kill()				
									self.mechanic_upgrade = mechanic_upgrade_window(self.lvl_matrix[y][x-1], self)

									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y][x-1] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y][x-1] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 90

								if type(self.lvl_matrix[y][x-1]) == tuple:

									self.action_lvl_now = True
									self.kill()				
									self.action_lvl = action_lvl(self, self.get_enemy_name(self.lvl_matrix[y][x-1]))

									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y][x-1] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y][x-1] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 90
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

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 0

								if self.lvl_matrix[y-1][x] == 1 or self.lvl_matrix[y-1][x] == 2 or self.lvl_matrix[y-1][x] == 3: #triger for event

									self.action_lvl_now = True
									self.kill()				
									self.mechanic_upgrade = mechanic_upgrade_window(self.lvl_matrix[y-1][x], self)

									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y-1][x] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y-1][x] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 0


								if type(self.lvl_matrix[y-1][x]) == tuple:

									self.action_lvl_now = True
									self.kill()				
									self.action_lvl = action_lvl(self, self.get_enemy_name(self.lvl_matrix[y-1][x]))

									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y-1][x] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y-1][x] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 0
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

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 180

								if self.lvl_matrix[y+1][x] == 1 or self.lvl_matrix[y+1][x] == 2 or self.lvl_matrix[y+1][x] == 3: #triger for event


									self.action_lvl_now = True
									self.kill()				
									self.mechanic_upgrade = mechanic_upgrade_window(self.lvl_matrix[y+1][x], self)


									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y+1][x] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y+1][x] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 180

								if type(self.lvl_matrix[y+1][x]) == tuple:

									self.action_lvl_now = True
									self.kill()				
									self.action_lvl = action_lvl(self, self.get_enemy_name(self.lvl_matrix[y+1][x]))

									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y+1][x] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y+1][x] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 180
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
			if self.action_lvl_now == False and self.lvl_changed == True:
				update_visual_lvl_matrix(self.player_vis_lvl, self.player_on_map_rotate, self)
		self.lvl_changed = False

		if self.action_lvl_now == False:
			self.matrix_plates_list_update()
			self.draw_distance_info()
			self.matrix_plates_draw()

		if self.player_health <= 0:
			self.kill()
			updateble_objects_m.objects.remove(self)

	def kill(self):
		updateble_objects_m.objects.remove(self.focus_offset)
		post_processing_m.objects.remove(self.game_surface_scale)
		#updateble_objects_m.objects.remove(self.background_m)
		for i in all_sprites:
			i.kill()

	def append(self):
		updateble_objects_m.objects.append(self.focus_offset)
		post_processing_m.objects.append(self.game_surface_scale)
		#updateble_objects_m.objects.append(self.background_m)
		update_visual_lvl_matrix(self.player_vis_lvl, self.player_on_map_rotate, self)


	def get_enemy_name(self, tuple_with_id):
		enemy_list = []
		for i in self.all_enemys:
			for n in tuple_with_id:
				if i.enemy_id == n:
					enemy_list.append(i)
		return enemy_list

	def matrix_plates_list_update(self):
		#print(len(self.matrix_plates_list))
		for i in self.matrix_plates_list:
			i.update()

	def matrix_plates_draw(self):
		#print(len(self.matrix_plates_in_draw_distance_list))
		for i in self.matrix_plates_in_draw_distance_list:
			game_surface.blit(i.image, (i.rect.x, i.rect.y))

	def draw_distance_info(self):
		self.matrix_plates_in_draw_distance_list = []
		x = 0
		y = 0
		for i in self.matrix_plates_list:
			if type(i) == img_player_plate:
				x = i.rect.x
				y = i.rect.y
		x = absolute_number(x)
		y = absolute_number(y)
		for i in self.matrix_plates_list:
			if absolute_number(absolute_number(i.rect.x) - x) < 400 and absolute_number(absolute_number(i.rect.y) - y) < 200:
				self.matrix_plates_in_draw_distance_list.append(i)



class focus_offset():
	def __init__(self, owner):
		self.owner = owner

		self.offset_x = 0
		self.offset_y = 0

		self.move_right = False
		self.move_left = False
		self.move_up = False
		self.move_down = False

		self.left_max = 0
		self.right_max = 600
		self.up_max = 0
		self.down_max = 360

		self.centred_point_x = 0
		self.centred_point_y = 0

		self.speedx = 0
		self.speedy = 0

		updateble_objects_m.objects.append(self)

	def update(self):
		for i in self.owner.matrix_plates_list:
			if type(i) == img_player_plate:
				self.centred_point_x = i.rect.centerx
				self.centred_point_y = i.rect.centery

		if self.centred_point_x > 340:
			self.move_left = True

		if self.centred_point_x < 260:
			self.move_right = True

		if self.centred_point_y < 160:
			self.move_down = True

		if self.centred_point_y > 200:
			self.move_up = True

		if self.move_right:
			self.speedx = 3
		if self.move_left:
			self.speedx  -= 3
		if self.move_up:
			self.speedy  -= 3
		if self.move_down:
			self.speedy  += 3

		self.offset_x += self.speedx
		self.offset_y += self.speedy

		if self.speedx != 0 or self.speedy != 0:
			for i in all_sprites:
				i.rect.x += self.speedx
				i.rect.y += self.speedy

			for i in self.owner.matrix_plates_list:
				i.rect.x += self.speedx
				i.rect.y += self.speedy

		self.move_right = False
		self.move_left = False
		self.move_up = False
		self.move_down = False

		self.speedx = 0
		self.speedy = 0


class game_surface_scale():
	def __init__(self):
		self.scale_coefficient = 1
		post_processing_m.objects.append(self)


	def update(self):
		global game_surface
		new_width = int(width * self.scale_coefficient)
		new_height = int(height * self.scale_coefficient)

		game_surface.blit(pygame.transform.scale(game_surface, (new_width, new_height)), (-(int((new_width-width)/2)),-(int((new_height-height)/2))))

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:   
					self.scale_coefficient += 0.5
				if event.button == 5:   
					self.scale_coefficient -= 0.5

		if self.scale_coefficient < 1:
			self.scale_coefficient = 1
		if self.scale_coefficient > 2.5:
			self.scale_coefficient = 2.5


class action_lvl():
	def __init__(self, owner, enemys):
		self.owner = owner

		self.player = player(self.owner.player_gun, self.owner.player_gun_mod, self.owner.player_health)

		self.enemy_m = enemy_manager(enemys, self)
		self.hp_m = hp_manager(self)

		updateble_objects_m.objects.append(self)

	def update(self):
		press = pygame.key.get_pressed()
		if self.player.health <= 0:
			self.kill()

	def kill(self):
		for i in all_sprites:
			i.kill()
		game.action_lvl_now = False
		game.append()
		self.owner.player_health = self.player.health
		updateble_objects_m.objects.remove(self)
		updateble_objects_m.objects.remove(self.enemy_m)
		post_processing_m.objects.remove(self.hp_m)

class hp_manager():
	def __init__(self, owner):
		self.owner = owner
		self.hp = self.owner.player.health

		post_processing_m.objects.append(self)

	def update(self):
		self.hp = self.owner.player.health
		if self.hp > 0:
			x = 20
			y = 20
			for i in range(self.hp):
				game_surface.blit(gg.hp ,(x, y))
				x += 30


class player(pygame.sprite.Sprite):
	obj_type = "player"
	def __init__(self, gun, gun_mod_num, hp):
		pygame.sprite.Sprite.__init__(self)
		self.orig_img = gg.player_al
		self.image = self.orig_img.copy()
		self.rect = self.image.get_rect()
		self.rect.centerx = width / 2
		self.rect.centery = height - self.rect.height * 2

		self.health = hp

		self.gun = gun(self, gun_mod_num)

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

		self.image = self.orig_img.copy()
		self.gun.update()



class gun1(pygame.sprite.Sprite):
	obj_type = "gun"
	max_mod_number = 2
	q1_mech = [0,1]
	q2_mech = [0,1,2]
	q3_mech = [0,1,2]
	all_mechs = [q1_mech, q2_mech, q3_mech]

	img_mod1 = gg.gun1mod1
	img_mod2 = gg.gun1mod2
	img_mod3 = gg.gun1mod3

	all_img = [img_mod1, img_mod2, img_mod3]


	def __init__(self, owner, mod):
		pygame.sprite.Sprite.__init__(self)

		self.mod = mod

		self.max_mod_number = 2 #3 in fact, but 3-1, becouse index in python work like: list[0] - its a first element 
								#													   list[1] - its a second element


	#	if self.mod > self.max_mod_number:
	#		self.mod = self.max_mod_number

		self.image = gun1.all_img[self.mod]

		self.mod1_characteristics = [3, 3, 10, (2,3), 5]    #index: 0 - damage, 1 - bullet_speed, 2 - clip_size, 3 - size (x,y), 4 - delay
		self.mod2_characteristics = [3, 4, 14, (2,3), 5]
		self.mod3_characteristics = [4, 4, 16, (2,3), 5]

		self.all_mod_characteristics = [self.mod1_characteristics, self.mod2_characteristics, self.mod3_characteristics]
		self.characteristics = self.all_mod_characteristics[self.mod]

		self.rect = self.image.get_rect()
		self.owner = owner

		self.shoot_delay_timer = 0

		self.offset_x = 12
		self.offset_y = 7

	def update(self):
		self.owner.image.blit(self.image, (0,0))
		press = pygame.key.get_pressed()
		if press[pygame.K_SPACE] and self.shoot_delay_timer > self.characteristics[4]:
			self.shoot()
			self.shoot_delay_timer = 0

		if self.shoot_delay_timer <= self.characteristics[4]:
			self.shoot_delay_timer += 1


	def shoot(self):
		default_bullet(self.characteristics[0], self.characteristics[1], self.characteristics[3], self.owner.rect.x + self.offset_x, self.owner.rect.y + self.offset_y)

class gun2(pygame.sprite.Sprite):
	obj_type = "gun"
	max_mod_number = 2

	q1_mech = []
	q2_mech = [0]
	q3_mech = [0,1]
	all_mechs = [q1_mech, q2_mech, q3_mech]

	img_mod1 = gg.gun2mod1
	img_mod2 = gg.gun2mod2
	img_mod3 = gg.gun2mod3

	all_img = [img_mod1, img_mod2, img_mod3]

	def __init__(self, owner, mod):
		pygame.sprite.Sprite.__init__(self)

		self.mod = mod

		self.max_mod_number = 2 #3 in fact, but 3-1, becouse index in python work like: list[0] - its a first element 
								#													   list[1] - its a second element


	#	if self.mod > self.max_mod_number:
	#		self.mod = self.max_mod_number

		self.image = gun2.all_img[self.mod]

		self.mod1_characteristics = [3, 3, 10, (1,3), 5]    #index: 0 - damage, 1 - bullet_speed, 2 - clip_size, 3 - size (x,y), 4 - delay
		self.mod2_characteristics = [3, 4, 14, (1,3), 5]
		self.mod3_characteristics = [4, 4, 16, (1,3), 5]

		self.all_mod_characteristics = [self.mod1_characteristics, self.mod2_characteristics, self.mod3_characteristics]
		self.characteristics = self.all_mod_characteristics[self.mod]

		self.rect = self.image.get_rect()
		self.owner = owner

		self.shoot_delay_timer = 0

		self.offset1_x = 3
		self.offset1_y = 7

		self.offset2_x = 12
		self.offset2_y = 7


	def update(self):
		self.owner.image.blit(self.image, (0,0))
		press = pygame.key.get_pressed()
		if press[pygame.K_SPACE] and self.shoot_delay_timer > self.characteristics[4]:
			self.shoot()
			self.shoot_delay_timer = 0

		if self.shoot_delay_timer <= self.characteristics[4]:
			self.shoot_delay_timer += 1

	def shoot(self):
		default_bullet(self.characteristics[0], self.characteristics[1], self.characteristics[3], self.owner.rect.x + self.offset1_x, self.owner.rect.y + self.offset1_y)
		default_bullet(self.characteristics[0], self.characteristics[1], self.characteristics[3], self.owner.rect.x + self.offset2_x, self.owner.rect.y + self.offset2_y)


class gun3(pygame.sprite.Sprite):
	obj_type = "gun"
	max_mod_number = 3

	q1_mech = [0]
	q2_mech = [0,1,2]
	q3_mech = [0,1,2,3]
	all_mechs = [q1_mech, q2_mech, q3_mech]

	img_mod1 = gg.gun3mod1
	img_mod2 = gg.gun3mod2
	img_mod3 = gg.gun3mod3
	img_mod4 = gg.gun3mod4

	all_img = [img_mod1, img_mod2, img_mod3, img_mod4]

	def __init__(self, owner, mod):
		pygame.sprite.Sprite.__init__(self)

		self.mod = mod

		self.max_mod_number = 3 #4 in fact, but 4-1, becouse index in python work like: list[0] - its a first element 
								#													   list[1] - its a second element


	#	if self.mod > self.max_mod_number:
	#		self.mod = self.max_mod_number

		self.image = gun3.all_img[self.mod]

		self.mod1_characteristics = [3, 3, 10, (2,3), 5]    #index: 0 - damage, 1 - bullet_speed, 2 - clip_size, 3 - size (x,y), 4 - delay
		self.mod2_characteristics = [3, 4, 14, (2,3), 5]
		self.mod3_characteristics = [4, 4, 16, (2,3), 5]
		self.mod4_charecteristics = [4, 4, 16, (2,3), 9]

		self.all_mod_characteristics = [self.mod1_characteristics, self.mod2_characteristics, self.mod3_characteristics, self.mod4_charecteristics]
		self.characteristics = self.all_mod_characteristics[self.mod]

		self.rect = self.image.get_rect()
		self.owner = owner

		self.shoot_delay_timer = 0

		self.offset_x = 7
		self.offset_y = -1

	def update(self):
		self.owner.image.blit(self.image, (0,0))
		press = pygame.key.get_pressed()
		if press[pygame.K_SPACE] and self.shoot_delay_timer > self.characteristics[4]:
			self.shoot()
			self.shoot_delay_timer = 0

		if self.shoot_delay_timer <= self.characteristics[4]:
			self.shoot_delay_timer += 1

	def shoot(self):
		default_bullet(self.characteristics[0], self.characteristics[1], self.characteristics[3], self.owner.rect.x + self.offset_x, self.owner.rect.y + self.offset_y)

class default_bullet(pygame.sprite.Sprite):
	obj_type = "player_bullet"
	def __init__(self, damage, speed, size, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(size)
		self.image.fill((255,255,0))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.bottom = y

		self.damage = damage
		self.speed = speed


		all_sprites.add(self)

	def update(self):
		if self.rect.bottom < 0:
			self.kill()
		self.rect.y -= self.speed
		for i in game.action_lvl.enemy_m.enemy_list:
			if self.rect.colliderect(i):
				i.hp -= self.damage
				self.kill()




class test_enemy(pygame.sprite.Sprite):
	enemy_id = -1
	obj_type = "enemy"
	def __init__(self, x, y, enemy_manager):
		pygame.sprite.Sprite.__init__(self)
		self.image = gg.test_enemy
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.speedx_max = 2
		self.speedy_max = 2
		self.speedx_now = 0
		self.speedy_now = 0

		self.move_up = False
		self.move_down = False
		self.move_left = False
		self.move_right = False

		self.hp = 15

		self.bullet_speed = 4
		self.bullet_size = (2,4)
		self.shoot_delay = 60
		self.shoot_delay_timer = 0

		self.enemy_m = enemy_manager

		all_sprites.add(self)

	def update(self):

		if self.shoot_delay_timer > self.shoot_delay:
			enemy_bullet(self.bullet_speed, self.bullet_size, self.rect.x + self.rect.width/2, self.rect.bottom)
			self.shoot_delay_timer = 0
		if self.shoot_delay_timer <= self.shoot_delay:
			self.shoot_delay_timer += 1


		if self.hp <= 0:
			self.kill_self()


		if self.move_up:
			if -self.speedy_max < self.speedy_now:
				self.speedy_now -=1
		else:
			if self.speedy_now < 0:
				self.speedy_now += 1
		if self.move_down:
			if self.speedy_max > self.speedy_now:
				self.speedy_now += 1
		else:
			if self.speedy_now > 0:
				self.speedy_now -= 1
		if self.move_right:
			if self.speedx_max > self.speedx_now:
				self.speedx_now += 1
		else:
			if self.speedx_now > 0:
				self.speedx_now -= 1
		if self.move_left:
			if -self.speedx_max < self.speedx_now:
				self.speedx_now -= 1
		else:
			if self.speedx_now < 0:
				self.speedx_now += 1
		
		self.rect.x += self.speedx_now
		self.rect.y += self.speedy_now

	def go_to(self, x, y):
		if self.rect.centerx < x:
			if self.rect.centerx + self.speedx_now > x:
				self.speedx_now = x - self.rect.centerx
			self.move_right = True
		if self.rect.centerx > x:
			if self.rect.centerx - self.speedx_now < x:
				self.speedx_now = x - self.rect.centerx
			self.move_left = True
		if self.rect.centery < y:
			if self.rect.centery + self.speedy_now > y:
				self.speedy_now = y - self.rect.centery
			self.move_down = True
		if self.rect.centery > y:
			if self.rect.centery - self.speedy_now < y:
				self.speedy_now = y - self.rect.centery
			self.move_up = True

	def kill_self(self):
		self.kill()
		self.enemy_m.enemy_list.remove(self)

class enemy(pygame.sprite.Sprite):
	enemy_id = -1
	obj_type = "enemy"
	def __init__(self, x, y, enemy_manager):
		pygame.sprite.Sprite.__init__(self)
		self.orig_img = gg.enemy_1.copy()
		self.image = self.orig_img
		self.shoot_anim = gg.enemy_1_shoot_anim
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.speedx_max = 2
		self.speedy_max = 2
		self.speedx_now = 0
		self.speedy_now = 0

		self.move_up = False
		self.move_down = False
		self.move_left = False
		self.move_right = False

		self.hp = 15

		self.bullet_speed = 3
		self.bullet_size = (2,3)
		self.shoot_delay = 60
		self.shoot_delay_timer = 0
		self.bullet_color = (255,255,0)

		self.bullet_offset_x = 4
		self.bullet_offset_y = 20

		self.is_shoot_anim = False
		self.shoot_anim_len = len(self.shoot_anim)
		self.to_shoot_frame = 0
		self.curent_shoot_anim_frame = 0
		self.shoot_frame_timer = 0
		
		self.enemy_m = enemy_manager

		all_sprites.add(self)


	def update(self):
		if self.is_shoot_anim == True:
			self.shoot_anim_update()

		if self.shoot_delay_timer > self.shoot_delay:
			self.is_shoot_anim = True
			#enemy_bullet(self.bullet_speed, self.bullet_size, self.rect.x + self.rect.width/2, self.rect.bottom)
			self.shoot_delay_timer = 0
		if self.shoot_delay_timer <= self.shoot_delay:
			self.shoot_delay_timer += 1

		if self.hp <= 0:
			self.kill_self()

		if self.move_up:
			if -self.speedy_max < self.speedy_now:
				self.speedy_now -=1
		else:
			if self.speedy_now < 0:
				self.speedy_now += 1
		if self.move_down:
			if self.speedy_max > self.speedy_now:
				self.speedy_now += 1
		else:
			if self.speedy_now > 0:
				self.speedy_now -= 1
		if self.move_right:
			if self.speedx_max > self.speedx_now:
				self.speedx_now += 1
		else:
			if self.speedx_now > 0:
				self.speedx_now -= 1
		if self.move_left:
			if -self.speedx_max < self.speedx_now:
				self.speedx_now -= 1
		else:
			if self.speedx_now < 0:
				self.speedx_now += 1
		
		self.rect.x += self.speedx_now
		self.rect.y += self.speedy_now

	def go_to(self, x, y):
		if self.rect.centerx < x:
			if self.rect.centerx + self.speedx_now > x:
				self.speedx_now = x - self.rect.centerx
			self.move_right = True
		if self.rect.centerx > x:
			if self.rect.centerx - self.speedx_now < x:
				self.speedx_now = x - self.rect.centerx
			self.move_left = True
		if self.rect.centery < y:
			if self.rect.centery + self.speedy_now > y:
				self.speedy_now = y - self.rect.centery
			self.move_down = True
		if self.rect.centery > y:
			if self.rect.centery - self.speedy_now < y:
				self.speedy_now = y - self.rect.centery
			self.move_up = True

	def kill_self(self):
		self.kill()
		self.enemy_m.enemy_list.remove(self)

	def shoot(self):
		enemy_bullet(self.bullet_speed, self.bullet_size, self.rect.x + self.bullet_offset_x, self.rect.top + self.bullet_offset_y, self.bullet_color)

	def shoot_anim_update(self):

		if self.curent_shoot_anim_frame == self.to_shoot_frame and self.shoot_frame_timer == 0:
			self.shoot()

		if self.shoot_frame_timer > 2:
			self.image = self.shoot_anim[self.curent_shoot_anim_frame]
			self.curent_shoot_anim_frame += 1
			self.shoot_frame_timer = 0
			if self.shoot_anim_len <= self.curent_shoot_anim_frame:
				self.curent_shoot_anim_frame = 0
				self.is_shoot_anim = False

		else:
			self.shoot_frame_timer += 1



class enemy_1(enemy):
	enemy_id = 1
	def __init__(self, x, y, enemy_manager):
		enemy.__init__(self, x , y, enemy_manager)
		self.orig_img = gg.enemy_1.copy()
		self.image = self.orig_img
		self.shoot_anim = gg.enemy_1_shoot_anim
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.speedx_max = 2
		self.speedy_max = 2

		self.hp = 15

		self.to_shoot_frame = 0

		self.bullet_speed = 3
		self.bullet_size = (2,3)
		self.shoot_delay = 60
		self.shoot_delay_timer = 0

		self.bullet_offset_x = 4
		self.bullet_offset_y = 20
		
		self.shoot_anim_len = len(self.shoot_anim)

class enemy_2(enemy):
	enemy_id = 2
	def __init__(self, x, y, enemy_manager):
		enemy.__init__(self, x , y, enemy_manager)
		self.orig_img = gg.enemy_2.copy()
		self.image = self.orig_img
		self.shoot_anim = gg.enemy_2_shoot_anim
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.speedx_max = 2
		self.speedy_max = 2

		self.hp = 15

		self.to_shoot_frame = 0

		self.bullet_speed = 3
		self.bullet_size = (2,4)
		self.shoot_delay = 60
		self.shoot_delay_timer = 0

		self.bullet_offset1_x = 4
		self.bullet_offset1_y = 20
		self.bullet_offset2_x = 26
		self.bullet_offset2_y = 20

		self.shoot_anim_len = len(self.shoot_anim)

	def shoot(self):
		enemy_bullet(self.bullet_speed, self.bullet_size, self.rect.x + self.bullet_offset1_x, self.rect.top + self.bullet_offset1_y)
		enemy_bullet(self.bullet_speed, self.bullet_size, self.rect.x + self.bullet_offset2_x, self.rect.top + self.bullet_offset2_y)


class enemy_3(enemy):
	enemy_id = 3
	def __init__(self, x, y, enemy_manager):
		enemy.__init__(self, x , y, enemy_manager)
		self.orig_img = gg.enemy_3.copy()
		self.image = self.orig_img
		self.shoot_anim = gg.enemy_3_shoot_anim
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.speedx_max = 2
		self.speedy_max = 2

		self.hp = 15

		self.to_shoot_frame = 0

		self.bullet_speed = 3
		self.bullet_size = (2,4)
		self.shoot_delay = 60
		self.shoot_delay_timer = 0

		self.bullet_offset1_x = 4
		self.bullet_offset1_y = 33
		self.bullet_offset2_x = 26
		self.bullet_offset2_y = 33

		self.shoot_anim_len = len(self.shoot_anim)

	def shoot(self):
		enemy_bullet(self.bullet_speed, self.bullet_size, self.rect.x + self.bullet_offset1_x, self.rect.top + self.bullet_offset1_y, self.bullet_color)
		enemy_bullet(self.bullet_speed, self.bullet_size, self.rect.x + self.bullet_offset2_x, self.rect.top + self.bullet_offset2_y, self.bullet_color)

	def kill_self(self):
		self.kill()
		self.enemy_m.enemy_list.remove(self)
		m = mine(self.rect.centerx, self.rect.bottom)

class mine(pygame.sprite.Sprite):
	obj_type = "mine"
	def __init__(self, center_x, bottom):
		pygame.sprite.Sprite.__init__(self)
		self.image = gg.enemy_3_mine
		self.anim = gg.enemy_3_mine_light_anim
		self.rect = self.image.get_rect()
		self.rect.centerx = center_x
		self.rect.bottom = bottom

		self.anim_len = len(self.anim)
		self.is_anim = False
		self.curent_anim_frame = 0
		self.frame_timer = 0

		self.anim_reload_timer = 0
		self.anim_reload = 50

		all_sprites.add(self)


	def update(self):

		self.rect.y += 1
		if self.rect.y > height:
			self.kill()

		if self.anim_reload_timer > self.anim_reload and self.is_anim == False:
			self.is_anim = True
			self.anim_reload = 200
			self.anim_reload_timer = 0
		else:
			self.anim_reload_timer += 1

		if self.is_anim == True:
			if self.frame_timer > 3:
				self.image = self.anim[self.curent_anim_frame]
				self.curent_anim_frame += 1
				self.frame_timer = 0
				if self.anim_len <= self.curent_anim_frame:
					self.curent_anim_frame = 0
					self.is_anim = False
			else:
				self.frame_timer += 1

		if self.rect.colliderect(game.action_lvl.player.rect):
			game.action_lvl.player.health -= 1
			self.kill()

class enemy_4(enemy):
	enemy_id = 4
	def __init__(self, x, y, enemy_manager):
		enemy.__init__(self, x , y, enemy_manager)
		self.orig_img = gg.enemy_4.copy()
		self.image = self.orig_img
		self.shoot_anim = gg.enemy_4_shoot_anim
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.speedx_max = 2
		self.speedy_max = 2

		self.hp = 15

		self.to_shoot_frame = 0

		self.bullet_speed = 3
		self.bullet_size = (2,3)
		self.shoot_delay = 1000
		self.shoot_delay_timer = 0

		self.bullet_offset_x = 8
		self.bullet_offset_y = 10
		
		self.shoot_anim_len = len(self.shoot_anim)

	def shoot(self):
		rocket = enemy_4_rocket(self)


class enemy_4_rocket(pygame.sprite.Sprite):
	obj_type = "enemy_4_rocket"
	def __init__(self, enemy):
		self.enemy = enemy
		pygame.sprite.Sprite.__init__(self)
		self.image = gg.enemy_4_rocket
		self.anim = gg.enemy_4_rocket_shoot_anim
		self.rect = self.image.get_rect()

		self.anim_len = len(self.anim)
		self.is_anim = False
		self.curent_anim_frame = 0
		self.frame_timer = 0

		self.init_anim = gg.enemy_4_rocket_init_anim
		self.is_init_anim = True
		self.init_anim_len = len(self.init_anim)
		self.curent_init_anim_frame = 0
		self.init_anim_frame_timer = 0

		self.rect.x = self.enemy.rect.x
		self.rect.y = self.enemy.rect.y

		all_sprites.add(self)

	def update(self):

		if self.rect.y > height:
			self.kill()

		if self.is_init_anim:
			if self.init_anim_frame_timer > 3:
				self.image = self.init_anim[self.curent_init_anim_frame]
				self.curent_init_anim_frame += 1
				self.init_anim_frame_timer = 0
				if self.init_anim_len <= self.curent_init_anim_frame:
					self.curent_init_anim_frame = 0
					self.is_init_anim = False
					self.is_anim = True

					self.image = self.anim[self.curent_anim_frame]
					self.rect = self.image.get_rect()
					self.rect.centerx = self.enemy.rect.centerx
					self.rect.bottom = self.enemy.rect.bottom
			else:
				self.init_anim_frame_timer += 1



		if self.is_anim == True:
			self.rect.y += 3
			if self.frame_timer > 3:
				self.image = self.anim[self.curent_anim_frame]
				self.curent_anim_frame += 1
				self.frame_timer = 0
				if self.anim_len <= self.curent_anim_frame:
					self.curent_anim_frame = 0
					#self.is_anim = False
			else:
				self.frame_timer += 1

		if self.rect.colliderect(game.action_lvl.player.rect):
			game.action_lvl.player.health -= 1
			self.kill()

class enemy_5(enemy):
	enemy_id = 5
	def __init__(self, x, y, enemy_manager):
		enemy.__init__(self, x , y, enemy_manager)
		self.orig_img = gg.enemy_5.copy()
		self.image = self.orig_img
		self.shoot_anim = gg.enemy_5_shoot_anim
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.speedx_max = 2
		self.speedy_max = 2

		self.hp = 15

		self.to_shoot_frame = 0

		self.bullet_speed = 3
		self.bullet_size = (2,3)
		self.shoot_delay = 60
		self.shoot_delay_timer = 0

		self.bullet_offset1_x = 4
		self.bullet_offset1_y = 33

		self.bullet_offset2_x = 16
		self.bullet_offset2_y = 33

		self.bullet_offset3_x = 28
		self.bullet_offset3_y = 33
		
		self.shoot_anim_len = len(self.shoot_anim)

	def shoot(self):
		if self.curent_shoot_anim_frame == 0:
			enemy_bullet(self.bullet_speed, self.bullet_size, self.rect.x + self.bullet_offset1_x, self.rect.top + self.bullet_offset1_y, self.bullet_color)
			self.to_shoot_frame = 1
		if self.curent_shoot_anim_frame == 1:
			enemy_bullet(self.bullet_speed, self.bullet_size, self.rect.x + self.bullet_offset2_x, self.rect.top + self.bullet_offset2_y, self.bullet_color)
			self.to_shoot_frame = 2
		if self.curent_shoot_anim_frame == 2:
			enemy_bullet(self.bullet_speed, self.bullet_size, self.rect.x + self.bullet_offset3_x, self.rect.top + self.bullet_offset3_y, self.bullet_color)
			self.to_shoot_frame = 0

class enemy_6(enemy):
	enemy_id = 6
	def __init__(self, x, y, enemy_manager):
		enemy.__init__(self, x , y, enemy_manager)
		self.orig_img = gg.enemy_6.copy()
		self.image = self.orig_img
		self.shoot_anim = gg.enemy_6_shoot_anim
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.speedx_max = 2
		self.speedy_max = 2

		self.hp = 15

		self.to_shoot_frame = 0

		self.bullet_speed = 8
		self.bullet_size = (4,6)
		self.shoot_delay = 60
		self.shoot_delay_timer = 0

		self.bullet_offset_x = 14
		self.bullet_offset_y = 33
		
		self.shoot_anim_len = len(self.shoot_anim)

class enemy_7(enemy):
	enemy_id = 7
	def __init__(self, x, y, enemy_manager):
		enemy.__init__(self, x , y, enemy_manager)

		self.orig_img = gg.enemy_7.copy()
		self.image = self.orig_img
		self.shoot_anim = gg.enemy_7_shoot_anim
		self.reload_anim = gg.enemy_7_reload_anim

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.speedx_max = 2
		self.speedy_max = 2

		self.hp = 15

		self.to_shoot_frame = 0

		self.bullet_speed = 7
		self.bullet_size = (4,5)

		self.shoot_delay = 60
		self.shoot_delay_timer = 0

		self.bullet_offset_x = 14
		self.bullet_offset_y = 28

		self.is_reload_anim = True
		self.curent_reload_anim_frame = 0
		self.reload_anim_len = len(self.reload_anim)
		self.relaod_anim_timer = 0

		
		self.shoot_anim_len = len(self.shoot_anim)

	def update(self):
		if self.shoot_anim_len <= self.curent_shoot_anim_frame + 1:
			self.is_reload_anim = True

		enemy.update(self)

		if self.is_reload_anim == True:

			if self.relaod_anim_timer > 3:
				self.image = self.reload_anim[self.curent_reload_anim_frame]
				self.curent_reload_anim_frame += 1
				self.relaod_anim_timer = 0
				if self.reload_anim_len <= self.curent_reload_anim_frame:
					self.curent_reload_anim_frame = 0
					self.is_reload_anim = False

			else:
				self.relaod_anim_timer += 1

class enemy_8(enemy):
	enemy_id = 8
	def __init__(self, x, y, enemy_manager):
		enemy.__init__(self, x , y, enemy_manager)
		self.orig_img = gg.enemy_8.copy()
		self.image = self.orig_img
		self.shoot_anim = gg.enemy_8_shoot_anim
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.speedx_max = 2
		self.speedy_max = 2

		self.hp = 15

		self.to_shoot_frame = 6

		self.bullet_speed = 7
		self.bullet_size = (4,8)
		self.shoot_delay = 60
		self.shoot_delay_timer = 0

		self.bullet_offset_x = 16
		self.bullet_offset_y = 37

		self.bullet_color = (197, 203, 232)
		
		self.shoot_anim_len = len(self.shoot_anim)

class enemy_9(enemy):
	enemy_id = 9
	def __init__(self, x, y, enemy_manager):
		enemy.__init__(self, x , y, enemy_manager)
		self.orig_img = gg.enemy_9.copy()
		self.image = self.orig_img
		self.shoot_anim = gg.enemy_9_shoot_anim
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.speedx_max = 2
		self.speedy_max = 2

		self.hp = 15

		self.to_shoot_frame = 0

		self.bullet_speed = 7
		self.bullet_size = (4,4)
		self.shoot_delay = 60
		self.shoot_delay_timer = 0

		self.bullet_offset1_x = 3
		self.bullet_offset1_y = 30

		self.bullet_offset2_x = 24
		self.bullet_offset2_y = 30


		self.bullet_color = (255, 255, 0)
		
		self.shoot_anim_len = len(self.shoot_anim)

		self.shield_reload = 3000
		self.shield_reload_timer = 3000


	def update(self):
		enemy.update(self)
		if self.shield_reload_timer > self.shield_reload:
			self.shield_reload_timer = 0
			shield = enemy_9_shield(self)
		else:
			self.shield_reload_timer += 1

	def shoot(self):
		enemy_bullet(self.bullet_speed, self.bullet_size, self.rect.x + self.bullet_offset1_x, self.rect.top + self.bullet_offset1_y, self.bullet_color)
		enemy_bullet(self.bullet_speed, self.bullet_size, self.rect.x + self.bullet_offset2_x, self.rect.top + self.bullet_offset2_y, self.bullet_color)

class enemy_9_shield(pygame.sprite.Sprite):
	obj_type = "enemy_9_shield"
	def __init__(self, enemy):
		pygame.sprite.Sprite.__init__(self)
		self.image = gg.enemy_9_shield
		self.anim = gg.enemy_9_shield_anim
		self.rect = self.image.get_rect()

		self.anim_len = len(self.anim)
		self.is_anim = False
		self.curent_anim_frame = 0
		self.frame_timer = 0

		self.init_anim = gg.enemy_9_shield_init_anim
		self.is_init_anim = True
		self.init_anim_len = len(self.init_anim)
		self.curent_init_anim_frame = 0
		self.init_anim_frame_timer = 0

		self.kill_anim = gg.enemy_9_shield_kill_anim
		self.is_kill_anim = False
		self.kill_anim_len = len(self.kill_anim)
		self.curent_kill_anim_frame = 0
		self.kill_anim_frame_timer = 0

		self.anim_reload_timer = 0
		self.anim_reload = 50

		self.to_live = 400
		self.live_timer = 0

		self.enemy = enemy

		all_sprites.add(self)

	def update(self):
		if self.live_timer > self.to_live:
			self.is_kill_anim = True

		else:
			self.live_timer += 1

		self.rect = self.image.get_rect()
		self.rect.centerx = self.enemy.rect.centerx
		self.rect.top = self.enemy.rect.bottom + 1

		if self.is_init_anim:
			if self.init_anim_frame_timer > 3:
				self.image = self.init_anim[self.curent_init_anim_frame]
				self.curent_init_anim_frame += 1
				self.init_anim_frame_timer = 0
				if self.init_anim_len <= self.curent_init_anim_frame:
					self.curent_init_anim_frame = 0
					self.is_init_anim = False
					self.is_anim = True
			else:
				self.init_anim_frame_timer += 1


		if self.is_anim == True:
			if self.frame_timer > 3:
				self.image = self.anim[self.curent_anim_frame]
				self.curent_anim_frame += 1
				self.frame_timer = 0
				if self.anim_len <= self.curent_anim_frame:
					self.curent_anim_frame = 0
					self.is_anim = False
			else:
				self.frame_timer += 1

		if self.is_kill_anim == True:
			if self.kill_anim_frame_timer > 3:
				self.image = self.kill_anim[self.curent_kill_anim_frame]
				self.curent_kill_anim_frame += 1
				self.kill_anim_frame_timer = 0
				if self.kill_anim_len <= self.curent_kill_anim_frame:
					self.curent_kill_anim_frame = 0
					self.is_kill_anim = False
					self.kill()
			else:
				self.kill_anim_frame_timer += 1

		if self.rect.colliderect(game.action_lvl.player.rect) and self.is_kill_anim == False:
			game.action_lvl.player.health -= 1
			self.is_kill_anim = True






class enemy_bullet(pygame.sprite.Sprite):
	obj_type = "enemy_bullet"
	def __init__(self, speed, size, x, y, color):
		pygame.sprite.Sprite.__init__(self)
		self.color = color
		self.image = pygame.Surface(size)
		self.image.fill(self.color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.top = y

		self.speed = speed

		all_sprites.add(self)

	def update(self):
		if self.rect.top > height:
			self.kill()
		self.rect.y += self.speed
		for i in all_sprites:
			if type(i).obj_type == "player" and self.rect.colliderect(i):
				i.health -= 1
				self.kill()

class enemy_manager():
	def __init__(self, enemys, action_lvl_obj):
		self.to_spawn = enemys
		self.enemy_list = []

		self.action_lvl = action_lvl_obj

		self.enemy_counter = 10


		updateble_objects_m.objects.append(self)

	def update(self):
		if len(self.enemy_list) < 3 and self.enemy_counter > 0:
			enemy = random.choice(self.to_spawn)(random.randint(0, 586), random.randint(0, 346), self)
			self.enemy_counter -= 1
			self.enemy_list.append(enemy)

		if self.enemy_counter <= 0 and len(self.enemy_list) <= 0:
			self.action_lvl.kill()

class mouse(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10, 10))
		self.rect = self.image.get_rect()
		self.image.fill((255,0,0))
		self.rect.centerx = width / 2
		self.rect.centery = height / 2
		pygame.mouse.set_visible(False)
		all_sprites.add(self)
	def update(self):
		mouse_rel = pygame.mouse.get_rel()
		self.rect.x += int(mouse_rel[0])
		self.rect.y += int(mouse_rel[1])
		if self.rect.bottom > height:
			self.rect.bottom = height
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > width:
			self.rect.right = width
		if self.rect.top < 0:
			self.rect.top = 0

class mechanic_upgrade_window():
	q1_guns = [gun1]
	q2_guns = [gun1, gun2, gun3]
	q3_guns = [gun1, gun2, gun3]
	all_q = [q1_guns, q2_guns, q3_guns]
	def __init__(self, qual, owner):

		self.mouse = mouse()

		self.qualification = qual - 1
		self.owner = owner

		self.to_upgrade_list = []
		self.can_upgrade = mechanic_upgrade_window.all_q[self.qualification]

		for i in self.can_upgrade:
			if i == self.owner.player_gun:
				if i.all_mechs[self.qualification] != []:
					for x in i.all_mechs[self.qualification]:
						if i.max_mod_number >= self.owner.player_gun_mod + 1:
							mod = self.owner.player_gun_mod + 1

							self.to_upgrade_list.append((i, mod))
							self.can_upgrade.remove(i)
							break

		if self.can_upgrade != []:
			self.to_upgrade_slot2 = random.choice(self.can_upgrade)
			self.can_upgrade.remove(self.to_upgrade_slot2)
			self.to_upgrade_list.append((self.to_upgrade_slot2, 0))
		if self.can_upgrade != []:
			self.to_upgrade_slot3 = random.choice(self.can_upgrade)
			self.can_upgrade.remove(self.to_upgrade_slot3)
			self.to_upgrade_list.append((self.to_upgrade_slot3, 0))

		x = 150
		y = 200
		num = 0
		for i in range(len(self.to_upgrade_list)):
			b = button_for_mechanic_window(x, y, self, num)
			x += 100
			num+=1


		updateble_objects_m.objects.append(self)

	def update(self):
		x = 100
		y = 150
		for i in self.to_upgrade_list:
			#print(str(i))
			game_surface.blit(i[0].all_img[i[1]], (x, y))
			x += 100
		draw_text(game_surface, "qualification"+str(self.qualification), 20, 20, 20, (255,255,255))




	def kill(self, num):
		for i in all_sprites:
			i.kill()
		updateble_objects_m.objects.remove(self)
		self.owner.player_gun = self.to_upgrade_list[num][0]
		self.owner.player_gun_mod = self.to_upgrade_list[num][1]
		self.owner.append()
		self.owner.action_lvl_now = False

class button_for_mechanic_window(pygame.sprite.Sprite):
	def __init__(self, x, y, owner, num):
		pygame.sprite.Sprite.__init__(self)
		self.owner = owner
		self.numeration = num
		self.image = pygame.Surface((70, 40))
		self.image.fill((0,255,255))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		all_sprites.add(self)
	def update(self):
		mouse_pressed = pygame.mouse.get_pressed()
		if self.rect.colliderect(self.owner.mouse) and mouse_pressed[0]:
			self.owner.kill(self.numeration)




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
	game_surface.fill((13, 13, 35))
	updateble_objects_m.update()
	all_sprites.update()
	all_sprites.draw(game_surface)
	post_processing_m.update()

	fullscreen_with_ratio()

	real_fps = int(clock.get_fps())

	draw_text(window, str(real_fps), 20, 60, 20, (255,255,255))
	draw_text(window, str(all_sprites), 10, 600, 40, (255,255,255))
	draw_text(window, str(updateble_objects_m.objects), 10, 600, 50, (255,255,255))
	draw_text(window, str(post_processing_m.objects), 10, 600, 60, (255,255,255))	

	pygame.display.flip()