import tkinter
import random

from frame import Frame
from button import ButtonDone, ButtonCancel, ButtonAdd
from utilities import parser, deparser

class TextBoxCreater(object):
	def __init__(self, master, file_name, state='disabled', mode=None, assign_button=False):
		self.master = master

		with open(file_name, 'br') as f:
			lines = self._preprocess(parser(f.read()), mode)

		self.text_box = tkinter.Text(
				master = master,
				width = 58,
				height = len(lines)+1,
				bd = 0,
			)

		self.text_box.pack(side=tkinter.LEFT, expand=True)

		self.text_box.insert('1.0', ''.join(lines))

		self.text_box.config(state=state)

		if assign_button:
			self.assign_button(len(lines))

	def _preprocess(self, lines, mode):
		if mode == 'recent':
			return ['achievements points {}\n\n'.format(len(lines)*10)]+lines[-10:]
		elif mode == 'random':
			if len(lines) <= 10:
				return lines

			random.seed()

			res, my_set = [], set()
			while len(res) < 10:
				idx = random.randrange(0, len(lines))
				if idx not in my_set:
					my_set.add(idx)
					res.append(lines[idx])

			return res
		elif not mode:
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
			self.button_done_list.append(ButtonDone(id=idx, master=button_frame.frame, text='{}.done'.format(idx+1), text_box_creater=self))
			self.button_cancel_list.append(ButtonCancel(id=idx, master=button_frame.frame, text='{}.cancel'.format(idx+1), text_box_creater=self))

		self.button_add = ButtonAdd(master=self.master, text_box_creater=self)
