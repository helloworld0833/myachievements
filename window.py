import tkinter

from frame import Frame
from text_box import TextBox

class Window(object):
	def __init__(self, className):
		self.window = tkinter.Tk(className=className)

		self.dashboard_frame = Frame(master=self.window)
		self.recent_frame = Frame(master=self.window)
		self.random_frame = Frame(master=self.window)

		self.dashboard_frame_text = TextBox(master=self.dashboard_frame.frame, file_name='dashboard.txt', window=self, state='normal', mode='dashboard')
		self.recent_frame_text = TextBox(master=self.recent_frame.frame, file_name='complete.txt', window=self, mode='recent')
		self.random_frame_text = TextBox(master=self.random_frame.frame, file_name='complete.txt', window=self, mode='random')

	def refresh(self):
		self.dashboard_frame_text.destroy()
		self.recent_frame_text.destroy()
		self.random_frame_text.destroy()

		self.dashboard_frame_text = TextBox(master=self.dashboard_frame.frame, file_name='dashboard.txt', window=self, state='normal', mode='dashboard')
		self.recent_frame_text = TextBox(master=self.recent_frame.frame, file_name='complete.txt', window=self, mode='recent')
		self.random_frame_text = TextBox(master=self.random_frame.frame, file_name='complete.txt', window=self, mode='random')

	def start(self):
		self.window.mainloop()
