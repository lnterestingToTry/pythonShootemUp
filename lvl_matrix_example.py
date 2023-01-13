import random

lvl = []

print("x=")
lvl_x = int(input())
print("y=")
lvl_y = int(input())

player_vis_lvl = [] #player_visible_lvl
for i in range(0, lvl_y):
	line = []
	for i in range(0,lvl_x):
		line.append(0)
	player_vis_lvl.append(line)

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
lvl[int(lvl_y / 2)][int(lvl_x / 2)] = (11, 12)

class create_ekshn_lvl():
	def __init__(self, enemys, kill_count):
		self.enemys = enemys
		self.kill_count = kill_count

for i in lvl:
	print(str(i))

run = True
while run:
	press = input()
	if press == "d":
		y = 0
		done = 0
		for line in lvl:
			x = 0
			for element in line:
				if element == "p":
					if 0 <= x < lvl_x - 1:
						if lvl[y][x+1] == 0:
							lvl[y][x] = 0
							lvl[y][x+1] = "p"

							player_vis_lvl[y][x] = 0
							player_vis_lvl[y][x+1] = "p"

							done = 1

						if lvl[y][x+1] == 1: #triger for event
							lvl[y][x] = 0				
							lvl[y][x+1] = "p"

							player_vis_lvl[y][x] = 0
							player_vis_lvl[y][x+1] = "p"

							done = 1					
							print ("event num1 here")	#event

						if type(lvl[y][x+1]) == tuple:
							cel = create_ekshn_lvl(lvl[y][x+1], 10)
							print(cel.enemys)
							lvl[y][x] = 0				
							lvl[y][x+1] = "p"

							player_vis_lvl[y][x] = 0
							player_vis_lvl[y][x+1] = "p"

							done = 1
					break
				x += 1

			if done == 1:
				break
			y += 1

		#for i in player_vis_lvl:
		#	print(str(i))

	if press == "a":
		y = 0
		done = 0
		for line in lvl:
			x = 0
			for element in line:
				if element == "p":
					if 0 < x <= lvl_x - 1:
						if lvl[y][x-1] == 0:
							lvl[y][x] = 0
							lvl[y][x-1] = "p"

							player_vis_lvl[y][x] = 0
							player_vis_lvl[y][x-1] = "p"


							done = 1
						if lvl[y][x-1] == 1: #triger for event
							lvl[y][x] = 0				
							lvl[y][x-1] = "p"

							player_vis_lvl[y][x] = 0
							player_vis_lvl[y][x-1] = "p"

							done = 1					
							print ("event num1 here")	#event
						if type(lvl[y][x-1]) == tuple:
							cel = create_ekshn_lvl(lvl[y][x-1], 10)
							print(cel.enemys)
							lvl[y][x] = 0				
							lvl[y][x-1] = "p"

							player_vis_lvl[y][x] = 0
							player_vis_lvl[y][x-1] = "p"

							done = 1
					break
				x += 1

			if done == 1:
				break
			y += 1

		#for i in player_vis_lvl:
		#	print(str(i))

	if press == "w":
		y = 0
		done = 0
		for line in lvl:
			x = 0
			for element in line:
				if element == "p":
					if 0 < y <= lvl_y - 1:
						if lvl[y-1][x] == 0:
							lvl[y][x] = 0
							lvl[y-1][x] = "p"

							player_vis_lvl[y][x] = 0
							player_vis_lvl[y-1][x] = "p"

							done = 1

						if lvl[y-1][x] == 1: #triger for event
							lvl[y][x] = 0				
							lvl[y-1][x] = "p"

							player_vis_lvl[y][x] = 0
							player_vis_lvl[y-1][x] = "p"

							done = 1					
							print ("event num1 here")	#event
						if type(lvl[y-1][x]) == tuple:
							cel = create_ekshn_lvl(lvl[y-1][x], 10)
							print(cel.enemys)
							lvl[y][x] = 0				
							lvl[y-1][x] = "p"

							player_vis_lvl[y][x] = 0
							player_vis_lvl[y-1][x] = "p"

							done = 1
					break
				x += 1

			if done == 1:
				break
			y += 1

		#for i in player_vis_lvl:
		#	print(str(i))

	if press == "s":
		y = 0
		done = 0
		for line in lvl:
			x = 0
			for element in line:
				if element == "p":
					if 0 <= y < lvl_y - 1:
						if lvl[y+1][x] == 0:
							lvl[y][x] = 0
							lvl[y+1][x] = "p"

							player_vis_lvl[y][x] = 0
							player_vis_lvl[y+1][x] = "p"

							done = 1
						if lvl[y+1][x] == 1: #triger for event
							lvl[y][x] = 0				
							lvl[y+1][x] = "p"

							player_vis_lvl[y][x] = 0
							player_vis_lvl[y+1][x] = "p"

							done = 1	
							print ("event num1 here")	#event
						if type(lvl[y+1][x]) == tuple:
							cel = create_ekshn_lvl(lvl[y+1][x], 10)
							print(cel.enemys)
							lvl[y][x] = 0				
							lvl[y+1][x] = "p"

							player_vis_lvl[y][x] = 0
							player_vis_lvl[y+1][x] = "p"

							done = 1
					break
				x += 1

			if done == 1:
				break
			y += 1

	y = 0
	for line in lvl:
		x = 0
		for element in line:
			if 0 <= x < lvl_x - 1:
				if lvl[y][x+1] == "p":
					player_vis_lvl[y][x] = element

			if 0 < x <= lvl_x - 1:
				if lvl[y][x-1] == "p":
					player_vis_lvl[y][x] = element

			if 0 <= y < lvl_y - 1:
				if lvl[y+1][x] == "p":
					player_vis_lvl[y][x] = element

			if 0 < y <= lvl_y - 1:
				if lvl[y-1][x] == "p":
					player_vis_lvl[y][x] = element

			if 0 < x <= lvl_x - 1 and 0 <= y < lvl_y - 1:
				if lvl[y+1][x-1] == "p":
					player_vis_lvl[y][x] = element

			if 0 < x <= lvl_x - 1 and 0 < y <= lvl_y - 1:
				if lvl[y-1][x-1] == "p":
					player_vis_lvl[y][x] = element

			if 0 <= x < lvl_x - 1 and 0 <= y < lvl_y - 1:
				if lvl[y+1][x+1] == "p":
					player_vis_lvl[y][x] = element

			if 0 <= x < lvl_x - 1 and 0 < y <= lvl_y - 1:
				if lvl[y-1][x+1] == "p":
					player_vis_lvl[y][x] = element



			x += 1
		y += 1


	for i in player_vis_lvl:
		print(str(i))


	if press == "x":
		run = False