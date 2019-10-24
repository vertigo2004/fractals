import tkinter as tk
import random


def draw_point(canvas, p, color='white', size=1):
    canvas.create_oval(p['x'], p['y'], p['x'] + size, p['y'] + size, fill=color)


def generate(point, i):
    # range −2.1820 < x < 2.6558 and 0 ≤ y < 9.9983.
    return [M[i][0] * point[0] + M[i][1] * point[1] + M[i][4],
            M[i][2] * point[0] + M[i][3] * point[1] + M[i][5]]


def roll_dice():
    prob = 0
    r = random.random()
    for i in range(3):
        prob += P[i]
        if r < prob:
            return i
    return 3


def draw_fern(canvas):
    w = c.winfo_width()
    h = c.winfo_height()
    print(w, h)

    scale_width = w / 20
    scale_height = h / 11
    center_x = w / 2

    p = [0, 0]
    while True:

        pixel = {'x': int(p[0] * scale_width + center_x), 'y': int(h - p[1] * scale_height)}
        draw_point(canvas, pixel, color='green')
        canvas.update()
        p = generate(p, roll_dice())
        # canvas.after(50)

# # ORIGINAL
P = [0.01, 0.85, 0.07, 0.07]             # Probability: sum of all elements must be 1 (one)

M = [
    [0,	0, 0, 0.16, 0, 0],               # Stem
    [0.85, 0.04, -0.04, 0.85, 0, 1.60],  # Successively smaller leaflets
    [0.20, -0.26, 0.23, 0.22, 0, 1.60],  # Largest left-hand leaflet
    [-0.15, 0.28, 0.26, 0.24, 0, 0.44]   # Largest right-hand leaflet
]

# Barnsley fern mutated into a Thelypteridaceae fern.
# P = [0.02, 0.84, 0.07, 0.07]             # Probability: sum of all elements must be 1 (one)
#
# M = [
#     [0, 0,  0,  0.25,   0,  -0.4],
#     [0.95, 0.005, -0.005, 0.93, -0.002, 0.5],
#     [0.035, -0.2, 0.16, 0.04, -0.09, 0.02],
#     [-0.04, 0.2, 0.16, 0.04, 0.083, 0.12]]

root = tk.Tk()
root.state('zoomed')

c = tk.Canvas(root, bg='black')
c.pack(fill=tk.BOTH, expand=True)
root.update()
root.focus_set()
root.bind("<Escape>", lambda e: root.destroy())

draw_fern(c)

root.mainloop()
