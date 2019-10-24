import math
import tkinter as tk


a45 = math.pi / 4
a135 = 3 * math.pi / 4
s45 = math.sin(a45)
c45 = math.cos(a45)
s135 = math.sin(-a45)
c135 = math.cos(-a45)
sqrt2 = math.sqrt(2)


def scale(ps):
    res = []
    # print('before => ', ps)
    for i in range(int(len(ps) / 2)):
        res.append(int(ps[i * 2] * scale_x + shift_x))
        res.append(int(ps[i * 2 + 1] * scale_y + shift_y))
    # print('after => ', res)
    return res



def draw_line(canvas, points, color='white', width=1):
    canvas.create_line(points, width=width, fill=color)


def curve(points):
    result = []
    base_x = 0
    base_y = 0
    for i in range(int(len(points) / 2)):
        x = points[i * 2] - base_x
        y = points[i * 2 + 1] - base_y
        if i % 2 == 0:
            nx = (x * c45 - y * s45) / sqrt2
            ny = (x * s45 + y * c45) / sqrt2
        else:
            nx = (x * c135 - y * s135) / sqrt2
            ny = (x * s135 + y * c135) / sqrt2

        result += [nx + base_x, ny + base_y, x + base_x, y + base_y]
        base_x = x + base_x
        base_y = y + base_y

    return result


def animation(canvas):
    points = [1, 0]
    pixels = scale([0, 0] + points)
    draw_line(canvas, pixels, color='yellow')
    for i in range(16):
        # print('anime', points)
        canvas.update()
        canvas.after(200)
        draw_line(canvas, pixels, color='black')
        canvas.update()
        points = curve(points)
        pixels = scale([0, 0] + points)
        draw_line(canvas, pixels, color='yellow')


root = tk.Tk()
root.state('zoomed')

c = tk.Canvas(root, bg='black')
c.pack(fill=tk.BOTH, expand=True)
root.update()
root.focus_set()
root.bind("<Escape>", lambda e: root.destroy())

w = c.winfo_width()
h = c.winfo_height()

scale_x = int((w - 300) * 0.6)
scale_y = scale_x

shift_x = 500
shift_y = int(h / 3)

print(w, h)

animation(c)

root.mainloop()



