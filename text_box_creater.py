import tkinter
import random

from frame_creater import FrameCreater
from button import ButtonDone, ButtonCancel, ButtonAdd
from utilities import parser

class TextBoxCreater(object):
	def __init__(self, master, file_name, state='disabled', mode=None, assign_button=False):
		self.master = master

		with open(file_name, 'br') as f:
			lines = parser(f.read())
			if mode:
				lines = self._preprocess(lines, mode)

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
			return lines[-10:]
		elif mode == 'random':
			if len(lines) <= 10:
				return lines

			random.seed()

			res, my_set = [], set()
			while len(res) < 10:
				idx = random.randrange(0, len(lines)-1)
				if idx not in my_set:
					my_set.add(idx)
					res.append(lines[idx])

			return res

	def assign_button(self, nums):
		self.frame_creater4_list = []
		self.button_done_list, self.button_cancel_list = [], []
		for idx in range(nums):
			frame_creater4 = FrameCreater(master=self.master, width=22, height=1, side=tkinter.TOP)
			self.frame_creater4_list.append(frame_creater4)
			self.button_done_list.append(ButtonDone(id=idx, master=frame_creater4.frame, text_box_creater=self))
			self.button_cancel_list.append(ButtonCancel(id=idx, master=frame_creater4.frame, text_box_creater=self))

		self.button_add = ButtonAdd(master=self.master, text_box_creater=self)
