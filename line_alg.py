from __future__ import division
import pygame, sys, math
from pygame.locals import *
def main():
	displaySurface = pygame.display.set_mode((500, 500))
	displaySurface.fill((255, 255, 255))
	x1 = 20
	y1 = 10
	x2 = 30
	y2 = 18
	pygame.draw.line(displaySurface, (255, 0, 0),[x1,y1], [x2,y2])
	pygame.draw.line(displaySurface, (255, 0, 0),[100,10], [10,100])
	pygame.draw.line(displaySurface, (255, 0, 0),[100, 10], [100, 100])
	pygame.draw.line(displaySurface, (255, 0, 0),[10, 100], [100, 100])
	draw_line(displaySurface, x1, y1, x2, y2)
	draw_line_dda(displaySurface, 100, 10, 10, 100)
	draw_line_bres(displaySurface, 100, 10, 100, 100)
	draw_line_bres(displaySurface, 10, 100, 100, 100)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()

def draw_line(surface, x1, y1, x2, y2, color=(255, 0, 0)):
	dx = x2 - x1
	dy = y2 - y1
	surface.set_at((x1, y1), color)
	if(dx == 0):
		if y2 > y1:
			stepY = 1
		elif y2 < y1:
			stepY = -1
		while y1 != y2:
			y1 += stepY
			surface.set_at((x1, y1), color)
	else:
		m = float(dy) / float(dx)
		b = y1 - (m * x1)
		if x2 > x1:
			stepX = 1
		elif x2 < x1:
			stepX = -1
		while x1 != x2:
			x1 += stepX
			y1 = int(m * x1 + b)
			surface.set_at((x1, y1), color)

def draw_line_dda(surface, x1, y1, x2, y2, color=(0, 255, 0)):
	
	dy = y2 - y1
	dx = x2 - x1
	if abs(dx) > abs(dy):
	    steps = dx
	else:
	    steps = dy
	xIncrement = float(dx) / float(steps)
	yIncrement = float(dy) / float(steps)
	surface.set_at((x1, y1), color)
	for i in range(steps):
	    x1 += xIncrement
	    y1 += yIncrement
	    surface.set_at((int(round(x1)), int(round(y1))), color)

def draw_line_bres(surface, x1, y1, x2, y2, color=(0, 0, 255)):
    dy = y2 - y1
    dx = x2 - x1
    stepY = -1 if dy < 0 else 1
    dy = math.fabs(dy)
    stepX = -1 if dx < 0 else 1
    dx = math.fabs(dx)

    if dx > dy:
        p = 2 * dy - dx
        incE = 2 * dy
        incNE = 2 * (dy - dx)
        x = x1
        y = y1
        xEnd = x2
        stepX = 1
    	surface.set_at((x,y), color)
        while x != xEnd:
            x += stepX
            if p < 0:
                p += incE
            else:
                p += incNE
                y += stepY
    	    surface.set_at((x,y), color)
    else:
        p = 2 * dx - dy
        incE = 2 * dx
        incNE = 2 * (dx - dy)
        x = x1
        y = y1
        yEnd = y2
        stepY = 1
        surface.set_at((x, y), color)
        while y != yEnd:
            y += stepY
            if p < 0:
                p += incE
            else:
                p += incNE
                x += stepX
            surface.set_at((x, y), color)

if __name__ == '__main__':
	main()
