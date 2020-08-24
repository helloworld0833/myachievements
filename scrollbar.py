import tkinter

class Scrollbar(object):
	def __init__(self, master, width=28, bg='white', orient='vertical'):
		self.scrollbar = tkinter.Scrollbar(
				master = master,
				width = width,
				bg = bg,
				orient = orient,
			)

		self.scrollbar.pack(fill=tkinter.Y, side=tkinter.RIGHT)

	def destroy(self):
		self.scrollbar.destroy()
