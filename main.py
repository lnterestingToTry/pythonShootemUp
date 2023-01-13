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

mouse_position_x = width / 2
mouse_position_y = height / 2

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

		self.matrix_plate9_1 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant1\\fog.png")).convert_alpha()
		self.matrix_plate9_1_anim = []
		for i in listdir(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant1\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant1\\anim\\{}".format(i))).convert_alpha()
			self.matrix_plate9_1_anim.append(img)
			#print(i)

		self.matrix_plate9_2 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant2\\fog.png")).convert_alpha()
		self.matrix_plate9_2_anim = []
		for i in listdir(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant2\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant2\\anim\\{}".format(i))).convert_alpha()
			self.matrix_plate9_2_anim.append(img)
			#print(i)

		self.matrix_plate9_3 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant3\\fog.png")).convert_alpha()
		self.matrix_plate9_3_anim = []
		for i in listdir(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant3\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant3\\anim\\{}".format(i))).convert_alpha()
			self.matrix_plate9_3_anim.append(img)
			#print(i)

		self.matrix_plate9_4 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant4\\fog.png")).convert_alpha()
		self.matrix_plate9_4_anim = []
		for i in listdir(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant4\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant4\\anim\\{}".format(i))).convert_alpha()
			self.matrix_plate9_4_anim.append(img)
			#print(i)

		self.matrix_plate9_5 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant5\\fog.png")).convert_alpha()
		self.matrix_plate9_5_anim = []
		for i in listdir(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant5\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant5\\anim\\{}".format(i))).convert_alpha()
			self.matrix_plate9_5_anim.append(img)

		self.matrix_plate9_6 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant6\\fog.png")).convert_alpha()
		self.matrix_plate9_6_anim = []
		for i in listdir(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant6\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant6\\anim\\{}".format(i))).convert_alpha()
			self.matrix_plate9_6_anim.append(img)

		self.matrix_plate9_7 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant7\\fog.png")).convert_alpha()
		self.matrix_plate9_7_anim = []
		for i in listdir(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant7\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant7\\anim\\{}".format(i))).convert_alpha()
			self.matrix_plate9_7_anim.append(img)

		self.matrix_plate9_8 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant6\\fog.png")).convert_alpha()
		self.matrix_plate9_8_anim = []
		for i in listdir(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant8\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\variant8\\anim\\{}".format(i))).convert_alpha()
			self.matrix_plate9_8_anim.append(img)

		self.matrix_plate_9_border_right1 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\border_fog\\b_fog_right1.png")).convert_alpha()
		self.matrix_plate_9_border_up1 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\border_fog\\b_fog_up1.png")).convert_alpha()
		self.matrix_plate_9_border_down1 = pygame.transform.flip(self.matrix_plate_9_border_up1, False, True)
		self.matrix_plate_9_border_left1 = pygame.transform.flip(self.matrix_plate_9_border_right1, True, False)
		self.matrix_plate_9_border_left_up = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\fog_plate\\border_fog\\b_fog_left_up1.png")).convert_alpha()
		self.matrix_plate_9_border_right_up = pygame.transform.rotate(self.matrix_plate_9_border_left_up, -90)
		self.matrix_plate_9_border_left_down = pygame.transform.rotate(self.matrix_plate_9_border_right_up, 180)
		self.matrix_plate_9_border_right_down = pygame.transform.rotate(self.matrix_plate_9_border_left_down, 90)

		self.matrix_plate_1_2_3 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\mechanic_plate\\plate.png")).convert_alpha()
		self.matrix_plate_1_2_3_anim = []
		for i in listdir(path.join(this_directory, "g\\matrix_plates\\mechanic_plate\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\mechanic_plate\\anim\\{}".format(i))).convert_alpha()
			self.matrix_plate_1_2_3_anim.append(img)

		self.test_enemy = pygame.image.load(path.join(this_directory, "g\\enemys\\test_enemy\\ship.png")).convert_alpha()

		self.planet1 = pygame.image.load(path.join(this_directory, "g\\background\\planets\\planet1.png")).convert_alpha()
		self.planet2 = pygame.image.load(path.join(this_directory, "g\\background\\planets\\planet2.png")).convert_alpha()
		self.planet3 = pygame.image.load(path.join(this_directory, "g\\background\\planets\\planet3.png")).convert_alpha()

		self.star1 = pygame.image.load(path.join(this_directory, "g\\background\\stars\\star1.png")).convert_alpha()
		self.star2 = pygame.image.load(path.join(this_directory, "g\\background\\stars\\star2.png")).convert_alpha()
		self.star3 = pygame.image.load(path.join(this_directory, "g\\background\\stars\\star3.png")).convert_alpha()

		self.enemy_1 = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_1\\enemy_1.png")).convert_alpha()
		self.enemy_1_icon = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_1\\matrix_icon.png")).convert_alpha()
		self.enemy_1_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_1\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_1\\shoot_anim\\{}".format(i))).convert_alpha()
			self.enemy_1_shoot_anim.append(img)

		self.enemy_2 = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_2\\enemy_2.png")).convert_alpha()
		self.enemy_2_icon = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_2\\matrix_icon.png")).convert_alpha()
		self.enemy_2_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_2\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_2\\shoot_anim\\{}".format(i))).convert_alpha()
			self.enemy_2_shoot_anim.append(img)

		self.enemy_3 = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_3\\enemy_3.png")).convert_alpha()
		self.enemy_3_icon = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_3\\matrix_icon.png")).convert_alpha()
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
		self.enemy_4_icon = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_4\\matrix_icon.png")).convert_alpha()
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
		self.enemy_5_icon = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_5\\matrix_icon.png")).convert_alpha()
		self.enemy_5_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_5\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_5\\shoot_anim\\{}".format(i))).convert_alpha()
			self.enemy_5_shoot_anim.append(img)

		self.enemy_6 = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_6\\enemy_6.png")).convert_alpha()
		self.enemy_6_icon = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_6\\matrix_icon.png")).convert_alpha()
		self.enemy_6_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_6\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_6\\shoot_anim\\{}".format(i))).convert_alpha()
			self.enemy_6_shoot_anim.append(img)

		self.enemy_7 = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_7\\enemy_7.png")).convert_alpha()
		self.enemy_7_icon = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_7\\matrix_icon.png")).convert_alpha()
		self.enemy_7_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_7\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_7\\shoot_anim\\{}".format(i))).convert_alpha()
			self.enemy_7_shoot_anim.append(img)
		self.enemy_7_reload_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_7\\reload_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_7\\reload_anim\\{}".format(i))).convert_alpha()
			self.enemy_7_reload_anim.append(img)

		self.enemy_8 = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_8\\enemy_8.png")).convert_alpha()
		self.enemy_8_icon = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_8\\matrix_icon.png")).convert_alpha()
		self.enemy_8_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_8\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_8\\shoot_anim\\{}".format(i))).convert_alpha()
			self.enemy_8_shoot_anim.append(img)

		self.enemy_9 = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_9\\enemy_9.png")).convert_alpha()
		self.enemy_9_icon = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_9\\matrix_icon.png")).convert_alpha()
		self.enemy_9_shoot_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_9\\shoot_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_9\\shoot_anim\\{}".format(i))).convert_alpha()
			self.enemy_9_shoot_anim.append(img)
		self.enemy_9_shield = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_9\\shield\\shield.png")).convert_alpha()
		self.enemy_9_shield_init_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_9\\shield\\init_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_9\\shield\\init_anim\\{}".format(i))).convert_alpha()
			self.enemy_9_shield_init_anim.append(img)
		self.enemy_9_shield_anim = []
		for i in listdir(path.join(this_directory, "g\\enemy_ships\\enemy_9\\shield\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\enemy_ships\\enemy_9\\shield\\anim\\{}".format(i))).convert_alpha()
			self.enemy_9_shield_anim.append(img)
		self.enemy_9_shield_kill_anim = revers_list(self.enemy_9_shield_init_anim)

		self.player_gun1_mod1 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_1\\mod_1\\gun1_mod1.png")).convert_alpha()
		self.player_gun1_mod1_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_1\\mod_1\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_1\\mod_1\\anim\\{}".format(i))).convert_alpha()
			self.player_gun1_mod1_anim.append(img)

		self.player_gun1_mod2 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_1\\mod_2\\gun1_mod2.png")).convert_alpha()
		self.player_gun1_mod2_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_1\\mod_2\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_1\\mod_2\\anim\\{}".format(i))).convert_alpha()
			self.player_gun1_mod2_anim.append(img)

		self.player_gun1_mod3 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_1\\mod_3\\gun1_mod3.png")).convert_alpha()
		self.player_gun1_mod3_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_1\\mod_3\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_1\\mod_3\\anim\\{}".format(i))).convert_alpha()
			self.player_gun1_mod3_anim.append(img)

		self.player_gun2_mod1 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_2\\mod_1\\gun2_mod1.png")).convert_alpha()
		self.player_gun2_mod1_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_2\\mod_1\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_2\\mod_1\\anim\\{}".format(i))).convert_alpha()
			self.player_gun2_mod1_anim.append(img)

		self.player_gun2_mod2 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_2\\mod_2\\gun2_mod2.png")).convert_alpha()
		self.player_gun2_mod2_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_2\\mod_2\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_2\\mod_2\\anim\\{}".format(i))).convert_alpha()
			self.player_gun2_mod2_anim.append(img)

		self.player_gun2_mod3 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_2\\mod_3\\gun2_mod3.png")).convert_alpha()
		self.player_gun2_mod3_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_2\\mod_3\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_2\\mod_3\\anim\\{}".format(i))).convert_alpha()
			self.player_gun2_mod3_anim.append(img)

		self.player_gun3_mod1 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_3\\mod_1\\gun3_mod1.png")).convert_alpha()
		self.player_gun3_mod1_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_3\\mod_1\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_3\\mod_1\\anim\\{}".format(i))).convert_alpha()
			self.player_gun3_mod1_anim.append(img)

		self.player_gun3_mod2 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_3\\mod_2\\gun3_mod2.png")).convert_alpha()
		self.player_gun3_mod2_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_3\\mod_2\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_3\\mod_2\\anim\\{}".format(i))).convert_alpha()
			self.player_gun3_mod2_anim.append(img)

		self.player_gun3_mod3 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_3\\mod_3\\gun3_mod3.png")).convert_alpha()
		self.player_gun3_mod3_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_3\\mod_3\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_3\\mod_3\\anim\\{}".format(i))).convert_alpha()
			self.player_gun3_mod3_anim.append(img)

		self.player_gun3_mod4 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_3\\mod_4\\gun3_mod4.png")).convert_alpha()
		self.player_gun3_mod4_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_3\\mod_4\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_3\\mod_4\\anim\\{}".format(i))).convert_alpha()
			self.player_gun3_mod4_anim.append(img)

		self.player_gun4_mod1 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_4\\mod_1\\gun4_mod1.png")).convert_alpha()
		self.player_gun4_mod1_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_4\\mod_1\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_4\\mod_1\\anim\\{}".format(i))).convert_alpha()
			self.player_gun4_mod1_anim.append(img)

		self.player_gun4_mod2 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_4\\mod_2\\gun4_mod2.png")).convert_alpha()
		self.player_gun4_mod2_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_4\\mod_2\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_4\\mod_2\\anim\\{}".format(i))).convert_alpha()
			self.player_gun4_mod2_anim.append(img)

		self.player_gun4_mod3 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_4\\mod_3\\gun4_mod3.png")).convert_alpha()
		self.player_gun4_mod3_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_4\\mod_3\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_4\\mod_3\\anim\\{}".format(i))).convert_alpha()
			self.player_gun4_mod3_anim.append(img)

		self.player_gun5_mod1 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_5\\mod_1\\gun5_mod1.png")).convert_alpha()
		self.player_gun5_mod1_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_5\\mod_1\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_5\\mod_1\\anim\\{}".format(i))).convert_alpha()
			self.player_gun5_mod1_anim.append(img)

		self.player_gun5_mod2 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_5\\mod_2\\gun5_mod2.png")).convert_alpha()
		self.player_gun5_mod2_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_5\\mod_2\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_5\\mod_2\\anim\\{}".format(i))).convert_alpha()
			self.player_gun5_mod2_anim.append(img)

		self.player_gun5_mod3 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_5\\mod_3\\gun5_mod3.png")).convert_alpha()
		self.player_gun5_mod3_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_5\\mod_3\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_5\\mod_3\\anim\\{}".format(i))).convert_alpha()
			self.player_gun5_mod3_anim.append(img)

		self.player_gun6_mod1 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_6\\mod_1\\gun6_mod1.png")).convert_alpha()
		self.player_gun6_mod1_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_6\\mod_1\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_6\\mod_1\\anim\\{}".format(i))).convert_alpha()
			self.player_gun6_mod1_anim.append(img)

		self.player_gun6_mod2 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_6\\mod_2\\gun6_mod2.png")).convert_alpha()
		self.player_gun6_mod2_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_6\\mod_2\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_6\\mod_2\\anim\\{}".format(i))).convert_alpha()
			self.player_gun6_mod2_anim.append(img)

		self.player_gun6_mod3 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_6\\mod_3\\gun6_mod3.png")).convert_alpha()
		self.player_gun6_mod3_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_6\\mod_3\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_6\\mod_3\\anim\\{}".format(i))).convert_alpha()
			self.player_gun6_mod3_anim.append(img)

		self.player_gun7_mod1 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_7\\mod_1\\gun7_mod1.png")).convert_alpha()
		self.player_gun7_mod1_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_7\\mod_1\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_7\\mod_1\\anim\\{}".format(i))).convert_alpha()
			self.player_gun7_mod1_anim.append(img)

		self.player_gun7_mod2 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_7\\mod_2\\gun7_mod2.png")).convert_alpha()
		self.player_gun7_mod2_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_7\\mod_2\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_7\\mod_2\\anim\\{}".format(i))).convert_alpha()
			self.player_gun7_mod2_anim.append(img)

		self.player_gun7_mod3 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_7\\mod_3\\gun7_mod3.png")).convert_alpha()
		self.player_gun7_mod3_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_7\\mod_3\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_7\\mod_3\\anim\\{}".format(i))).convert_alpha()
			self.player_gun7_mod3_anim.append(img)

		self.player_gun8_mod1 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_8\\mod_1\\gun8_mod1.png")).convert_alpha()
		self.player_gun8_mod1_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_8\\mod_1\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_8\\mod_1\\anim\\{}".format(i))).convert_alpha()
			self.player_gun8_mod1_anim.append(img)

		self.player_gun8_mod2 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_8\\mod_2\\gun8_mod2.png")).convert_alpha()
		self.player_gun8_mod2_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_8\\mod_2\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_8\\mod_2\\anim\\{}".format(i))).convert_alpha()
			self.player_gun8_mod2_anim.append(img)

		self.player_gun8_mod3 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_8\\mod_3\\gun8_mod3.png")).convert_alpha()
		self.player_gun8_mod3_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_8\\mod_3\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_8\\mod_3\\anim\\{}".format(i))).convert_alpha()
			self.player_gun8_mod3_anim.append(img)

		self.player_gun9_mod1 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_9\\mod_1\\gun9_mod1.png")).convert_alpha()
		self.player_gun9_mod1_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_9\\mod_1\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_9\\mod_1\\anim\\{}".format(i))).convert_alpha()
			self.player_gun9_mod1_anim.append(img)

		self.player_gun9_mod2 = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_9\\mod_2\\gun9_mod2.png")).convert_alpha()
		self.player_gun9_mod2_anim = []
		for i in listdir(path.join(this_directory, "g\\player_guns\\gun_9\\mod_2\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\player_guns\\gun_9\\mod_2\\anim\\{}".format(i))).convert_alpha()
			self.player_gun9_mod2_anim.append(img)

		self.info_panel = pygame.image.load(path.join(this_directory, "g\\gui\\info_panel\\info_panel.png")).convert_alpha()

		self.mechanic_window_fon = pygame.image.load(path.join(this_directory, "g\\gui\\mechanic_window\\fon.png")).convert_alpha()
		self.mechanic_window_info_panel = pygame.image.load(path.join(this_directory, "g\\gui\\mechanic_window\\player_info.png")).convert_alpha()
		self.mechanic_window_exit_button = pygame.image.load(path.join(this_directory, "g\\gui\\mechanic_window\\exit_button.png")).convert_alpha()

		self.enemy_plate_1 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\enemy_plate\\enemy_plate1.png")).convert_alpha()
		self.enemy_plate_2 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\enemy_plate\\enemy_plate2.png")).convert_alpha()
		self.enemy_plate_3 = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\enemy_plate\\enemy_plate3.png")).convert_alpha()

		self.highteck_up_plate = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\tehnology_up_plate\\plate.png")).convert_alpha()
		self.highteck_up_plate_anim = []
		for i in listdir(path.join(this_directory, "g\\matrix_plates\\tehnology_up_plate\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\tehnology_up_plate\\anim\\{}".format(i))).convert_alpha()
			self.highteck_up_plate_anim.append(img)

		self.compas_hiden_mech_plate = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\compas_hiden_mech\\plate.png")).convert_alpha()
		self.compas_hiden_mech_plate_anim = []
		for i in listdir(path.join(this_directory, "g\\matrix_plates\\compas_hiden_mech\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\compas_hiden_mech\\anim\\{}".format(i))).convert_alpha()
			self.compas_hiden_mech_plate_anim.append(img)

		self.change_lvl_plate = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\change_lvl_plate\\plate.png")).convert_alpha()
		self.change_lvl_plate_anim = []
		for i in listdir(path.join(this_directory, "g\\matrix_plates\\change_lvl_plate\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\matrix_plates\\change_lvl_plate\\anim\\{}".format(i))).convert_alpha()
			self.change_lvl_plate_anim.append(img)


		self.compas = pygame.image.load(path.join(this_directory, "g\\hitec\\compas\\compas.png")).convert_alpha()
		self.compas_background = pygame.image.load(path.join(this_directory, "g\\hitec\\compas\\background.png")).convert_alpha()
		self.compas_init = []
		for i in listdir(path.join(this_directory, "g\\hitec\\compas\\init_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\hitec\\compas\\init_anim\\{}".format(i))).convert_alpha()
			self.compas_init.append(img)
		self.compas_anim = []
		for i in listdir(path.join(this_directory, "g\\hitec\\compas\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\hitec\\compas\\anim\\{}".format(i))).convert_alpha()
			self.compas_anim.append(img)

		self.hable = pygame.image.load(path.join(this_directory, "g\\hitec\\hable\\hable.png")).convert_alpha()
		self.hable_background = pygame.image.load(path.join(this_directory, "g\\hitec\\hable\\background.png")).convert_alpha()
		self.hable_init = []
		for i in listdir(path.join(this_directory, "g\\hitec\\hable\\init_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\hitec\\hable\\init_anim\\{}".format(i))).convert_alpha()
			self.hable_init.append(img)
		self.hable_anim = []
		for i in listdir(path.join(this_directory, "g\\hitec\\hable\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\hitec\\hable\\anim\\{}".format(i))).convert_alpha()
			self.hable_anim.append(img)

		self.boosted_engine = pygame.image.load(path.join(this_directory, "g\\hitec\\boosted_engine\\boosted_engine.png")).convert_alpha()
		self.boosted_engine_background = pygame.image.load(path.join(this_directory, "g\\hitec\\boosted_engine\\background.png")).convert_alpha()
		self.boosted_engine_init = []
		for i in listdir(path.join(this_directory, "g\\hitec\\boosted_engine\\init_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\hitec\\boosted_engine\\init_anim\\{}".format(i))).convert_alpha()
			self.boosted_engine_init.append(img)
		self.boosted_engine_anim = []
		for i in listdir(path.join(this_directory, "g\\hitec\\boosted_engine\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\hitec\\boosted_engine\\anim\\{}".format(i))).convert_alpha()
			self.boosted_engine_anim.append(img)

		self.green_energy = pygame.image.load(path.join(this_directory, "g\\hitec\\green_energy\\green_energy.png")).convert_alpha()
		self.green_energy_background = pygame.image.load(path.join(this_directory, "g\\hitec\\green_energy\\background.png")).convert_alpha()
		self.green_energy_init = []
		for i in listdir(path.join(this_directory, "g\\hitec\\green_energy\\init_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\hitec\\green_energy\\init_anim\\{}".format(i))).convert_alpha()
			self.green_energy_init.append(img)
		self.green_energy_anim = []
		for i in listdir(path.join(this_directory, "g\\hitec\\green_energy\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\hitec\\green_energy\\anim\\{}".format(i))).convert_alpha()
			self.green_energy_anim.append(img)

		self.polimerization = pygame.image.load(path.join(this_directory, "g\\hitec\\polimerization\\polimerization.png")).convert_alpha()
		self.polimerization_background = pygame.image.load(path.join(this_directory, "g\\hitec\\polimerization\\background.png")).convert_alpha()
		self.polimerization_init = []
		for i in listdir(path.join(this_directory, "g\\hitec\\polimerization\\init_anim")):
			img = pygame.image.load(path.join(this_directory, "g\\hitec\\polimerization\\init_anim\\{}".format(i))).convert_alpha()
			self.polimerization_init.append(img)
		self.polimerization_anim = []
		for i in listdir(path.join(this_directory, "g\\hitec\\polimerization\\anim")):
			img = pygame.image.load(path.join(this_directory, "g\\hitec\\polimerization\\anim\\{}".format(i))).convert_alpha()
			self.polimerization_anim.append(img)

		self.hp = pygame.Surface((20,20))
		self.hp.fill((255,0,0))

		self.main_menu_img = pygame.image.load(path.join(this_directory, "g\\main_menu\\main_menu.png")).convert_alpha()

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
	#font_name = pygame.font.match_font('font.ttf')
	font = pygame.font.Font(path.join(this_directory, "font.ttf"), size)
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


def create_lvl_matrix(lvl_x, lvl_y, lvl_num):

	lvl = []

	change_lvl_randnum = random.randint(0, 3)
	change_lvl_plate_positions =  [(1, 1), (1, lvl_y - 2), (lvl_x - 2, 1), (lvl_x - 2, lvl_y - 2)]#[(0, 0), (0, 0), (0, 0), (0, 0)] [(1, 1), (1, lvl_y - 2), (lvl_x - 2, 1), (lvl_x - 2, lvl_y - 2)]

	player_vis_lvl = []

	for i in range(lvl_y):
		line = []
		for i in range(lvl_x):
			line.append(9)
		player_vis_lvl.append(line)

	for i in range(0,lvl_y):
		line = []
		for i in range(0,lvl_x):
			line.append(0)
		lvl.append(line)

	y = 0
	plates_1_2_3_limit = 2
	plates_highteck_limit = 1
	for line in lvl:
		x = 0
		for element in line:
			randnum = random.randint(0, 100)
			#if randnum > 80:
			#	lvl[y][x] = (1, 2, 3, 4, 5, 6, 7, 8, 9)#random.choice([(0, 0), (random.randint(0, 2), random.randint(0, 2) )])

			if randnum > 96 and plates_1_2_3_limit > 0:
				lvl[y][x] = 3
				plates_1_2_3_limit -= 1

			elif 92 < randnum < 96 and plates_1_2_3_limit > 0:
				lvl[y][x] = 2
				plates_1_2_3_limit -= 1

			elif  86 < randnum < 92 and plates_1_2_3_limit > 0:
				plates_1_2_3_limit -= 1
				lvl[y][x] = 1

			randnum = random.randint(0, 100)

			if randnum > 90 and plates_highteck_limit > 0:
				plates_highteck_limit -= 1
				lvl[y][x] = 12

			x += 1
		print(line)
		plates_1_2_3_limit = 2
		y += 1
	
	if lvl_num == 1 or lvl_num == 2:
		lvl[change_lvl_plate_positions[change_lvl_randnum][0]][change_lvl_plate_positions[change_lvl_randnum][1]] = 11

	startpos_y = int(lvl_y / 2)
	lvl[startpos_y][int(lvl_x / 2)] = "p"
	player_vis_lvl[startpos_y][int(lvl_x / 2)] = "p"

	if lvl_num == 3:
		planets_positions = [(random.randint(1, 3), random.randint(1, 3)), (random.randint(1, 3), random.randint(lvl_y - 4, lvl_y - 2)), (random.randint(lvl_x-4, lvl_x-2), random.randint(1, 3)), (random.randint(lvl_x-4, lvl_x-2), random.randint(lvl_y-4, lvl_y-2)),]

		coordinates = random.choice(planets_positions)
		planets_positions.remove(coordinates)
		lvl[coordinates[0]][coordinates[1]] = 18
		coordinates = random.choice(planets_positions)
		planets_positions.remove(coordinates)
		lvl[coordinates[0]][coordinates[1]] = 19
		coordinates = random.choice(planets_positions)
		planets_positions.remove(coordinates)
		lvl[coordinates[0]][coordinates[1]] = 20

	y = 0
	for line in lvl:
		x = 0
		for element in line:
			if element == "p":
				lvl[y][x+1] = 0
				lvl[y][x-1] = 0
				lvl[y-1][x] = 0
				lvl[y+1][x] = 0
				lvl[y-1][x-1] = 0
				lvl[y-1][x+1] = 0
				lvl[y+1][x-1] = 0
				lvl[y+1][x+1] = 0

				lvl[y][x+2] = 0
				lvl[y][x-2] = 0
				lvl[y-2][x] = 0
				lvl[y+2][x] = 0
				lvl[y-2][x-2] = 0
				lvl[y-2][x+2] = 0
				lvl[y+2][x-2] = 0
				lvl[y+2][x+2] = 0
				lvl[y-2][x-1] = 0
				lvl[y-2][x+1] = 0
				lvl[y+2][x-1] = 0
				lvl[y+2][x+1] = 0
				lvl[y][x-2] = 0
				lvl[y][x+2] = 0
				lvl[y+2][x] = 0
				lvl[y-2][x] = 0
			
			if element == 11:
				lvl[y][x+1] = 0
				lvl[y][x-1] = 0
				lvl[y-1][x] = 0
				lvl[y+1][x] = 0
				lvl[y-1][x-1] = 0
				lvl[y-1][x+1] = 0
				lvl[y+1][x-1] = 0
				lvl[y+1][x+1] = 0

			x += 1
		y += 1

	y = 0
	for line in lvl:
		x = 0
		for element in line:
			if element == 11:
				if x + 1 <= lvl_x - 1 and 0 <= y <= lvl_y - 1:
					lvl[y][x+1] = (7, 8, 9)

				if x - 1 >= 0 and 0 <= y <= lvl_y - 1:
					lvl[y][x-1] = (7, 8, 9)

				if y + 1 <= lvl_y - 1 and 0 <= x <= lvl_x - 1:
					lvl[y+1][x] = (7, 8, 9)

				if y - 1 >= 0 and 0 <= x <= lvl_x - 1:
					lvl[y-1][x] = (7, 8, 9)

			if element == 1:
				if x + 1 <= lvl_x - 1 and 0 <= y <= lvl_y - 1:
					lvl[y][x+1] = (1, 2, 3)

				if x - 1 >= 0 and 0 <= y <= lvl_y - 1:
					lvl[y][x-1] = (1, 2, 3)

				if y + 1 <= lvl_y - 1 and 0 <= x <= lvl_x - 1:
					lvl[y+1][x] = (1, 2, 3)

				if y - 1 >= 0 and 0 <= x <= lvl_x - 1:
					lvl[y-1][x] = (1, 2, 3)

			if element == 2:
				if x + 1 <= lvl_x - 1 and 0 <= y <= lvl_y - 1:
					lvl[y][x+1] = (4, 5, 6)

				if x - 1 >= 0 and 0 <= y <= lvl_y - 1:
					lvl[y][x-1] = (4, 5, 6)

				if y + 1 <= lvl_y - 1 and 0 <= x <= lvl_x - 1:
					lvl[y+1][x] = (4, 5, 6)
				if y - 1 >= 0 and 0 <= x <= lvl_x - 1:
					lvl[y-1][x] = (4, 5, 6)

			if element == 3:
				if x + 1 <= lvl_x - 1 and 0 <= y <= lvl_y - 1:
					lvl[y][x+1] = (7, 8, 9)

				if x - 1 >= 0 and 0 <= y <= lvl_y - 1:
					lvl[y][x-1] = (7, 8, 9)

				if y + 1 <= lvl_y - 1 and 0 <= x <= lvl_x - 1:
					lvl[y+1][x] = (7, 8, 9)

				if y - 1 >= 0 and 0 <= x <= lvl_x - 1:
					lvl[y-1][x] = (7, 8, 9)

			x += 1
		y += 1

	return(lvl, player_vis_lvl)

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

			if element == 11:
				index = 0
				for i in owner.matrix_plates_list:
					if type(i) != img_plate_change_lvl and i.rect.x == x and i.rect.y == y:
						del owner.matrix_plates_list[index]
						plate = img_plate_change_lvl(x, y)
						owner.matrix_plates_list.append(plate)

					index += 1

			if element == 12:
				index = 0
				for i in owner.matrix_plates_list:
					if type(i) != highteck_up_plate and i.rect.x == x and i.rect.y == y:
						del owner.matrix_plates_list[index]
						plate = highteck_up_plate(x, y)
						owner.matrix_plates_list.append(plate)

					index += 1

			if element == 13:
				index = 0
				for i in owner.matrix_plates_list:
					if type(i) != compas_hiden_plate and i.rect.x == x and i.rect.y == y:
						del owner.matrix_plates_list[index]
						plate = compas_hiden_plate(x, y)
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

	lenx_matrix = owner.matrix_x - 1
	leny_matrix = owner.matrix_y - 1
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

				if x == 0 and y == 0:
					plate = img_plate_border(x-16, y - 16, 5)
					owner.matrix_plates_list.append(plate)

				if x == 0 and y == leny_matrix * 16:
					plate = img_plate_border(x - 16, y + 16, 7)
					owner.matrix_plates_list.append(plate)

				if x  == lenx_matrix * 16  and y == 0:
					plate = img_plate_border(x + 16, y - 16, 6)
					owner.matrix_plates_list.append(plate)

				if x == lenx_matrix * 16 and y == leny_matrix * 16:
					plate = img_plate_border(x + 16, y + 16, 8)
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
	(gg.matrix_plate9_3, gg.matrix_plate9_3_anim), (gg.matrix_plate9_4, gg.matrix_plate9_4_anim), 
	(gg.matrix_plate9_5, gg.matrix_plate9_5_anim), (gg.matrix_plate9_6, gg.matrix_plate9_6_anim), 
	(gg.matrix_plate9_7, gg.matrix_plate9_7_anim), (gg.matrix_plate9_8, gg.matrix_plate9_8_anim)]

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

class compas_hiden_plate(pygame.sprite.Sprite):
	def __init__(self, x, y):

		pygame.sprite.Sprite.__init__(self)
		self.image = gg.compas_hiden_mech_plate
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.anim = gg.compas_hiden_mech_plate_anim
		self.anim_len = len(self.anim)
		self.is_anim = False
		self.curent_anim_frame = 0
		self.frame_timer = 0

		self.anim_reload = random.randint(0, 500)
		self.anim_reload_timer = 0



	def update(self):
		if self.anim_reload_timer > self.anim_reload and self.is_anim == False:
			self.is_anim = True
			self.anim_reload = random.randint(100, 1300)
			self.anim_reload_timer = 0
		else:
			self.anim_reload_timer += 1

		if self.is_anim == True:
			if self.frame_timer > 13:
				self.image = self.anim[self.curent_anim_frame]
				self.curent_anim_frame += 1
				self.frame_timer = 0
				if self.anim_len <= self.curent_anim_frame:
					self.curent_anim_frame = 0
					self.is_anim = False
			else:
				self.frame_timer += 1


class highteck_up_plate(pygame.sprite.Sprite):
	def __init__(self, x, y):

		pygame.sprite.Sprite.__init__(self)
		self.image =  gg.highteck_up_plate
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.anim = gg.highteck_up_plate_anim
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
			if self.frame_timer > 4:
				self.image = self.anim[self.curent_anim_frame]
				self.curent_anim_frame += 1
				self.frame_timer = 0
				if self.anim_len <= self.curent_anim_frame:
					self.curent_anim_frame = 0
					self.is_anim = False
			else:
				self.frame_timer += 1
		
class img_plate_with_enemys(pygame.sprite.Sprite):
	fog_imgs = [gg.enemy_plate_1, gg.enemy_plate_2, gg.enemy_plate_3]
	def __init__(self, x, y, tuple_enemys_id):
		self.fog_image = random.choice(img_plate_with_enemys.fog_imgs)
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((16,16))
		#self.image.fill((255,255,255))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.enemys = tuple_enemys_id

		self.enemys_imgs = []

		self.blit_imgs = []

		for i in game.all_enemys:
			for x in self.enemys:
				if i.enemy_id == x:
					self.enemys_imgs.append(i.icon)

		self.spawn_enemy_timer = 30

	def update(self):
		self.image = pygame.Surface((16, 16)).convert_alpha()
		self.image.fill((13, 13, 35))
		if self.spawn_enemy_timer > 30:
			enemys = plate_with_enemys_enemy(random.randint(-2, 14), random.choice(self.enemys_imgs))
			self.spawn_enemy_timer = 0
			self.blit_imgs.append(enemys)
		else:
			self.spawn_enemy_timer += 1

		for i in self.blit_imgs:
			i.update()
			self.image.blit(i.image, (i.rect.x, i.rect.y))
			if i.rect.left > 17 or i.rect.right < -1:
				self.blit_imgs.remove(i)

		self.image.blit(self.fog_image, (0,0))

class plate_with_enemys_enemy(pygame.sprite.Sprite):
	def __init__(self, y, image):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.transform.scale(image, (8, 8))
		self.image = image #pygame.transform.rotate(image, 90)
		self.rect = self.image.get_rect()
		self.rect.x = random.choice([-8, 16])
		self.rect.y = y
		self.x = self.rect.x
		self.y = self.rect.y

		self.speed = 0
		if self.rect.x == -8:
			self.image = pygame.transform.rotate(image, 90)
			self.speed = 0.2
		elif self.rect.x == 16:
			self.speed = -0.2
			self.image =  pygame.transform.rotate(image, -90)

		self.alpha = 0
		print("created")

	def update(self):
		if self.alpha <= 255 and self.rect.left <= 0 and self.speed > 0:
			self.alpha += 5
			if self.alpha > 255:
				self.alpha = 255
			self.image.set_alpha(self.alpha)
		if self.rect.right >= 17 and self.speed > 0:
			self.alpha -= 20
			if self.alpha < 0:
				self.alpha = 0
			self.image.set_alpha(self.alpha)

		if self.alpha <= 255 and self.rect.right >=16 and self.speed < 0:
			self.alpha += 5
			if self.alpha > 255:
				self.alpha = 255
			self.image.set_alpha(self.alpha)
		if self.rect.left < -1 and self.speed < 0:
			self.alpha -= 20
			if self.alpha < 0:
				self.alpha = 0
			self.image.set_alpha(self.alpha)


		self.x += self.speed
		self.rect.x = self.x



class img_plate_change_lvl(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = gg.change_lvl_plate
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.anim = gg.change_lvl_plate_anim
		self.anim_len = len(self.anim)
		self.is_anim = False
		self.curent_anim_frame = 0
		self.frame_timer = 0

		self.anim_reload = random.randint(0, 300)
		self.anim_reload_timer = 0
		

	def update(self):
		if self.anim_reload_timer > self.anim_reload and self.is_anim == False:
			self.is_anim = True
			self.anim_reload = random.randint(120, 140)
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

class img_planet_plate(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = gg.player
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self):
		pass


class mechanic_plate(pygame.sprite.Sprite):
	def __init__(self, x, y, qual):
		pygame.sprite.Sprite.__init__(self)
		self.image = gg.matrix_plate_1_2_3
		#self.image.fill((255,255,0))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.anim = gg.matrix_plate_1_2_3_anim
		self.anim_len = len(self.anim)
		self.is_anim = False
		self.curent_anim_frame = 0
		self.frame_timer = 0

		self.anim_reload = random.randint(0, 300)
		self.anim_reload_timer = 0

		self.qualification = qual - 1

	def update(self):
		if self.anim_reload_timer > self.anim_reload and self.is_anim == False:
			self.is_anim = True
			self.anim_reload = random.randint(100, 800)
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

		if self.kill == True:
			self.alpha -= 40
			if self.alpha < 0:
				self.owner.matrix_plates_list.remove(self)
				self.alpha = 0
			self.image.set_alpha(self.alpha)


class img_plate_border(pygame.sprite.Sprite):
	img_left = [gg.matrix_plate_9_border_left1]
	img_right = [gg.matrix_plate_9_border_right1]
	img_down = [gg.matrix_plate_9_border_down1]
	img_up = [gg.matrix_plate_9_border_up1]
	img_left_up = [gg.matrix_plate_9_border_left_up]
	img_right_up = [gg.matrix_plate_9_border_right_up]
	img_left_down = [gg.matrix_plate_9_border_left_down]
	img_right_down = [gg.matrix_plate_9_border_right_down]
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
		if self.left_right_down_up == 5:
			self.image = img_plate_border.img_left_up[0]
		if self.left_right_down_up == 6:
			self.image = img_plate_border.img_right_up[0]
		if self.left_right_down_up == 7:
			self.image = img_plate_border.img_left_down[0]
		if self.left_right_down_up == 8:
			self.image = img_plate_border.img_right_down[0]

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

class info_panel():
	def __init__(self):
		self.image = gg.info_panel.copy()
		self.rect = self.image.get_rect()
		post_processing_m.objects.append(self)

	def update(self):
		self.image = gg.info_panel.copy()
		self.image.blit(game.player_gun.all_img[game.player_gun_mod], (162, 16))
		draw_text(self.image, str(game.player_health), 38, 32, 36 ,(172, 176, 207))
		draw_text(self.image, str(game.resours1), 32, 41, 115 ,(172, 176, 207))
		draw_text(self.image, str(game.resours2), 32, 105, 115 ,(172, 176, 207))
		draw_text(self.image, str(game.resours3), 32, 170, 115 ,(172, 176, 207))
		draw_text(self.image, str(game.fuel), 32, 100, 36 ,(172, 176, 207))
		game_surface.blit(self.image, (600 - self.rect.width, 0))


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

		self.centred_point_x = 300
		self.centred_point_y = 200

		#for i in self.owner.matrix_plates_list:
		#	i.rect.x += self.speedx
		#	i.rect.y += self.speedy


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
		self.scale_coefficient = 1.5
		post_processing_m.objects.append(self)


	def update(self):
		global game_surface
		new_width = int(width * self.scale_coefficient)
		new_height = int(height * self.scale_coefficient)

		game_surface.blit(pygame.transform.scale(game_surface, (new_width, new_height)), (-(int((new_width-width)/2)),-(int((new_height-height)/2))))

		if self.scale_coefficient < 1:
			self.scale_coefficient = 1
		if self.scale_coefficient > 2.5:
			self.scale_coefficient = 2.5


class action_lvl():
	def __init__(self, owner, enemys):
		black_off()
		self.enemys = enemys
		self.owner = owner

		self.player = player(self.owner.player_gun, self.owner.player_gun_mod, self.owner.player_health)

		self.enemy_m = enemy_manager(enemys, self)
		self.hp_m = hp_manager(self)

		updateble_objects_m.objects.append(self)

		self.fuel_reward = 0

		if enemy_1 in self.enemys or enemy_2 in self.enemys or enemy_3 in self.enemys:
			self.fuel_reward = 2
		if enemy_4 in self.enemys or enemy_5 in self.enemys or enemy_6 in self.enemys:
			self.fuel_reward = 3
		if enemy_7 in self.enemys or enemy_8 in self.enemys or enemy_9 in self.enemys:
			self.fuel_reward = 3

		if game.highteck_ups[0] == True:
			self.fuel_reward += 2

	def update(self):
		press = pygame.key.get_pressed()
		if self.player.health <= 0:
			self.kill()

	def kill(self):
		if game.highteck_ups[1] == True:
			if enemy_7 in self.enemys or enemy_8 in self.enemys or enemy_9 in self.enemys:
				game.resours3 += 1

		game.fuel += self.fuel_reward

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

		self.speedx_max = 2
		self.speedy_max = 2
		self.speedx_now = 2
		self.speedy_now = 0

		if game.highteck_ups[4] == True:
			self.speedy_max = 3
			self.speedx_max = 3


		self.acceleration_x = 0.5
		self.acceleration_y = 0.5

		self.move_up = False
		self.move_down = False
		self.move_left = False
		self.move_right = False

		all_sprites.add(self)

	def update(self):
		#self.health = 3 #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

		press = pygame.key.get_pressed()
		if press[pygame.K_w]:
			self.move_up = True
		if press[pygame.K_s]:
			self.move_down = True
		if press[pygame.K_d]:
			self.move_right = True
		if press[pygame.K_a]:
			self.move_left = True

		if self.move_up:
			if -self.speedy_max < self.speedy_now:
				self.speedy_now -= self.acceleration_y
		else:
			if self.speedy_now < 0:
				self.speedy_now += self.acceleration_y
		if self.move_down:
			if self.speedy_max > self.speedy_now:
				self.speedy_now += self.acceleration_y
		else:
			if self.speedy_now > 0:
				self.speedy_now -= self.acceleration_y
		if self.move_right:
			if self.speedx_max > self.speedx_now:
				self.speedx_now += self.acceleration_x
		else:
			if self.speedx_now > 0:
				self.speedx_now -= self.acceleration_x
		if self.move_left:
			if -self.speedx_max < self.speedx_now:
				self.speedx_now -= self.acceleration_x
		else:
			if self.speedx_now < 0:
				self.speedx_now += self.acceleration_x

		self.move_up = False
		self.move_down = False
		self.move_left = False
		self.move_right = False
		
		self.rect.x += self.speedx_now
		self.rect.y += self.speedy_now

		self.image = self.orig_img.copy()
		self.gun.update()


		if self.rect.top < 193:
			self.rect.top = 193

		if self.rect.bottom > 360:
			self.rect.bottom = 360

		if self.rect.left < 0:
			self.rect.left = 0

		if self.rect.right > 600:
			self.rect.right = 600

class gun(pygame.sprite.Sprite):
	obj_type = "gun"
	max_mod_number = 0 #3 in fact, but 3 - 1 = 2
	q1_mech = [0,1,2]
	q2_mech = [0,1,2]
	q3_mech = [0,1,2]
	all_mechs = [q1_mech, q2_mech, q3_mech]

	mod1_cost = (100,100,200)
	all_mod_cost = [mod1_cost]


	img_mod1 = gg.player_gun1_mod1
	anim_mod1 = gg.player_gun1_mod1_anim

	all_img = [img_mod1]
	all_anims = [anim_mod1]

	def __init__(self, owner, mod):
		pygame.sprite.Sprite.__init__(self)

		self.mod = mod

		self.max_mod_number = 0 #3 in fact, but 3-1, becouse index in python work like: list[0] - its a first element 
								#													   list[1] - its a second element


	#	if self.mod > self.max_mod_number:
	#		self.mod = self.max_mod_number

		self.image = gun.all_img[self.mod]
		self.anim = gun.all_anims[self.mod]

		self.mod1_characteristics = [3, 3, 10, (2,3), 6, 100, (100,100,200)]    #index: 0 - damage, 1 - bullet_speed, 2 - clip_size, 3 - size (x,y), 4 - delay, 5 - reload, 6 resourses_cost

		self.all_mod_characteristics = [self.mod1_characteristics]
		self.characteristics = self.all_mod_characteristics[self.mod]

		self.rect = self.image.get_rect()
		self.owner = owner

		self.shoot_delay_timer = 0
		self.in_clip = self.mod1_characteristics[2]
		self.clip_reload_timer = 0
		self.clip_reload = self.mod1_characteristics[5]

		self.is_shoot_anim = False
		self.shoot_anim_len = len(self.anim)
		self.to_shoot_frame = 0
		self.curent_shoot_anim_frame = 0
		self.shoot_frame_timer = 0

		self.to_shoot = False

		self.offset1_x = 3
		self.offset1_y = 13
		self.offset2_x = 26
		self.offset2_y = 13

	def update(self):

		self.owner.image.blit(self.image, (0,0))
		press = pygame.key.get_pressed()
		if press[pygame.K_SPACE] and self.shoot_delay_timer > self.characteristics[4] and self.is_shoot_anim == False and self.in_clip > 0:
			self.to_shoot = True
			self.shoot_delay_timer = 0
			self.is_shoot_anim = True

		if self.shoot_delay_timer <= self.characteristics[4]:
			self.shoot_delay_timer += 1

		if self.to_shoot and self.curent_shoot_anim_frame == self.to_shoot_frame:
			self.in_clip -=1
			self.shoot()
			self.to_shoot = False

		if self.is_shoot_anim:
			if self.shoot_frame_timer > self.characteristics[4] / self.shoot_anim_len:
				self.image = self.anim[self.curent_shoot_anim_frame]
				self.curent_shoot_anim_frame += 1
				self.shoot_frame_timer = 0
				if self.shoot_anim_len <= self.curent_shoot_anim_frame:
					self.curent_shoot_anim_frame = 0
					self.is_shoot_anim = False

			else:
				self.shoot_frame_timer += 1

		if self.in_clip <= 0:
			if self.clip_reload_timer > self.clip_reload:
				self.in_clip = self.characteristics[2]
				self.clip_reload_timer = 0
			else:
				self.clip_reload_timer += 1


	def shoot(self):
		default_bullet(self.characteristics[0], self.characteristics[1], self.characteristics[3], self.owner.rect.x + self.offset1_x, self.owner.rect.y + self.offset1_y)
		default_bullet(self.characteristics[0], self.characteristics[1], self.characteristics[3], self.owner.rect.x + self.offset2_x, self.owner.rect.y + self.offset2_y)


class gun1(gun):

	max_mod_number = 2 #3 in fact, but 3 - 1 = 2
	q1_mech = [0,1,2]
	q2_mech = [0,1,2]
	q3_mech = [0,1,2]
	all_mechs = [q1_mech, q2_mech, q3_mech]

	img_mod1 = gg.player_gun1_mod1
	anim_mod1 = gg.player_gun1_mod1_anim
	img_mod2 = gg.player_gun1_mod2
	anim_mod2 = gg.player_gun1_mod2_anim
	img_mod3 = gg.player_gun1_mod3
	anim_mod3 = gg.player_gun1_mod3_anim

	mod1_cost = (100,100,200)
	mod2_cost = (100,100,200)
	mod3_cost = (100,100,200)

	all_mod_cost = [mod1_cost, mod2_cost, mod3_cost]


	all_img = [img_mod1, img_mod2, img_mod3]
	all_anims = [anim_mod1, anim_mod2, anim_mod3]

	def __init__(self, owner, mod):
		pygame.sprite.Sprite.__init__(self)

		self.mod = mod

		self.max_mod_number = 2 #3 in fact, but 3-1, becouse index in python work like: list[0] - its a first element 
								#													   list[1] - its a second element


	#	if self.mod > self.max_mod_number:
	#		self.mod = self.max_mod_number

		self.image = gun1.all_img[self.mod]
		self.anim = gun1.all_anims[self.mod]

		self.mod1_characteristics = [3, 3, 10, (2,3), 6, 100, (100,100,200)]    #index: 0 - damage, 1 - bullet_speed, 2 - clip_size, 3 - size (x,y), 4 - delay
		self.mod2_characteristics = [3, 4, 14, (2,3), 6, 100, (100,100,200)]
		self.mod3_characteristics = [4, 4, 16, (2,3), 6, 100, (100,100,200)]

		self.all_mod_characteristics = [self.mod1_characteristics, self.mod2_characteristics, self.mod3_characteristics]
		self.characteristics = self.all_mod_characteristics[self.mod]

		self.rect = self.image.get_rect()
		self.owner = owner

		self.shoot_delay_timer = 0

		self.shoot_delay_timer = 0
		self.in_clip = self.mod1_characteristics[2]
		self.clip_reload_timer = 0
		self.clip_reload = self.mod1_characteristics[5]

		self.is_shoot_anim = False
		self.shoot_anim_len = len(self.anim)
		self.to_shoot_frame = 0
		self.curent_shoot_anim_frame = 0
		self.shoot_frame_timer = 0

		self.to_shoot = False

		self.offset1_x = 3
		self.offset1_y = 13
		self.offset2_x = 26
		self.offset2_y = 13

class gun2(gun):

	max_mod_number = 2 #3 in fact, but 3 - 1 = 2
	q1_mech = [0,1,2]
	q2_mech = [0,1,2]
	q3_mech = [0,1,2]
	all_mechs = [q1_mech, q2_mech, q3_mech]

	img_mod1 = gg.player_gun2_mod1
	anim_mod1 = gg.player_gun2_mod1_anim
	img_mod2 = gg.player_gun2_mod2
	anim_mod2 = gg.player_gun2_mod2_anim
	img_mod3 = gg.player_gun2_mod3
	anim_mod3 = gg.player_gun2_mod3_anim

	all_img = [img_mod1, img_mod2, img_mod3]
	all_anims = [anim_mod1, anim_mod2, anim_mod3]

	mod1_cost = (100,100,200)
	mod2_cost = (100,100,200)
	mod3_cost = (100,100,200)

	all_mod_cost = [mod1_cost, mod2_cost, mod3_cost]

	def __init__(self, owner, mod):
		pygame.sprite.Sprite.__init__(self)

		self.mod = mod

		self.max_mod_number = 2 #3 in fact, but 3-1, becouse index in python work like: list[0] - its a first element 
								#													   list[1] - its a second element


	#	if self.mod > self.max_mod_number:
	#		self.mod = self.max_mod_number

		self.image = gun2.all_img[self.mod]
		self.anim = gun2.all_anims[self.mod]

		self.mod1_characteristics = [3, 3, 10, (2,3), 6, 100, (100,100,200)]    #index: 0 - damage, 1 - bullet_speed, 2 - clip_size, 3 - size (x,y), 4 - delay
		self.mod2_characteristics = [3, 4, 14, (2,3), 6, 100, (100,100,200)]
		self.mod3_characteristics = [4, 4, 16, (2,3), 6, 100, (100,100,200)]

		self.all_mod_characteristics = [self.mod1_characteristics, self.mod2_characteristics, self.mod3_characteristics]
		self.characteristics = self.all_mod_characteristics[self.mod]

		self.rect = self.image.get_rect()
		self.owner = owner

		self.shoot_delay_timer = 0

		self.shoot_delay_timer = 0
		self.in_clip = self.mod1_characteristics[2]
		self.clip_reload_timer = 0
		self.clip_reload = self.mod1_characteristics[5]

		self.is_shoot_anim = False
		self.shoot_anim_len = len(self.anim)
		self.to_shoot_frame = 0
		self.curent_shoot_anim_frame = 0
		self.shoot_frame_timer = 0

		self.to_shoot = False

		self.offset1_x = 12
		self.offset1_y = 9
		self.offset2_x = 18
		self.offset2_y = 9

class gun3(gun):

	max_mod_number = 3 #3 in fact, but 3 - 1 = 2
	q1_mech = [0,1,2,3]
	q2_mech = [0,1,2,3]
	q3_mech = [0,1,2,3]
	all_mechs = [q1_mech, q2_mech, q3_mech]

	img_mod1 = gg.player_gun3_mod1
	anim_mod1 = gg.player_gun3_mod1_anim
	img_mod2 = gg.player_gun3_mod2
	anim_mod2 = gg.player_gun3_mod2_anim
	img_mod3 = gg.player_gun3_mod3
	anim_mod3 = gg.player_gun3_mod3_anim
	img_mod4 = gg.player_gun3_mod4
	anim_mod4 = gg.player_gun3_mod4_anim

	all_img = [img_mod1, img_mod2, img_mod3, img_mod3]
	all_anims = [anim_mod1, anim_mod2, anim_mod3, anim_mod4]

	mod1_cost = (100,100,200)
	mod2_cost = (100,100,200)
	mod3_cost = (100,100,200)
	mod4_cost = (100,100,200)

	all_mod_cost = [mod1_cost, mod2_cost, mod3_cost, mod4_cost]

	def __init__(self, owner, mod):
		pygame.sprite.Sprite.__init__(self)

		self.mod = mod

		self.max_mod_number = 3 #3 in fact, but 3-1, becouse index in python work like: list[0] - its a first element 
								#													   list[1] - its a second element


	#	if self.mod > self.max_mod_number:
	#		self.mod = self.max_mod_number

		self.image = gun3.all_img[self.mod]
		self.anim = gun3.all_anims[self.mod]

		self.mod1_characteristics = [3, 3, 10, (4,6), 10, 100, (100,100,200)]    #index: 0 - damage, 1 - bullet_speed, 2 - clip_size, 3 - size (x,y), 4 - delay
		self.mod2_characteristics = [3, 4, 14, (4,6), 10, 100, (100,100,200)]
		self.mod3_characteristics = [4, 4, 16, (4,6), 10, 100, (100,100,200)]
		self.mod4_characteristics = [4, 4, 16, (4,6), 10, 100, (100,100,200)]

		self.all_mod_characteristics = [self.mod1_characteristics, self.mod2_characteristics, self.mod3_characteristics, self.mod4_characteristics]
		self.characteristics = self.all_mod_characteristics[self.mod]

		self.rect = self.image.get_rect()
		self.owner = owner

		self.shoot_delay_timer = 0

		self.shoot_delay_timer = 0
		self.in_clip = self.mod1_characteristics[2]
		self.clip_reload_timer = 0
		self.clip_reload = self.mod1_characteristics[5]

		self.is_shoot_anim = False
		self.shoot_anim_len = len(self.anim)
		self.to_shoot_frame = 0
		self.curent_shoot_anim_frame = 0
		self.shoot_frame_timer = 0

		self.to_shoot = False

		self.offset1_x = 14
		self.offset1_y = 1
		#self.offset2_x = 18
		#self.offset2_y = 9
	def shoot(self):
		default_bullet(self.characteristics[0], self.characteristics[1], self.characteristics[3], self.owner.rect.x + self.offset1_x, self.owner.rect.y + self.offset1_y)
		#default_bullet(self.characteristics[0], self.characteristics[1], self.characteristics[3], self.owner.rect.x + self.offset2_x, self.owner.rect.y + self.offset2_y)

class gun4(gun):

	max_mod_number = 2 #3 in fact, but 3 - 1 = 2
	q1_mech = [0,1,2]
	q2_mech = [0,1,2]
	q3_mech = [0,1,2]
	all_mechs = [q1_mech, q2_mech, q3_mech]

	img_mod1 = gg.player_gun4_mod1
	anim_mod1 = gg.player_gun4_mod1_anim
	img_mod2 = gg.player_gun4_mod2
	anim_mod2 = gg.player_gun4_mod2_anim
	img_mod3 = gg.player_gun4_mod3
	anim_mod3 = gg.player_gun4_mod3_anim

	all_img = [img_mod1, img_mod2, img_mod3]
	all_anims = [anim_mod1, anim_mod2, anim_mod3]

	mod1_cost = (100,100,200)
	mod2_cost = (100,100,200)
	mod3_cost = (100,100,200)

	all_mod_cost = [mod1_cost, mod2_cost, mod3_cost]

	def __init__(self, owner, mod):
		pygame.sprite.Sprite.__init__(self)

		self.mod = mod

		self.max_mod_number = 2 #3 in fact, but 3-1, becouse index in python work like: list[0] - its a first element 
								#													   list[1] - its a second element


	#	if self.mod > self.max_mod_number:
	#		self.mod = self.max_mod_number

		self.image = gun4.all_img[self.mod]
		self.anim = gun4.all_anims[self.mod]

		self.mod1_characteristics = [3, 3, 10, (2,5), 6, 100, (100,100,200)]    #index: 0 - damage, 1 - bullet_speed, 2 - clip_size, 3 - size (x,y), 4 - delay
		self.mod2_characteristics = [3, 4, 14, (2,5), 6, 100, (100,100,200)]
		self.mod3_characteristics = [4, 4, 16, (2,5), 6, 100, (100,100,200)]

		self.all_mod_characteristics = [self.mod1_characteristics, self.mod2_characteristics, self.mod3_characteristics]
		self.characteristics = self.all_mod_characteristics[self.mod]

		self.rect = self.image.get_rect()
		self.owner = owner

		self.shoot_delay_timer = 0

		self.shoot_delay_timer = 0
		self.in_clip = self.mod1_characteristics[2]
		self.clip_reload_timer = 0
		self.clip_reload = self.mod1_characteristics[5]

		self.is_shoot_anim = False
		self.shoot_anim_len = len(self.anim)
		self.to_shoot_frame = 0
		self.curent_shoot_anim_frame = 0
		self.shoot_frame_timer = 0

		self.to_shoot = False

		self.offset1_x = 4
		self.offset1_y = 11
		#self.offset2_x = 18
		#self.offset2_y = 9

	def shoot(self):
		default_bullet(self.characteristics[0], self.characteristics[1], self.characteristics[3], self.owner.rect.x + self.offset1_x, self.owner.rect.y + self.offset1_y)
		#default_bullet(self.characteristics[0], self.characteristics[1], self.characteristics[3], self.owner.rect.x + self.offset2_x, self.owner.rect.y + self.offset2_y)

class gun5(gun):

	max_mod_number = 2 #3 in fact, but 3 - 1 = 2
	q1_mech = [0,1,2]
	q2_mech = [0,1,2]
	q3_mech = [0,1,2]
	all_mechs = [q1_mech, q2_mech, q3_mech]

	img_mod1 = gg.player_gun5_mod1
	anim_mod1 = gg.player_gun5_mod1_anim
	img_mod2 = gg.player_gun5_mod2
	anim_mod2 = gg.player_gun5_mod2_anim
	img_mod3 = gg.player_gun5_mod3
	anim_mod3 = gg.player_gun5_mod3_anim

	all_img = [img_mod1, img_mod2, img_mod3]
	all_anims = [anim_mod1, anim_mod2, anim_mod3]

	mod1_cost = (100,100,200)
	mod2_cost = (100,100,200)
	mod3_cost = (100,100,200)

	all_mod_cost = [mod1_cost, mod2_cost, mod3_cost]

	def __init__(self, owner, mod):
		pygame.sprite.Sprite.__init__(self)

		self.mod = mod

		self.max_mod_number = 2 #3 in fact, but 3-1, becouse index in python work like: list[0] - its a first element 
								#													   list[1] - its a second element


	#	if self.mod > self.max_mod_number:
	#		self.mod = self.max_mod_number

		self.image = gun5.all_img[self.mod]
		self.anim = gun5.all_anims[self.mod]

		self.mod1_characteristics = [3, 3, 10, (2,5), 6, 100, (100,100,200)]    #index: 0 - damage, 1 - bullet_speed, 2 - clip_size, 3 - size (x,y), 4 - delay
		self.mod2_characteristics = [3, 4, 14, (2,5), 6, 100, (100,100,200)]
		self.mod3_characteristics = [4, 4, 16, (2,5), 6, 100, (100,100,200)]

		self.all_mod_characteristics = [self.mod1_characteristics, self.mod2_characteristics, self.mod3_characteristics]
		self.characteristics = self.all_mod_characteristics[self.mod]

		self.rect = self.image.get_rect()
		self.owner = owner

		self.shoot_delay_timer = 0

		self.shoot_delay_timer = 0
		self.in_clip = self.mod1_characteristics[2]
		self.clip_reload_timer = 0
		self.clip_reload = self.mod1_characteristics[5]

		self.is_shoot_anim = False
		self.shoot_anim_len = len(self.anim)
		self.to_shoot_frame = 0
		self.curent_shoot_anim_frame = 0
		self.shoot_frame_timer = 0

		self.to_shoot = False

		self.offset1_x = 4
		self.offset1_y = 11
		#self.offset2_x = 18
		#self.offset2_y = 9

	def shoot(self):
		default_bullet(self.characteristics[0], self.characteristics[1], self.characteristics[3], self.owner.rect.x + self.offset1_x, self.owner.rect.y + self.offset1_y)
		#default_bullet(self.characteristics[0], self.characteristics[1], self.characteristics[3], self.owner.rect.x + self.offset2_x, self.owner.rect.y + self.offset2_y)

class gun6(gun):

	max_mod_number = 2 #3 in fact, but 3 - 1 = 2
	q1_mech = [0,1,2]
	q2_mech = [0,1,2]
	q3_mech = [0,1,2]
	all_mechs = [q1_mech, q2_mech, q3_mech]

	img_mod1 = gg.player_gun6_mod1
	anim_mod1 = gg.player_gun6_mod1_anim
	img_mod2 = gg.player_gun6_mod2
	anim_mod2 = gg.player_gun6_mod2_anim
	img_mod3 = gg.player_gun6_mod3
	anim_mod3 = gg.player_gun6_mod3_anim

	all_img = [img_mod1, img_mod2, img_mod3]
	all_anims = [anim_mod1, anim_mod2, anim_mod3]

	mod1_cost = (100,100,200)
	mod2_cost = (100,100,200)
	mod3_cost = (100,100,200)

	all_mod_cost = [mod1_cost, mod2_cost, mod3_cost]

	def __init__(self, owner, mod):
		pygame.sprite.Sprite.__init__(self)

		self.mod = mod

		self.max_mod_number = 2 #3 in fact, but 3-1, becouse index in python work like: list[0] - its a first element 
								#													   list[1] - its a second element


	#	if self.mod > self.max_mod_number:
	#		self.mod = self.max_mod_number

		self.image = gun6.all_img[self.mod]
		self.anim = gun6.all_anims[self.mod]

		self.mod1_characteristics = [3, 3, 10, (4,5), 6, 100, (100,100,200)]    #index: 0 - damage, 1 - bullet_speed, 2 - clip_size, 3 - size (x,y), 4 - delay
		self.mod2_characteristics = [3, 4, 14, (4,5), 6, 100, (100,100,200)]
		self.mod3_characteristics = [4, 4, 16, (4,5), 6, 100, (100,100,200)]

		self.all_mod_characteristics = [self.mod1_characteristics, self.mod2_characteristics, self.mod3_characteristics]
		self.characteristics = self.all_mod_characteristics[self.mod]

		self.rect = self.image.get_rect()
		self.owner = owner

		self.shoot_delay_timer = 0

		self.shoot_delay_timer = 0
		self.in_clip = self.mod1_characteristics[2]
		self.clip_reload_timer = 0
		self.clip_reload = self.mod1_characteristics[5]

		self.is_shoot_anim = False
		self.shoot_anim_len = len(self.anim)
		self.to_shoot_frame = 0
		self.curent_shoot_anim_frame = 0
		self.shoot_frame_timer = 0

		self.to_shoot = False

		self.offset1_x = 4
		self.offset1_y = 13
		self.offset2_x = 24
		self.offset2_y = 13

class gun7(gun):

	max_mod_number = 2 #3 in fact, but 3 - 1 = 2
	q1_mech = [0,1,2]
	q2_mech = [0,1,2]
	q3_mech = [0,1,2]
	all_mechs = [q1_mech, q2_mech, q3_mech]

	img_mod1 = gg.player_gun7_mod1
	anim_mod1 = gg.player_gun7_mod1_anim
	img_mod2 = gg.player_gun7_mod2
	anim_mod2 = gg.player_gun7_mod2_anim
	img_mod3 = gg.player_gun7_mod3
	anim_mod3 = gg.player_gun7_mod3_anim

	all_img = [img_mod1, img_mod2, img_mod3]
	all_anims = [anim_mod1, anim_mod2, anim_mod3]

	mod1_cost = (10,90,9)
	mod2_cost = (300,200,300)
	mod3_cost = (400,100,200)

	all_mod_cost = [mod1_cost, mod2_cost, mod3_cost]

	def __init__(self, owner, mod):
		pygame.sprite.Sprite.__init__(self)

		self.mod = mod

		self.max_mod_number = 2 #3 in fact, but 3-1, becouse index in python work like: list[0] - its a first element 
								#													   list[1] - its a second element


	#	if self.mod > self.max_mod_number:
	#		self.mod = self.max_mod_number

		self.image = gun7.all_img[self.mod]
		self.anim = gun7.all_anims[self.mod]

		self.mod1_characteristics = [999, 10, 10, (4,5), 6, 100, (100,100,200)]    #index: 0 - damage, 1 - bullet_speed, 2 - clip_size, 3 - size (x,y), 4 - delay
		self.mod2_characteristics = [3, 4, 14, (4,5), 6, 100, (300,300,300)]
		self.mod3_characteristics = [4, 4, 16, (4,5), 6, 100, (100,100,200)]

		self.all_mod_characteristics = [self.mod1_characteristics, self.mod2_characteristics, self.mod3_characteristics]
		self.characteristics = self.all_mod_characteristics[self.mod]

		self.rect = self.image.get_rect()
		self.owner = owner

		self.shoot_delay_timer = 0

		self.shoot_delay_timer = 0
		self.in_clip = self.mod1_characteristics[2]
		self.clip_reload_timer = 0
		self.clip_reload = self.mod1_characteristics[5]

		self.is_shoot_anim = False
		self.shoot_anim_len = len(self.anim)
		self.to_shoot_frame = len(self.anim) - 1
		self.curent_shoot_anim_frame = 0
		self.shoot_frame_timer = 0

		self.to_shoot = False

		self.offset1_x = 14
		self.offset1_y = -1
		#self.offset2_x = 24
		#self.offset2_y = 13

	def shoot(self):
		default_bullet(self.characteristics[0], self.characteristics[1], self.characteristics[3], self.owner.rect.x + self.offset1_x, self.owner.rect.y + self.offset1_y)

class gun8(gun):

	mod1_cost = (100,100,200)
	mod2_cost = (100,100,200)
	mod3_cost = (100,100,200)

	all_mod_cost = [mod1_cost, mod2_cost, mod3_cost]
	max_mod_number = 2 #3 in fact, but 3 - 1 = 2
	q1_mech = [0,1,2]
	q2_mech = [0,1,2]
	q3_mech = [0,1,2]
	all_mechs = [q1_mech, q2_mech, q3_mech]

	img_mod1 = gg.player_gun8_mod1
	anim_mod1 = gg.player_gun8_mod1_anim
	img_mod2 = gg.player_gun8_mod2
	anim_mod2 = gg.player_gun8_mod2_anim
	img_mod3 = gg.player_gun8_mod3
	anim_mod3 = gg.player_gun8_mod3_anim

	all_img = [img_mod1, img_mod2, img_mod3]
	all_anims = [anim_mod1, anim_mod2, anim_mod3]

	def __init__(self, owner, mod):
		pygame.sprite.Sprite.__init__(self)

		self.mod = mod

		self.max_mod_number = 2 #3 in fact, but 3-1, becouse index in python work like: list[0] - its a first element 
								#													   list[1] - its a second element


	#	if self.mod > self.max_mod_number:
	#		self.mod = self.max_mod_number

		self.image = gun8.all_img[self.mod]
		self.anim = gun8.all_anims[self.mod]

		self.mod1_characteristics = [3, 3, 10, (4,6), 14, 100, (100,100,200)]    #index: 0 - damage, 1 - bullet_speed, 2 - clip_size, 3 - size (x,y), 4 - delay
		self.mod2_characteristics = [3, 4, 14, (4,6), 14, 100, (100,100,200)]
		self.mod3_characteristics = [4, 4, 16, (4,6), 14, 100, (100,100,200)]

		self.all_mod_characteristics = [self.mod1_characteristics, self.mod2_characteristics, self.mod3_characteristics]
		self.characteristics = self.all_mod_characteristics[self.mod]

		self.rect = self.image.get_rect()
		self.owner = owner

		self.shoot_delay_timer = 0

		self.shoot_delay_timer = 0
		self.in_clip = self.mod1_characteristics[2]
		self.clip_reload_timer = 0
		self.clip_reload = self.mod1_characteristics[5]

		self.is_shoot_anim = False
		self.shoot_anim_len = len(self.anim)
		self.to_shoot_frame = 0
		self.curent_shoot_anim_frame = 0
		self.shoot_frame_timer = 0

		self.to_shoot = False

		self.offset1_x = 14
		self.offset1_y = -1
		#self.offset2_x = 18
		#self.offset2_y = 9

	def shoot(self):
		default_bullet(self.characteristics[0], self.characteristics[1], self.characteristics[3], self.owner.rect.x + self.offset1_x, self.owner.rect.y + self.offset1_y)
		#default_bullet(self.characteristics[0], self.characteristics[1], self.characteristics[3], self.owner.rect.x + self.offset2_x, self.owner.rect.y + self.offset2_y)

class gun9(gun):

	mod1_cost = (100,100,200)
	mod2_cost = (100,100,200)

	all_mod_cost = [mod1_cost, mod2_cost]

	max_mod_number = 1 #3 in fact, but 3 - 1 = 2
	q1_mech = [0,1,2]
	q2_mech = [0,1,2]
	q3_mech = [0,1,2]
	all_mechs = [q1_mech, q2_mech, q3_mech]

	img_mod1 = gg.player_gun9_mod1
	anim_mod1 = gg.player_gun9_mod1_anim
	img_mod2 = gg.player_gun9_mod2
	anim_mod2 = gg.player_gun9_mod2_anim

	all_img = [img_mod1, img_mod2]
	all_anims = [anim_mod1, anim_mod2]

	def __init__(self, owner, mod):
		pygame.sprite.Sprite.__init__(self)

		self.mod = mod

		self.max_mod_number = 1 #3 in fact, but 3-1, becouse index in python work like: list[0] - its a first element 
								#													   list[1] - its a second element


	#	if self.mod > self.max_mod_number:
	#		self.mod = self.max_mod_number

		self.image = gun9.all_img[self.mod]
		self.anim = gun9.all_anims[self.mod]

		self.mod1_characteristics = [3, 3, 10, (2,4), 5, 100, (100,100,200)]    #index: 0 - damage, 1 - bullet_speed, 2 - clip_size, 3 - size (x,y), 4 - delay
		self.mod2_characteristics = [3, 4, 14, (2,4), 5, 100, (100,100,200)]

		self.all_mod_characteristics = [self.mod1_characteristics, self.mod2_characteristics]
		self.characteristics = self.all_mod_characteristics[self.mod]

		self.rect = self.image.get_rect()
		self.owner = owner

		self.shoot_delay_timer = 0

		self.shoot_delay_timer = 0
		self.in_clip = self.mod1_characteristics[2]
		self.clip_reload_timer = 0
		self.clip_reload = self.mod1_characteristics[5]

		self.is_shoot_anim = False
		self.shoot_anim_len = len(self.anim)
		self.to_shoot_frame = 0
		self.curent_shoot_anim_frame = 0
		self.shoot_frame_timer = 0

		self.to_shoot = False

		self.offset1_x = 4
		self.offset1_y = 14
		self.offset2_x = 26
		self.offset2_y = 14

"""
class gun1(pygame.sprite.Sprite):
	obj_type = "gun"
	max_mod_number = 2
	q1_mech = [0,1]
	q2_mech = [0,1,2]
	q3_mech = [0,1,2]
	all_mechs = [q1_mech, q2_mech, q3_mech]

	img_mod1 = gg.player_gun1_mod1
	img_mod2 = gg.player_gun1_mod2
	img_mod3 = gg.player_gun1_mod3

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

	img_mod1 = gg.player_gun2_mod1
	img_mod2 = gg.player_gun2_mod2
	img_mod3 = gg.player_gun2_mod3

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

	img_mod1 = gg.player_gun3_mod1
	img_mod2 = gg.player_gun3_mod2
	img_mod3 = gg.player_gun3_mod3
	img_mod4 = gg.player_gun3_mod4

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


"""
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
		if len(self.enemy_m.sl[0][0]) == 3:
			self.line = self.enemy_m.fl
		if len(self.enemy_m.fl[0][0]) == 3:
			self.line = self.enemy_m.sl
		if len(self.enemy_m.sl[0][0]) < 3 and len(self.enemy_m.fl[0][0]) < 3:
			self.line = random.choice([self.enemy_m.sl, self.enemy_m.fl])

		self.line[0][0].append(self)
		self.line[1][0] = True

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
				self.speedy_now -=0.08
		else:
			if self.speedy_now < 0:
				self.speedy_now += 0.08
		if self.move_down:
			if self.speedy_max > self.speedy_now:
				self.speedy_now += 0.08
		else:
			if self.speedy_now > 0:
				self.speedy_now -= 0.08
		if self.move_right:
			if self.speedx_max > self.speedx_now:
				self.speedx_now += 0.08
		else:
			if self.speedx_now > 0:
				self.speedx_now -= 0.08
		if self.move_left:
			if -self.speedx_max < self.speedx_now:
				self.speedx_now -= 0.08
		else:
			if self.speedx_now < 0:
				self.speedx_now += 0.08

		self.move_up = False
		self.move_down = False
		self.move_left = False
		self.move_right = False
		
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
		self.line[0][0].remove(self)
		self.line[1][0] = True

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
	orig_img = gg.enemy_1.copy()
	icon = gg.enemy_1_icon
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
	orig_img = gg.enemy_2.copy()
	icon = gg.enemy_2_icon
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
		enemy_bullet(self.bullet_speed, self.bullet_size, self.rect.x + self.bullet_offset1_x, self.rect.top + self.bullet_offset1_y, self.bullet_color)
		enemy_bullet(self.bullet_speed, self.bullet_size, self.rect.x + self.bullet_offset2_x, self.rect.top + self.bullet_offset2_y, self.bullet_color)


class enemy_3(enemy):
	enemy_id = 3
	orig_img = gg.enemy_3.copy()
	icon = gg.enemy_3_icon
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
		self.line[0][0].remove(self)
		self.line[1][0] = True

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
	orig_img = gg.enemy_4.copy()
	icon = gg.enemy_4_icon
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
	orig_img = gg.enemy_5.copy()
	icon = gg.enemy_5_icon
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
	orig_img = gg.enemy_6.copy()
	icon = gg.enemy_6_icon
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
	orig_img = gg.enemy_7.copy()
	icon = gg.enemy_7_icon
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
	orig_img = gg.enemy_8.copy()
	icon = gg.enemy_8_icon
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
	orig_img = gg.enemy_9.copy()
	icon = gg.enemy_9_icon
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

		self.health = 100

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

		for i in all_sprites:
			if type(i).obj_type == "player_bullet":
				if self.rect.colliderect(i):
					self.health -= i.damage
					i.kill()

		if self.health <= 0:
			self.is_kill_anim = True


		if self.enemy.hp <= 0:
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

		self.first_line = []
		self.second_line = []
		self.non_lined = []

		self.action_lvl = action_lvl_obj

		self.enemy_counter = 10

		self.three_in_tuple_sl_funcs = [self.three_in_tuple_sl1, self.three_in_tuple_sl2, self.three_in_tuple_sl3, self.three_in_tuple_sl4,
		self.three_in_tuple_sl5, self.three_in_tuple_sl6, self.three_in_tuple_sl7, self.three_in_tuple_sl8, self.three_in_tuple_sl9, self.three_in_tuple_sl10, self.three_in_tuple_sl11,
		self.three_in_tuple_sl12, self.three_in_tuple_sl13]

		self.two_in_tuple_sl_funcs = [self.two_in_tuple_sl1, self.two_in_tuple_sl2, self.two_in_tuple_sl3, self.two_in_tuple_sl4, self.two_in_tuple_sl5, self.two_in_tuple_sl6, self.two_in_tuple_sl7,
		self.two_in_tuple_sl8, self.two_in_tuple_sl9, self.two_in_tuple_sl10, self.two_in_tuple_sl11, self.two_in_tuple_sl12, self.two_in_tuple_sl13, self.two_in_tuple_sl14, self.two_in_tuple_sl15,
		self.two_in_tuple_sl16, self.two_in_tuple_sl17, self.two_in_tuple_sl18, self.two_in_tuple_sl19, self.two_in_tuple_sl20, self.two_in_tuple_sl21, self.two_in_tuple_sl22, self.two_in_tuple_sl23,
		self.two_in_tuple_sl24, self.two_in_tuple_sl25]

		self.one_in_tuple_sl_funcs = [self.one_in_tuple_sl1]

		self.three_in_tuple_fl_funcs = [self.three_in_tuple_fl1, self.three_in_tuple_fl2, self.three_in_tuple_fl3, self.three_in_tuple_fl4, self.three_in_tuple_fl5, self.three_in_tuple_fl6, 
		self.three_in_tuple_fl7,self.three_in_tuple_fl8, self.three_in_tuple_fl9, self.three_in_tuple_fl10, self.three_in_tuple_fl11, self.three_in_tuple_fl12, self.three_in_tuple_fl3]


		self.two_in_tuple_fl_funcs = [self.two_in_tuple_fl1, self.two_in_tuple_fl2, self.two_in_tuple_fl3, self.two_in_tuple_fl4, self.two_in_tuple_fl5, self.two_in_tuple_fl6, self.two_in_tuple_fl6,
		self.two_in_tuple_fl7, self.two_in_tuple_fl8, self.two_in_tuple_fl9, self.two_in_tuple_fl10, self.two_in_tuple_fl11, self.two_in_tuple_fl12, self.two_in_tuple_fl13, self.two_in_tuple_fl14,
		self.two_in_tuple_fl15, self.two_in_tuple_fl16, self.two_in_tuple_fl17, self.two_in_tuple_fl18, self.two_in_tuple_fl19, self.two_in_tuple_fl20, self.two_in_tuple_fl21, self.two_in_tuple_fl22,
		self.two_in_tuple_fl23, self.two_in_tuple_fl24, self.two_in_tuple_fl25]
		self.one_in_tuple_fl_funcs = [self.one_in_tuple_fl1]

		self.fl_change_timer = 0
		self.sl_change_timer = 0


		self.all_funcs = [[self.one_in_tuple_sl_funcs,self.two_in_tuple_sl_funcs,self.three_in_tuple_sl_funcs], [self.one_in_tuple_fl_funcs, self.two_in_tuple_fl_funcs, self.three_in_tuple_fl_funcs]]

		self.fl_changed = False
		self.sl_changed = False

		self.fl = ([self.first_line], [self.fl_changed])
		self.sl = ([self.second_line], [self.sl_changed])

		self.fl_func = None
		self.sl_func = None


		updateble_objects_m.objects.append(self)

	def update(self):



		if len(self.enemy_list) < 6 and self.enemy_counter > 0:
			enemy = random.choice(self.to_spawn)(random.randint(0, 600 - 40), -60 , self)
			self.enemy_counter -= 1
			self.enemy_list.append(enemy)

		if self.enemy_counter <= 0 and len(self.enemy_list) <= 0:
			self.action_lvl.kill()

		if self.sl[1][0] == True:
			self.sl[1][0] = False
			self.sl_change_timer = 0
			if self.second_line == []:
				self.sl_func = None
			else:
				enemy_counter = 0
				for i in self.second_line:
					enemy_counter += 1
				enemy_counter -= 1
				self.sl_func = random.choice(self.all_funcs[0][enemy_counter])

		if self.fl[1][0] == True:
			self.fl[1][0] = False
			self.fl_change_timer = 0
			if self.first_line == []:
				self.fl_func = None
			else:
				enemy_counter = 0
				for i in self.first_line:
					enemy_counter += 1
				enemy_counter -= 1
				self.fl_func = random.choice(self.all_funcs[1][enemy_counter])

		if self.fl_change_timer > 280:
			self.fl[1][0] = True
			self.fl_change_timer = 0
		else:
			self.fl_change_timer += 1

		if self.sl_change_timer > 280:
			self.sl[1][0] = True
			self.sl_change_timer = 0
		else:
			self.sl_change_timer += 1

		if self.sl_func != None:
			print("its_work")
			self.sl_func()

		if self.fl_func != None:
			self.fl_func()

		draw_text(game_surface, str(self.sl_func), 20, 100, 40, (255,255,255))

	def three_in_tuple_sl1(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 60)
		self.second_line[1].go_to(self.second_line[0].rect.left - 60, 50)
		self.second_line[2].go_to(self.second_line[0].rect.right + 60, 50)

	def three_in_tuple_sl2(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 60, 20)
		self.second_line[2].go_to(self.second_line[0].rect.right + 60, 60)

	def three_in_tuple_sl3(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 60, 60)
		self.second_line[2].go_to(self.second_line[0].rect.right + 60, 20)

	def three_in_tuple_sl4(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 24)
		self.second_line[1].go_to(self.second_line[0].rect.left - 60, 24)
		self.second_line[2].go_to(self.second_line[0].rect.right + 60, 24)

	def three_in_tuple_sl5(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 24)
		self.second_line[1].go_to(self.second_line[0].rect.left - 80, 24)
		self.second_line[2].go_to(self.second_line[0].rect.right + 80, 24)

	def three_in_tuple_sl6(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 80, 60)
		self.second_line[2].go_to(self.second_line[0].rect.right + 40, 20)

	def three_in_tuple_sl7(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 40, 60)
		self.second_line[2].go_to(self.second_line[0].rect.right + 80, 20)

	def three_in_tuple_sl8(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 40, 60)
		self.second_line[2].go_to(self.second_line[0].rect.right + 80, 60)

	def three_in_tuple_sl9(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 80, 60)
		self.second_line[2].go_to(self.second_line[0].rect.right + 40, 60)

	def three_in_tuple_sl10(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 80, 60)
		self.second_line[2].go_to(self.second_line[0].rect.right + 80, 20)

	def three_in_tuple_sl11(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 80, 20)
		self.second_line[2].go_to(self.second_line[0].rect.right + 80, 60)

	def three_in_tuple_sl12(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 80, 60)
		self.second_line[2].go_to(self.second_line[0].rect.right + 80, 20)

	def three_in_tuple_sl13(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 80, 60)
		self.second_line[2].go_to(self.second_line[0].rect.right + 80, 20)

	def two_in_tuple_sl1(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 20)
		self.second_line[1].go_to(game.action_lvl.player.rect.centerx, 50)

	def two_in_tuple_sl2(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 60)
		self.second_line[1].go_to(self.second_line[0].rect.left - 60, 50)

	def two_in_tuple_sl3(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.right + 60, 60)

	def two_in_tuple_sl4(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 60, 60)

	def two_in_tuple_sl5(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 24)
		self.second_line[1].go_to(self.second_line[0].rect.left - 60, 24)

	def two_in_tuple_sl6(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 24)
		self.second_line[1].go_to(self.second_line[0].rect.right + 60, 24)

	def two_in_tuple_sl7(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 24)
		self.second_line[1].go_to(self.second_line[0].rect.right + 80, 24)

	def two_in_tuple_sl8(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 24)
		self.second_line[1].go_to(self.second_line[0].rect.left - 80, 24)

	def two_in_tuple_sl9(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 80, 60)

	def two_in_tuple_sl10(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.right + 40, 20)

	def two_in_tuple_sl11(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 40, 60)

	def two_in_tuple_sl12(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.right + 80, 20)

	def two_in_tuple_sl13(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 40, 60)

	def two_in_tuple_sl14(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.right + 80, 60)

	def two_in_tuple_sl15(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.right + 40, 60)

	def two_in_tuple_sl16(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 80, 60)

	def two_in_tuple_sl17(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.right + 80, 20)

	def two_in_tuple_sl18(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 80, 60)

	def two_in_tuple_sl19(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 80, 20)

	def two_in_tuple_sl20(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.right + 80, 60)

	def two_in_tuple_sl21(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 80, 60)

	def two_in_tuple_sl22(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.right + 80, 20)

	def two_in_tuple_sl23(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.right + 80, 20)

	def two_in_tuple_sl24(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 40)
		self.second_line[1].go_to(self.second_line[0].rect.left - 80, 60)

	def two_in_tuple_sl25(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 20)
		self.second_line[1].go_to(game.action_lvl.player.rect.centerx - 30, 50)

	def one_in_tuple_sl1(self):
		self.second_line[0].go_to(game.action_lvl.player.rect.centerx, 50)

	def three_in_tuple_fl1(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 120)
		self.first_line[1].go_to(self.first_line[0].rect.left - 60, 100)
		self.first_line[2].go_to(self.first_line[0].rect.right + 60, 100)

	def three_in_tuple_fl2(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.left - 60, 80)
		self.first_line[2].go_to(self.first_line[0].rect.right + 60, 120)

	def three_in_tuple_fl3(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.left - 60, 120)
		self.first_line[2].go_to(self.first_line[0].rect.right + 60, 80)

	def three_in_tuple_fl4(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 104)
		self.first_line[1].go_to(self.first_line[0].rect.left - 60, 104)
		self.first_line[2].go_to(self.first_line[0].rect.right + 60, 104)

	def three_in_tuple_fl5(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 104)
		self.first_line[1].go_to(self.first_line[0].rect.left - 80, 104)
		self.first_line[2].go_to(self.first_line[0].rect.right + 80, 104)

	def three_in_tuple_fl6(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.left - 80, 120)
		self.first_line[2].go_to(self.first_line[0].rect.right + 40, 80)

	def three_in_tuple_fl7(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.left - 40, 120)
		self.first_line[2].go_to(self.first_line[0].rect.right + 80, 80)

	def three_in_tuple_fl8(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 80)
		self.first_line[1].go_to(self.first_line[0].rect.left - 40, 120)
		self.first_line[2].go_to(self.first_line[0].rect.right + 80, 100)

	def three_in_tuple_fl9(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.left - 80, 120)
		self.first_line[2].go_to(self.first_line[0].rect.right + 40, 120)

	def three_in_tuple_fl10(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.left - 80, 120)
		self.first_line[2].go_to(self.first_line[0].rect.right + 80, 80)

	def three_in_tuple_fl11(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.left - 80, 80)
		self.first_line[2].go_to(self.first_line[0].rect.right + 80, 120)

	def three_in_tuple_fl12(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.left - 80, 120)
		self.first_line[2].go_to(self.first_line[0].rect.right + 80, 80)

	def three_in_tuple_fl13(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.left - 80, 120)
		self.first_line[2].go_to(self.first_line[0].rect.right + 80, 80)

	def two_in_tuple_fl1(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 80)
		self.first_line[1].go_to(game.action_lvl.player.rect.centerx, 110)

	def two_in_tuple_fl2(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 110)
		self.first_line[1].go_to(self.first_line[0].rect.left - 60, 100)

	def two_in_tuple_fl3(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.right + 60, 120)

	def two_in_tuple_fl4(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.left - 60, 110)

	def two_in_tuple_fl5(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 94)
		self.first_line[1].go_to(self.first_line[0].rect.left - 60, 94)

	def two_in_tuple_fl6(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 94)
		self.first_line[1].go_to(self.first_line[0].rect.right + 60, 94)

	def two_in_tuple_fl7(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 94)
		self.first_line[1].go_to(self.first_line[0].rect.right + 80, 94)

	def two_in_tuple_fl8(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 94)
		self.first_line[1].go_to(self.first_line[0].rect.left - 80, 94)

	def two_in_tuple_fl9(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 90)
		self.first_line[1].go_to(self.first_line[0].rect.left - 80, 110)

	def two_in_tuple_fl10(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 90)
		self.first_line[1].go_to(self.first_line[0].rect.left - 40, 110)

	def two_in_tuple_fl11(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 110)
		self.first_line[1].go_to(self.first_line[0].rect.right + 80, 90)

	def two_in_tuple_fl12(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.left - 40, 120)

	def two_in_tuple_fl13(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.right + 80, 120)

	def two_in_tuple_fl14(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.right + 40, 120)

	def two_in_tuple_fl15(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.left - 80, 120)

	def two_in_tuple_fl16(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 110)
		self.first_line[1].go_to(self.first_line[0].rect.right + 80, 90)

	def two_in_tuple_fl17(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 90)
		self.first_line[1].go_to(self.first_line[0].rect.left - 80, 110)

	def two_in_tuple_fl18(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 120)
		self.first_line[1].go_to(self.first_line[0].rect.left - 80, 100)

	def two_in_tuple_fl19(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.right + 80, 120)

	def two_in_tuple_fl20(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)
		self.first_line[1].go_to(self.first_line[0].rect.left - 80, 120)

	def two_in_tuple_fl21(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 110)
		self.first_line[1].go_to(self.first_line[0].rect.right + 80, 90)

	def two_in_tuple_fl22(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 110)
		self.first_line[1].go_to(self.first_line[0].rect.right + 80, 90)

	def two_in_tuple_fl23(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 90)
		self.first_line[1].go_to(self.first_line[0].rect.left - 80, 120)

	def two_in_tuple_fl24(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 90)
		self.first_line[1].go_to(game.action_lvl.player.rect.centerx - 30, 110)

	def two_in_tuple_fl25(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 110)
		self.first_line[1].go_to(self.first_line[0].rect.right + 40, 90)

	def one_in_tuple_fl1(self):
		self.first_line[0].go_to(game.action_lvl.player.rect.centerx, 100)

class mouse(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10, 10))
		self.rect = self.image.get_rect()
		self.image.fill((255,0,0))
		self.rect.centerx = mouse_position_x
		self.rect.centery = mouse_position_y
		pygame.mouse.set_visible(False)
		post_processing_m.objects.append(self)
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
		global mouse_position_x 
		global mouse_position_y
		mouse_position_x = self.rect.centerx
		mouse_position_y = self.rect.centery

		game_surface.blit(self.image, (self.rect.x, self.rect.y))

class mechanic_upgrade_window():
	q1_guns = [gun1, gun2, gun3, gun4, gun5, gun6, gun7, gun8, gun9]
	q2_guns = [gun1, gun2, gun3, gun4, gun5, gun6, gun7, gun8, gun9]
	q3_guns = [gun1, gun2, gun3, gun4, gun5, gun6, gun7, gun8, gun9]
	all_q = [q1_guns, q2_guns, q3_guns]
	def __init__(self, qual, owner):

		black_off()

		self.mouse = mouse()

		self.qualification = qual - 1
		self.owner = owner

		self.to_upgrade_list = []
		self.can_upgrade = mechanic_upgrade_window.all_q[self.qualification].copy()

		if self.owner.player_gun.max_mod_number == self.owner.player_gun_mod:
			self.can_upgrade.remove(self.owner.player_gun)
			#print("max_mod_number")
			if self.can_upgrade != []:
				self.to_upgrade_slot2 = random.choice(self.can_upgrade)
				self.can_upgrade.remove(self.to_upgrade_slot2)
				self.to_upgrade_list.append((self.to_upgrade_slot2, 0))

		else:
			for i in self.can_upgrade:
				if i == self.owner.player_gun:
					#print("if i == self.owner.player_gun")
					if i.all_mechs[self.qualification] != []:
						#print("i.all_mechs[self.qualification] != []")
						for x in i.all_mechs[self.qualification]:
							if i.max_mod_number > self.owner.player_gun_mod:

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

		x = 66
		y = 54
		num = 0
		for i in range(len(self.to_upgrade_list)):
			b = button_for_mechanic_window(x, y, self, num)
			x += 168
			num+=1

		self.slot1_res1_pos = (84, 258)
		self.slot1_res2_pos = (132, 258)
		self.slot1_res3_pos = (180, 258)

		self.slot2_res1_pos = (252, 258)
		self.slot2_res2_pos = (300, 258)
		self.slot2_res3_pos = (348, 258)

		self.slot3_res1_pos = (420, 258)
		self.slot3_res2_pos = (468, 258)
		self.slot3_res3_pos = (516, 258)

		self.all_res_pos = [[self.slot1_res1_pos, self.slot1_res2_pos,self.slot1_res3_pos],
		[self.slot2_res1_pos, self.slot2_res2_pos, self.slot2_res3_pos],
		[self.slot3_res1_pos, self.slot3_res2_pos, self.slot3_res3_pos]]

		updateble_objects_m.objects.append(self)

		self.info_panel = info_panel_mech_window(self)
		self.button_exit = button_exit_for_mechanic_window(self)

	def update(self):
		game_surface.blit(gg.mechanic_window_fon, (0, 0))
		x = 68
		y = 56
		for i in self.to_upgrade_list:
			#print(str(i))
			game_surface.blit(pygame.transform.scale(i[0].all_img[i[1]].copy(), (128, 128)), (x, y))
			x += 168
		#draw_text(game_surface, "qualification"+str(self.qualification), 20, 20, 20, (255,255,255))
		#draw_text(game_surface, str(self.to_upgrade_list), 15, 200, 40, (255,255,255))
		x = 0
		for i in self.to_upgrade_list:
			draw_text(game_surface, str(i[0].all_mod_cost[i[1]][0]), 18, self.all_res_pos[x][0][0], self.all_res_pos[x][0][1], (172, 176, 207))
			draw_text(game_surface, str(i[0].all_mod_cost[i[1]][1]), 18, self.all_res_pos[x][1][0], self.all_res_pos[x][1][1], (172, 176, 207))
			draw_text(game_surface, str(i[0].all_mod_cost[i[1]][2]), 18, self.all_res_pos[x][2][0], self.all_res_pos[x][2][1], (172, 176, 207))

			x += 1
		self.info_panel.update()

	def kill_and_up(self, num):
		for i in all_sprites:
			i.kill()
		updateble_objects_m.objects.remove(self)
		post_processing_m.objects.remove(self.mouse)
		self.owner.player_gun = self.to_upgrade_list[num][0]
		self.owner.player_gun_mod = self.to_upgrade_list[num][1]
		self.owner.append()
		self.owner.action_lvl_now = False
		self.owner.lvl_changed = True

	def kill(self):
		for i in all_sprites:
			i.kill()
		post_processing_m.objects.remove(self.mouse)
		updateble_objects_m.objects.remove(self)
		self.owner.append()
		self.owner.action_lvl_now = False
		self.owner.lvl_changed = True

class info_panel_mech_window():
	def __init__(self, owner):
		self.owner = owner
		self.image = gg.mechanic_window_info_panel.copy()
		self.rect = self.image.get_rect()
		self.rect.x = 600 - self.rect.width
		self.rect.y = 0

		self.offset_x = 0

	def update(self):
		if self.rect.colliderect(self.owner.mouse):
			if self.rect.x > 600 - self.rect.width:
				self.offset_x -= 2
				if self.offset_x < -20:
					self.offset_x = -20
					
				self.rect.x += self.offset_x
				if self.rect.x < 600 - self.rect.width:
					self.rect.x = 600 - self.rect.width
					self.offset_x = 0
		else:
			if self.rect.right < 600 + 272 - 66:
				self.offset_x += 2
				if self.offset_x > 20:

					self.offset_x = 20
				self.rect.x += self.offset_x
				if self.rect.right > 600 + 272 - 66:
					self.rect.right = 600 + 272 - 66
					self.offset_x = 0

		if self.rect.left > 600 - 66:
			self.rect.left = 600 - 66


		self.image = gg.mechanic_window_info_panel.copy()
		self.image.blit(game.player_gun.all_img[game.player_gun_mod], (122+66, 16))
		draw_text(self.image, str(game.player_health), 40, 40+66, 38 ,(172, 176, 207))
		draw_text(self.image, str(game.resours1), 32, 41+66, 115 ,(172, 176, 207))
		draw_text(self.image, str(game.resours2), 32, 105+66, 115 ,(172, 176, 207))
		draw_text(self.image, str(game.resours3), 32, 170+66, 115 ,(172, 176, 207))
		game_surface.blit(self.image, (self.rect.x, self.rect.y))


class button_for_mechanic_window(pygame.sprite.Sprite):
	def __init__(self, x, y, owner, num):
		pygame.sprite.Sprite.__init__(self)
		self.owner = owner
		self.numeration = num
		self.image = pygame.Surface((132, 132))
		self.image.set_alpha(0)
		#self.image.fill((0,255,255))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		all_sprites.add(self)
	def update(self):
		mouse_pressed = pygame.mouse.get_pressed()
		if self.rect.colliderect(self.owner.mouse) and mouse_pressed[0]:
			if self.owner.to_upgrade_list[self.numeration][0].all_mod_cost[self.owner.to_upgrade_list[self.numeration][1]][0] <= game.resours1 and self.owner.to_upgrade_list[self.numeration][0].all_mod_cost[self.owner.to_upgrade_list[self.numeration][1]][1] <= game.resours2 and self.owner.to_upgrade_list[self.numeration][0].all_mod_cost[self.owner.to_upgrade_list[self.numeration][1]][2] <= game.resours3: 
				game.resours1 -= self.owner.to_upgrade_list[self.numeration][0].all_mod_cost[self.owner.to_upgrade_list[self.numeration][1]][0]
				game.resours2 -= self.owner.to_upgrade_list[self.numeration][0].all_mod_cost[self.owner.to_upgrade_list[self.numeration][1]][1]
				game.resours3 -= self.owner.to_upgrade_list[self.numeration][0].all_mod_cost[self.owner.to_upgrade_list[self.numeration][1]][2]
				self.owner.kill_and_up(self.numeration)

class button_exit_for_mechanic_window(pygame.sprite.Sprite):
	def __init__(self, owner):
		pygame.sprite.Sprite.__init__(self)
		self.owner = owner
		self.image = gg.mechanic_window_exit_button
		#self.image.fill((255,0,0))
		self.rect = self.image.get_rect()
		self.rect.x = 259
		self.rect.y = 294
		draw_text(self.image, "EXIT", 31, self.rect.width / 2, self.rect.height / 2, (189,218,224))
		all_sprites.add(self)

	def update(self):
		mouse_pressed = pygame.mouse.get_pressed()
		if self.rect.colliderect(self.owner.mouse) and mouse_pressed[0]:
			self.owner.kill()
			self.kill()

class black_on():
	def __init__(self, func, args):
		self.image = pygame.Surface((width, height))
		self.image.fill((0,0,0))
		self.func = func
		self.args = args
		self.alpha = 0

		post_processing_m.objects.append(self)

	def update(self):
		if self.alpha == 255:
			#game.press_timer = 120
			#game.lvl_changed = True
			post_processing_m.objects.remove(self)
			if self.args != None:
				self.func(self.args)
			else:
				self.func()

		self.alpha += 10
		if self.alpha > 255:
			self.alpha = 255
		self.image.set_alpha(self.alpha)

		game_surface.blit(self.image, (0,0))

class black_off():
	def __init__(self):
		self.image = pygame.Surface((width, height))
		self.image.fill((0,0,0))
		self.alpha = 255
		post_processing_m.objects.append(self)

	def update(self):
		if self.alpha == 0:
			post_processing_m.objects.remove(self)

		self.alpha -= 10
		if self.alpha <= 0:
			self.alpha = 0
		self.image.set_alpha(self.alpha)

		game_surface.blit(self.image, (0,0))

class hitec_anim_manager():
	def __init__(self, owner):
		self.highteck_ups = owner.highteck_ups
		self.to_create_list = []
		index = 0
		for i in self.highteck_ups:
			if i == True:
				self.to_create_list.append(owner.highteck_ups_visual[index])

			index += 1

		self.created_objs_list = []

		post_processing_m.objects.append(self)

	def update(self):
		for i in self.to_create_list:
			x = i()
			self.to_create_list.remove(i)
			self.created_objs_list.append(x)

		x = 350
		y = 60
		for i in self.highteck_ups:
			draw_text(game_surface, str(i), 10, x, y, (255,255,255))
			x -= 48



		x = 350
		y = 30
		for i in self.created_objs_list:
			i.update()
			i.rect.x = x
			i.rect.y = y

			game_surface.blit(i.background, (i.rect.centerx - (((i.background.get_width()) - i.rect.width) / 2), i.rect.centery - ((i.background.get_height() - i.rect.height) / 2)))
			game_surface.blit(i.image , (x, y))
			x -= 48

class highteck_up_visual(pygame.sprite.Sprite):
	img = gg.highteck_up_plate
	anim = gg.highteck_up_plate_anim
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image =  highteck_up_visual.img
		self.rect = self.image.get_rect()

		self.anim = highteck_up_visual.anim
		self.anim_speed = 6
		self.anim_len = len(self.anim)
		self.is_anim = False
		self.curent_anim_frame = 0
		self.frame_timer = 0

		self.init_anim = gg.enemy_4_rocket_init_anim
		self.init_anim_speed = 6
		self.is_init_anim = True
		self.init_anim_len = len(self.init_anim)
		self.curent_init_anim_frame = 0
		self.init_anim_frame_timer = 0

		self.anim_reload = 200
		self.anim_reload_timer = 0

		self.background = gg.compas_background

	def update(self):
		if self.anim_reload_timer > self.anim_reload and self.is_anim == False:
			self.is_anim = True
			self.anim_reload_timer = 0
		else:
			self.anim_reload_timer += 1

		if self.is_anim == True and self.is_init_anim == False:
			if self.frame_timer > self.anim_speed:
				self.image = self.anim[self.curent_anim_frame]
				self.curent_anim_frame += 1
				self.frame_timer = 0
				if self.anim_len <= self.curent_anim_frame:
					self.curent_anim_frame = 0
					self.is_anim = False
			else:
				self.frame_timer += 1

		if self.is_init_anim:
			if self.init_anim_frame_timer > self.init_anim_speed:
				self.image = self.init_anim[self.curent_init_anim_frame]
				self.curent_init_anim_frame += 1
				self.init_anim_frame_timer = 0
				if self.init_anim_len <= self.curent_init_anim_frame:
					self.curent_init_anim_frame = 0
					self.is_init_anim = False
					self.is_anim = True

					self.image = self.anim[self.curent_anim_frame]

			else:
				self.init_anim_frame_timer += 1

class hitec_compas_visual(highteck_up_visual):
	def __init__(self):
		highteck_up_visual.__init__(self)
		self.image = gg.compas
		self.init_anim = gg.compas_init
		self.anim = gg.compas_anim
		self.anim_len = len(self.anim)
		self.init_anim_len = len(self.init_anim)
		self.anim_reload = 200

		self.background = gg.compas_background

class hitec_hable_visual(highteck_up_visual):
	def __init__(self):
		highteck_up_visual.__init__(self)
		self.image = gg.hable
		self.init_anim = gg.hable_init
		self.anim = gg.hable_anim
		self.anim_len = len(self.anim)
		self.init_anim_len = len(self.init_anim)
		self.anim_speed = 10
		self.anim_reload = 400

		self.background = gg.hable_background

class hitec_boosted_engine_visual(highteck_up_visual):
	def __init__(self):
		highteck_up_visual.__init__(self)
		self.image = gg.boosted_engine
		self.init_anim = gg.boosted_engine_init
		self.anim = gg.boosted_engine_anim
		self.anim_len = len(self.anim)
		self.init_anim_len = len(self.init_anim)
		self.anim_reload = 100
		self.anim_speed = 10

		self.background = gg.boosted_engine_background

class hitec_green_energy_visual(highteck_up_visual):
	def __init__(self):
		highteck_up_visual.__init__(self)
		self.image = gg.green_energy
		self.init_anim = gg.green_energy_init
		self.anim = gg.green_energy_anim
		self.anim_len = len(self.anim)
		self.init_anim_len = len(self.init_anim)
		self.anim_reload = 200
		self.anim_speed = 10
		self.init_anim_speed = 3

		self.background = gg.green_energy_background

class hitec_polimerization_visual(highteck_up_visual):
	def __init__(self):
		highteck_up_visual.__init__(self)
		self.image = gg.polimerization
		self.init_anim = gg.polimerization_init
		self.anim = gg.polimerization_anim
		self.anim_len = len(self.anim)
		self.init_anim_len = len(self.init_anim)
		self.anim_reload = 200
		self.anim_speed = 10
		self.init_anim_speed = 3

		self.background = gg.polimerization_background

class game_manager():
	all_enemys = [enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6, enemy_7, enemy_8, enemy_9]
	def __init__(self):

		black_off()

		self.matrix_x = 10
		self.matrix_y = 10

		self.player_gun = gun7
		self.player_gun_mod = 0
		self.player_health = 3
		self.fuel = 999

		self.resours1 = 999
		self.resours2 = 999
		self.resours3 = 999

		#self.green_energy = False
		#self.polimerization = False
		#self.compas = False
		self.compas_init = True
		#self.hable = False
		#self.boost_engine = False

		self.highteck_ups = [False, False, False, False, False]#[self.green_energy, self.polimerization, self.compas, self.hable, self.boost_engine]
		self.highteck_ups_visual = [hitec_green_energy_visual, hitec_polimerization_visual, hitec_compas_visual, hitec_hable_visual, hitec_boosted_engine_visual]#[green_energy_vis, polimerization_vis, compas_vis, hable_vis, boost_engine_vis]

		self.all_enemys = [enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6, enemy_7, enemy_8, enemy_9]

		self.game_surface_scale = game_surface_scale()

		self.press_timer = 0

		self.action_lvl_now = False

		self.lvl_changed = True

		self.player_on_map_rotate = 270

		self.player_vis_lvl = [] #player_visible_lvl

		self.f_lvl = create_lvl_matrix(self.matrix_x,self.matrix_y, 1)
		self.s_lvl = create_lvl_matrix(self.matrix_x,self.matrix_y, 2)
		self.t_lvl = create_lvl_matrix(self.matrix_x,self.matrix_y, 3)

		self.all_lvls = [self.f_lvl, self.s_lvl, self.t_lvl]
		self.all_lvl_counter = 0

		self.lvl_matrix = self.f_lvl[0]
		self.player_vis_lvl = self.f_lvl[1]

		updateble_objects_m.objects.append(self)

		self.background_m = background_manager()

		self.matrix_plates_list = []
		self.matrix_plates_in_draw_distance_list = []

		build_visual_lvl_matrix(self.player_vis_lvl, self.player_on_map_rotate, self)

		self.focus_offset = focus_offset(self)

		self.hitec_anim_m = hitec_anim_manager(self)

		self.mouse = mouse()

		self.info_panel = info_panel()

		self.controls_block = False

		self.move_left = False
		self.move_right = False
		self.move_up = False
		self.move_down = False

		#self.game_main_menu_button = game_main_menu_button()
		self.pause_menu_created = False

	def update(self):
		
		self.move_left = False
		self.move_right = False
		self.move_up = False
		self.move_down = False

		press = pygame.key.get_pressed()
		if press[pygame.K_w] and self.controls_block == False:
			self.move_up = True
		if press[pygame.K_s] and self.controls_block == False:
			self.move_down = True
		if press[pygame.K_d] and self.controls_block == False:
			self.move_right = True
		if press[pygame.K_a] and self.controls_block == False:
			self.move_left = True

		self.background_m.update()

		if self.fuel <= 0:
			self.kill()
			updateble_objects_m.objects.remove(self)


		if press[pygame.K_ESCAPE] and self.press_timer <= 0 and self.action_lvl_now == False:
			self.press_timer = 20
			if self.pause_menu_created == False:
				self.pause_menu_created = True
				self.controls_block = True
				self.game_main_menu_button = game_main_menu_button()
			elif self.pause_menu_created == True:
				self.controls_block = False
				self.game_main_menu_button.kill()
				self.pause_menu_created = False

		if self.press_timer > 0 and self.action_lvl_now == False:
			self.press_timer -= 1
		if self.action_lvl_now == False:
			if self.move_right and self.press_timer <= 0:
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

									self.fuel -= 1

								if self.lvl_matrix[y][x+1] == 1 or self.lvl_matrix[y][x+1] == 2 or self.lvl_matrix[y][x+1] == 3: #triger for event

									black_on(self.create_mechanic_window, args = (self.lvl_matrix[y][x+1], self))

									self.controls_block = True

									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y][x+1] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y][x+1] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 270

									self.fuel -= 1

								if type(self.lvl_matrix[y][x+1]) == tuple:

									black_on(self.create_action_lvl, args = (self, self.get_enemy_name(self.lvl_matrix[y][x+1])))

									self.controls_block = True

									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y][x+1] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y][x+1] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 270

									self.fuel -= 1

								if self.lvl_matrix[y][x+1] == 11:
									black_on(self.change_lvl, args = None)

									self.fuel -= 1
									self.controls_block = True
									done = 1

								if self.lvl_matrix[y][x+1] == 12:
									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y][x+1] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y][x+1] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 270

									self.fuel -= 1

									randnum = random.randint(0,4)
									if self.highteck_ups[randnum] == False:
										self.highteck_ups[randnum] = True
										self.hitec_anim_m.to_create_list.append(self.highteck_ups_visual[randnum])
									else:
										index = 0
										for i in self.highteck_ups:
											if i == False:
												self.highteck_ups[index] = True
												self.hitec_anim_m.to_create_list.append(self.highteck_ups_visual[index])
												break
											index += 1

									done = 1
							
							break
						x += 1

					if done == 1:
						break
					y += 1

				#for i in self.player_vis_lvl:
				#	print(str(i))

			if self.move_left and self.press_timer <= 0:
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

									self.fuel -= 1

								if self.lvl_matrix[y][x-1] == 1 or self.lvl_matrix[y][x-1] == 2 or self.lvl_matrix[y][x-1] == 3: #triger for event

									black_on(self.create_mechanic_window, args = (self.lvl_matrix[y][x-1], self))

									self.controls_block = True

									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y][x-1] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y][x-1] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 90

									self.fuel -= 1

								if type(self.lvl_matrix[y][x-1]) == tuple:

									black_on(self.create_action_lvl, args = (self, self.get_enemy_name(self.lvl_matrix[y][x-1])))

									self.controls_block = True

									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y][x-1] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y][x-1] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 90

									self.fuel -= 1

								if self.lvl_matrix[y][x-1] == 11:
									black_on(self.change_lvl, args = None)

									self.fuel -= 1
									self.controls_block = True
									done = 1

								if self.lvl_matrix[y][x-1] == 12:
									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y][x-1] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y][x-1] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 90

									self.fuel -= 1

									randnum = random.randint(0,4)
									if self.highteck_ups[randnum] == False:
										self.highteck_ups[randnum] = True
										self.hitec_anim_m.to_create_list.append(self.highteck_ups_visual[randnum])
									else:
										index = 0
										for i in self.highteck_ups:
											if i == False:
												self.highteck_ups[index] = True
												self.hitec_anim_m.to_create_list.append(self.highteck_ups_visual[index])
												break
											index += 1

									done = 1


							break
						x += 1

					if done == 1:
						break
					y += 1

				#for i in self.player_vis_lvl:
				#	print(str(i))

			if self.move_up and self.press_timer <= 0:
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
									self.fuel -= 1

								if self.lvl_matrix[y-1][x] == 1 or self.lvl_matrix[y-1][x] == 2 or self.lvl_matrix[y-1][x] == 3: #triger for event

									black_on(self.create_mechanic_window, args = (self.lvl_matrix[y-1][x], self))

									self.controls_block = True

									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y-1][x] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y-1][x] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 0
									self.fuel -= 1


								if type(self.lvl_matrix[y-1][x]) == tuple:

									black_on(self.create_action_lvl, args = (self, self.get_enemy_name(self.lvl_matrix[y-1][x])))

									self.controls_block = True

									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y-1][x] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y-1][x] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 0
									self.fuel -= 1


								if self.lvl_matrix[y-1][x] == 11:
									black_on(self.change_lvl, args = None)

									self.fuel -= 1
									self.controls_block = True
									done = 1

								if self.lvl_matrix[y-1][x] == 12:
									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y-1][x] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y-1][x] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 0

									self.fuel -= 1

									randnum = random.randint(0,4)
									if self.highteck_ups[randnum] == False:
										self.highteck_ups[randnum] = True
										self.hitec_anim_m.to_create_list.append(self.highteck_ups_visual[randnum])
									else:
										index = 0
										for i in self.highteck_ups:
											if i == False:
												self.highteck_ups[index] = True
												self.hitec_anim_m.to_create_list.append(self.highteck_ups_visual[index])
												break
											index += 1

									done = 1

							break
						x += 1

					if done == 1:
						break
					y += 1

				#for i in self.player_vis_lvl:
				#	print(str(i))

			if  self.move_down and self.press_timer <= 0:
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

									self.fuel -= 1

								if self.lvl_matrix[y+1][x] == 1 or self.lvl_matrix[y+1][x] == 2 or self.lvl_matrix[y+1][x] == 3: #triger for event

									black_on(self.create_mechanic_window, args = (self.lvl_matrix[y+1][x], self))

									self.controls_block = True

									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y+1][x] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y+1][x] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 180

									self.fuel -= 1

								if type(self.lvl_matrix[y+1][x]) == tuple:

									black_on(self.create_action_lvl, args = (self, self.get_enemy_name(self.lvl_matrix[y+1][x])))

									self.controls_block = True

									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y+1][x] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y+1][x] = "p"

									self.lvl_changed = True
									done = 1

									self.fuel -= 1

									self.player_on_map_rotate = 180

								if self.lvl_matrix[y+1][x] == 11:
									black_on(self.change_lvl, args = None)

									self.fuel -= 1
									self.controls_block = True

									done = 1

								if self.lvl_matrix[y+1][x] == 12:
									self.lvl_matrix[y][x] = 0				
									self.lvl_matrix[y+1][x] = "p"

									self.player_vis_lvl[y][x] = 0
									self.player_vis_lvl[y+1][x] = "p"

									self.lvl_changed = True
									done = 1

									self.player_on_map_rotate = 270

									self.fuel -= 1

									randnum = random.randint(0,4)
									if self.highteck_ups[randnum] == False:
										self.highteck_ups[randnum] = True
										self.hitec_anim_m.to_create_list.append(self.highteck_ups_visual[randnum])
									else:
										index = 0
										for i in self.highteck_ups:
											if i == False:
												self.highteck_ups[index] = True
												self.hitec_anim_m.to_create_list.append(self.highteck_ups_visual[index])
												break
											index += 1

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
					if self.highteck_ups[2]:
						if y == 0 and x == 0:
							self.compas_init = True
						if self.compas_init == True:
							if element == 1 or element == 2 or element == 3:
								self.player_vis_lvl[y][x] = 13
							if y == self.matrix_y - 1 and x == self.matrix_x - 1:
								self.compas_init = False

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

					if self.highteck_ups[3] == True:
						if 0 <= x < self.matrix_x - 2:
							if self.lvl_matrix[y][x+2] == "p":
								self.player_vis_lvl[y][x] = element

						if 1 < x <= self.matrix_x - 1:
							if self.lvl_matrix[y][x-2] == "p":
								self.player_vis_lvl[y][x] = element

						if 0 <= y < self.matrix_y - 2:
							if self.lvl_matrix[y+2][x] == "p":
								self.player_vis_lvl[y][x] = element

						if 1 < y <= self.matrix_y - 1:
							if self.lvl_matrix[y-2][x] == "p":
								self.player_vis_lvl[y][x] = element

						if 0 <= x < self.matrix_x - 2 and 0 < y <= self.matrix_y - 1:
							if self.lvl_matrix[y-1][x+2] == "p":
								self.player_vis_lvl[y][x] = element

						if 0 <= x < self.matrix_x - 2 and 0 <= y < self.matrix_y - 1:
							if self.lvl_matrix[y+1][x+2] == "p":
								self.player_vis_lvl[y][x] = element

						if 1 < x <= self.matrix_x - 1 and 0 < y <= self.matrix_y - 1:
							if self.lvl_matrix[y-1][x-2] == "p":
								self.player_vis_lvl[y][x] = element

						if 1 < x <= self.matrix_x - 1 and 0 <= y < self.matrix_y - 1:
							if self.lvl_matrix[y+1][x-2] == "p":
								self.player_vis_lvl[y][x] = element

						if 0 <= y < self.matrix_y - 2 and 0 < x <= self.matrix_x - 1:
							if self.lvl_matrix[y+2][x-1] == "p":
								self.player_vis_lvl[y][x] = element

						if 0 <= y < self.matrix_y - 2 and 0 <= x < self.matrix_x - 1:
							if self.lvl_matrix[y+2][x+1] == "p":
								self.player_vis_lvl[y][x] = element

						if 1 < y <= self.matrix_y - 1 and 0 < x <= self.matrix_x - 1:
							if self.lvl_matrix[y-2][x-1] == "p":
								self.player_vis_lvl[y][x] = element

						if 1 < y <= self.matrix_y - 1 and 0 <= x < self.matrix_x - 1:
							if self.lvl_matrix[y-2][x+1] == "p":
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
		post_processing_m.objects.remove(self.info_panel)
		post_processing_m.objects.remove(self.game_surface_scale)
		post_processing_m.objects.remove(self.mouse)
		#updateble_objects_m.objects.remove(self.background_m)
		post_processing_m.objects.remove(self.hitec_anim_m)

		for i in all_sprites:
			i.kill()

	def append(self):
		post_processing_m.objects.append(self.game_surface_scale)
		updateble_objects_m.objects.append(self.focus_offset)
		self.hitec_anim_m = hitec_anim_manager(self)
		post_processing_m.objects.append(self.info_panel)
		post_processing_m.objects.append(self.mouse)
		#updateble_objects_m.objects.append(self.background_m)
		#update_visual_lvl_matrix(self.player_vis_lvl, self.player_on_map_rotate, self)
		self.controls_block = False


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
			if absolute_number(absolute_number(i.rect.x) - x) < 340 and absolute_number(absolute_number(i.rect.y) - y) < 200:
				self.matrix_plates_in_draw_distance_list.append(i)

	def change_lvl(self):
		self.all_lvl_counter += 1
		self.lvl_matrix = self.all_lvls[self.all_lvl_counter][0]
		self.player_vis_lvl = self.all_lvls[self.all_lvl_counter][1]

		self.focus_offset.offset_x = 0
		self.focus_offset.offset_y = 0

		self.compas_init = False

		self.matrix_plates_list = []
		build_visual_lvl_matrix(self.player_vis_lvl, self.player_on_map_rotate, self)
		#update_visual_lvl_matrix(self.player_vis_lvl, self.player_on_map_rotate, self)
		self.lvl_changed = True
		self.controls_block = False

	def create_mechanic_window(self, args):
		self.action_lvl_now = True
		self.kill()				
		self.mechanic_upgrade = mechanic_upgrade_window(args[0], args[1])     #(self.lvl_matrix[y][x+1], self)

	def create_action_lvl(self, args):
		self.action_lvl_now = True
		self.kill()				
		self.action_lvl = action_lvl(args[0], args[1]) #(self, self.get_enemy_name(self.lvl_matrix[y+1][x]))

	def go_to_main_menu(self):
		updateble_objects_m.objects.remove(self.focus_offset)
		post_processing_m.objects.remove(self.info_panel)
		post_processing_m.objects.remove(self.game_surface_scale)
		post_processing_m.objects.remove(self.mouse)
		#updateble_objects_m.objects.remove(self.background_m)
		post_processing_m.objects.remove(self.hitec_anim_m)

		for i in all_sprites:
			i.kill()

		updateble_objects_m.objects.remove(self)
		global main_m
		main_m = main_menu()

class game_main_menu_button(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((168, 80))
		self.image.fill((26,37, 36))
		self.rect = self.image.get_rect()
		self.rect.x = width / 2
		self.rect.y = height / 2
		draw_text(self.image, "MEIN MENU", 30, self.rect.width/2, self.rect.height/2, (255,255,255))
		all_sprites.add(self)
	def update(self):
		self.rect.x = width / 2
		self.rect.y = height / 2
		if self.rect.colliderect(game.mouse):
			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						black_on(game.go_to_main_menu, None)
						self.kill()
	
class main_menu():
	def __init__(self):
		self.mouse = mouse()
		updateble_objects_m.objects.append(self)

		self.background_to_spawn = [gg.star1, gg.star2, gg.star3, gg.enemy_1, gg.enemy_2, gg.enemy_3, gg.enemy_4, gg.enemy_5, gg.enemy_6, gg.enemy_7, gg.enemy_8, gg.enemy_9, gg.enemy_4_rocket]
		self.background_objs = []

		self.but_quit = menu_quit_button()
		self.but_start = menu_start_button()

	def update(self):
		if len(self.background_objs) <= 10:
			self.background_objs.append((random.choice(self.background_to_spawn), [random.randint(0, 599), random.randint(-400, -100)], (random.randint(2, 10))))

		for i in self.background_objs:
			if i[1][1] > height:
				self.background_objs.remove(i)

			i[1][1] += i[2]
			game_surface.blit(i[0], (i[1][0], i[1][1]))
		game_surface.blit(gg.main_menu_img, (0,0))


	def create_game(self):
		for i in all_sprites:
			i.kill()
		post_processing_m.objects.remove(self.mouse)
		global game
		game = game_manager()
		updateble_objects_m.objects.remove(self)


class menu_quit_button(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((134, 62))
		self.image.fill((26,37, 36))
		self.rect = self.image.get_rect()
		self.rect.x =  154  
		self.rect.y = 286
		draw_text(self.image, "QUIT", 30, self.rect.width/2, self.rect.height/2, (255,255,255))
		all_sprites.add(self)
	def update(self):
		if self.rect.colliderect(main_m.mouse):
			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						global running
						running = False


class menu_start_button(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((168, 80))
		self.image.fill((26,37, 36))
		self.rect = self.image.get_rect()
		self.rect.x = 26  
		self.rect.y = 34
		draw_text(self.image, "START", 30, self.rect.width/2, self.rect.height/2, (255,255,255))
		all_sprites.add(self)
	def update(self):
		if self.rect.colliderect(main_m.mouse):
			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						black_on(main_m.create_game, None)

updateble_objects_m = updateble_objects_manager()
post_processing_m = post_processing_manager()

main_m = main_menu()


events = []

running = True
while running:
	clock.tick(fps)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				#running = False
				pass
		events.append(event)
	
	game_surface = pygame.Surface((width, height))
	game_surface.fill((13, 13, 35))
	updateble_objects_m.update()
	all_sprites.update()
	all_sprites.draw(game_surface)
	post_processing_m.update()

	fullscreen_with_ratio()

	real_fps = int(clock.get_fps())

	#draw_text(window, str(real_fps), 20, 100, 40, (255,255,255))
	#draw_text(window, str(len(game.matrix_plates_list)), 10, 600, 40, (255,255,255))
	#draw_text(window, str(updateble_objects_m.objects), 10, 600, 50, (255,255,255))
	#draw_text(window, str(post_processing_m.objects), 10, 600, 60, (255,255,255))
	#draw_text(window, str(events), 10, 600, 70, (255,255,255))
	#draw_text(window, str(game.action_lvl_now), 10, 600, 80, (255,255,255))

	events = []	

	pygame.display.flip()