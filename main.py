import pygame as py
from algrothim import BubbleSort
import numpy as np

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

app = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = py.time.Clock()

arr = np.random.randint(0, 100, 30)

bubbleSort = BubbleSort(arr, height_multiplier=5, window_size=app.get_size())


while True:
    for ev in py.event.get():
        if ev.type == py.QUIT:
            py.quit()
            exit()
        if ev.type == py.KEYDOWN:
            if ev.key == py.K_ESCAPE:
                py.quit()
                exit()
            if ev.key == py.K_s:
                bubbleSort.sort()
            if ev.key == py.K_r:
                arr = np.random.randint(0, 100, 30)
                bubbleSort.update(arr)
            if ev.key == py.K_n:
                bubbleSort.next_step()
            if ev.key == py.K_g:
                bubbleSort.sorting_is_paused = (
                    False if bubbleSort.sorting_is_paused else True
                )

    app.fill(120)
    clock.tick(bubbleSort.speed)

    bubbleSort.run_sorting()

    bubbleSort.draw(app, py)

    py.display.flip()
