import tkinter

class Canvas(object):
	def __init__(self, master, width=22, height=80, bg='white'):
		self.canvas = tkinter.Canvas(
				master = master,
				width = width,
				height = height,
				bg = bg,
			)

		self.canvas.pack(fill=tkinter.BOTH, side=tkinter.LEFT)

	def destroy(self):
		self.canvas.destroy()
