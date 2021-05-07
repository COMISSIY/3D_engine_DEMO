import pygame, math
pygame.init()

sc = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

points = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1),	(1, 1, 1), (0, 1, 1)]
pos = [[i[0]*100, i[1]*100, i[2]*100] for i in points]
y_a = 0.01
z_a = 0.01
x_a = 0.01

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
	for n, i in enumerate(pos, -1):
		m_pos = (300, 200, 500)
		pygame.draw.circle(sc, (255,255,255), return_2D_proection_z_obsyss(i, m_pos), 5)
		pygame.draw.line(sc, (255, 0, 0), (return_2D_proection_z_obsyss(i, m_pos)), return_2D_proection_z_obsyss(pos[n], m_pos))
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

	pygame.display.update()