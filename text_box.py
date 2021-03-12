import tkinter
import random

from frame import Frame
from button import ButtonDone, ButtonCancel, ButtonAdd
from utilities import parser, deparser

class TextBox(object):
	def __init__(self, master, file_name, window, state='disabled', mode=None):
		self.master = master
		self.window = window
		self.mode = mode

		with open(file_name, 'ab+') as f:
			f.seek(0)
			lines = self._preprocess(parser(f.read()))

		self.text_box = tkinter.Text(
				master = master,
				width = 58,
				height = len(lines)+1,
				bd = 0,
			)

		self.text_box.pack(side=tkinter.LEFT, expand=True)

		self.text_box.insert('1.0', ''.join(lines))

		self.text_box.config(state=state)

		if mode == 'dashboard':
			self.assign_button(len(lines))

	def _preprocess(self, lines):
		if self.mode == 'recent':
			return ['achievement points {}\n\n'.format(len(lines)*10)]+lines[-20:]
		elif self.mode == 'random':
			if len(lines) <= 20:
				return lines

			random.seed()

			res, my_set = [], set()
			while len(res) < 20:
				idx = random.randrange(0, len(lines))
				if idx not in my_set:
					my_set.add(idx)
					res.append(lines[idx])

			return res
		elif self.mode == 'dashboard':
			res = []
			for idx, line in enumerate(lines):
				res.append('{}.{}'.format(idx+1, line))

			return res

	def assign_button(self, nums):
		self.button_frame_list = []
		self.button_done_list, self.button_cancel_list = [], []
		for idx in range(nums):
			button_frame = Frame(master=self.master, width=22, height=1, side=tkinter.TOP)
			self.button_frame_list.append(button_frame)
			self.button_done_list.append(ButtonDone(id=idx, master=button_frame.frame, text='{}.done'.format(idx+1), text_box=self, window=self.window))
			self.button_cancel_list.append(ButtonCancel(id=idx, master=button_frame.frame, text='{}.cancel'.format(idx+1), text_box=self, window=self.window))

		self.button_add = ButtonAdd(master=self.master, text_box=self, window=self.window)

	def destroy(self):
		if self.mode == 'dashboard':
			self.button_add.destroy()

			for button_done in self.button_done_list:
				button_done.destroy()

			for button_cancel in self.button_cancel_list:
				button_cancel.destroy()

			for button_frame in self.button_frame_list:
				button_frame.destroy()

		self.text_box.destroy()
