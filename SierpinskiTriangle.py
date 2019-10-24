import tkinter as tk
import random


active = True


def draw_point(canvas, p, color='white', size=3):
    canvas.create_oval(p['x'], p['y'], p['x'] + size, p['y'] + size, fill=color)


def calculate_midpoint(p1, p2):
    return {'x': (p1['x'] + p2['x']) / 2, 'y': (p1['y'] + p2['y']) / 2}


def set_inactive(event):
    global active
    active = False


def animation(canvas):
    global active
    w = canvas.winfo_width()
    h = canvas.winfo_height()


    print(w, h)
    color = ['red', 'green', 'blue']
    triangle = [{'x': random.randint(int(w / 5 * 2), int(w / 5 * 3)), 'y': random.randint(0, int(h / 5))},
                {'x': random.randint(0, int(w / 5)), 'y': random.randint(int(h / 5 * 4), h)},
                {'x': random.randint(int(w / 5 * 4), w), 'y': random.randint(int(h / 5 * 4), h)}]

    current = {'x': random.randint(0, w), 'y': random.randint(0, h)}

    for p in triangle:
        draw_point(c, p, 'red')

    draw_point(c, current)
    n = 0
    hundred = 0
    text = canvas.create_text(0, 0, text=n, fill='white')

    while active:

        r = random.random()
        if r < 0.333:
            i = 0
        elif r < 0.667:
            i = 1
        else:
            i = 2

        current = calculate_midpoint(current, triangle[i])
        draw_point(canvas, current, color=color[i])

        if n > hundred * 100 + random.randint(0, 100):
            canvas.delete(text)
            text = canvas.create_text(w - 20, 10, text=str(n), fill='white', justify='right')
            hundred = hundred + 2

        canvas.update()

        n = n + 1


root = tk.Tk()
root.state('zoomed')

c = tk.Canvas(root, bg='black')
c.pack(fill=tk.BOTH, expand=True)
root.update()
root.focus_set()



root.bind("<space>", set_inactive)
root.bind("<Escape>", lambda e: root.destroy())

animation(c)

root.mainloop()
