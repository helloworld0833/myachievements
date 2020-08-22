import tkinter

class Frame(object):
	def __init__(self, master, bg='white', width=80, height=80, side=tkinter.LEFT):
		self.frame = tkinter.Frame(
				master = master,
				width = width,
				height = height,
				bg = bg,
			)

		self.frame.pack(fill=tkinter.BOTH, side=side, expand=True)

	def destroy(self):
		self.frame.destroy()
