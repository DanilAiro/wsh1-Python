# Задание 2.

# Создать прямоугольник с тенью. Тень должна находиться под наклоном. . 
# Прямоугольник с тенью должны двигаться при нажатии на кнопки клавиатуры W, A, S, D.

from tkinter import *

root = Tk()
root.geometry('800x800')
root.title('system32')

canvas = Canvas(root, width=800, height=800)
canvas.pack()
rec = canvas.create_rectangle(50, 50, 200, 200, fill='red')
rec_sh = canvas.create_polygon(50, 200, 200, 200, 250, 250, 100, 250, fill='grey')

def up(event):
  x = 0
  y = -10
  canvas.move(rec, x, y)
  canvas.move(rec_sh, x, y)

def down(event):
  x = 0
  y = 10
  canvas.move(rec, x, y)
  canvas.move(rec_sh, x, y)

def left(event):
  x = -10
  y = 0
  canvas.move(rec, x, y)
  canvas.move(rec_sh, x, y)

def right(event):
  x = 10
  y = 0
  canvas.move(rec, x, y)
  canvas.move(rec_sh, x, y)

def diag(event):
  x = -10
  y = -10
  canvas.move(rec, x, y)
  canvas.move(rec_sh, x, y)

root.bind('w', up)
root.bind('s', down)
root.bind('a', left)
root.bind('d', right)

root.mainloop()

