import pygame, math
pygame.init()

sc = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()

path = "/home/eugene/Документы/Programming/git/2551_open3dmodel/dante_naked/dante_naked.obj"
size = 100

m_pos = pygame.Vector3([sc.get_width()//2, sc.get_height()//2, 1000])

y_a = 0.05
z_a = 0.05
x_a = 0.05

def get_polygons(path):
	polys = []
	with open(path, 'r') as f:
		for n, i in enumerate(f.read().split("\n")):
			if i.split(" ")[0] == "f":
				point = i.split(" ")[1:4]
				
				polygons = list(map(lambda x: int(x.split("/")[1]), point))
				polys.append(polygons)
	print(len(polys))
	return polys

def get_points(path):
	points = []
	with open(path, 'r') as f:
		for i in f.read().split("\n"):
			if i.split(" ")[0] == "v":
				point = list(map(lambda x: float(x)*size, i.split(" ")[1:4]))
				point[1] = m_pos[1] - point[1]
				points.append(pygame.Vector3(point))
	print(len(points))
	return points

pos = get_points(path)
polys = get_polygons(path)

def rotated_y(p, a):
	x = p[0]*math.cos(a)+p[2]*math.sin(a)
	y = p[1]
	z = -p[0]*math.sin(a)+p[2]*math.cos(a)
	return x, y, z

def rotated_x(p, a):
	x = p[0]
	y = p[1]*math.cos(a)+p[2]*math.sin(a)
	z = -p[1]*math.sin(a)+p[2]*math.cos(a)
	return x, y, z

def rotated_z(p, a):
	x = p[0]*math.cos(a)-p[1]*math.sin(a)
	y = p[0]*math.sin(a)+p[1]*math.cos(a)
	z = p[2]
	return x, y, z

def return_2D_proection_z_obsyss(pos, start=(0, 0, 0)):
	dist = start[2]
	ox = start[0]+pos[0]*dist/(pos[2]+dist)
	oy = start[1]+pos[1]*dist/(pos[2]+dist)
	return ox, oy

while True:
	[exit() for i in pygame.event.get() if i.type == pygame.QUIT]
	clock.tick(30)
	sc.fill((0, 0, 0))
	for n, i in enumerate(pos, 0):
		func = return_2D_proection_z_obsyss
		pygame.draw.circle(sc, (255,255,255), func(i, m_pos), 1)

		# pygame.draw.line(sc, (255, 0, 0), return_2D_proection_z_obsyss(i, m_pos), return_2D_proection_z_obsyss(pos[n], m_pos))
	keys = pygame.key.get_pressed()
	if keys[pygame.K_y]:
		for n, i in enumerate(pos):
			pos[n] = rotated_y(i, y_a)
	if keys[pygame.K_x]:
		for n, i in enumerate(pos):
			pos[n] = rotated_x(i, x_a)
	if keys[pygame.K_z]:
		for n, i in enumerate(pos):
			pos[n] = rotated_z(i, z_a)
	if keys[pygame.K_UP]:
		for n, i in enumerate(pos):
			pos[n] += pygame.Vector3((0, 10, 0))
	if keys[pygame.K_DOWN]:
		for n, i in enumerate(pos):
			pos[n] += pygame.Vector3((0, -10, 0))
	if keys[pygame.K_LEFT]:
		for n, i in enumerate(pos):
			pos[n] += pygame.Vector3((10, 0, 0))
	if keys[pygame.K_RIGHT]:
		for n, i in enumerate(pos):
			pos[n] += pygame.Vector3((-10, 0, 0))
	if keys[pygame.K_EQUALS]:
		for n, i in enumerate(pos):
			pos[n] += pygame.Vector3((0, 0, -10))
	if keys[pygame.K_MINUS]:
		for n, i in enumerate(pos):
			pos[n] += pygame.Vector3((0, 0, 10))

	pygame.display.update()