import tkinter
import datetime

from frame_creater import FrameCreater
from utilities import parser, deparser

class Button(object):
	def __init__(self, master, text, width, height=1, side=tkinter.LEFT):
		self.button = tkinter.Button(
				master = master,
    			text = text,
    			width = width,
			)

		self.button.pack(side=side, expand=True)

class ButtonDone(Button):
	def __init__(self, id, master, text_box_creater):
		self.id = id
		self.text_box_creater = text_box_creater

		super(ButtonDone, self).__init__(master=master, text='done', width=10, height=1)

		self.button.bind('<Button-1>', self._done)

	def _done(self, event):
		text = self.text_box_creater.text_box.get('1.0', 'end')
		text_list = text.split('\n')
		while text_list and not text_list[-1]:
			text_list.pop()

		item_done = text_list[self.id]
		text_list.pop(self.id)

		self.text_box_creater.text_box.delete('{}.0'.format(self.id+1), '{}.end + 1 char'.format(self.id+1))

		frame_creater4 = self.text_box_creater.frame_creater4_list[self.id]
		frame_creater4.frame.pack_forget()

		self.text_box_creater.frame_creater4_list.pop(self.id)
		self.text_box_creater.button_done_list.pop(self.id)
		self.text_box_creater.button_cancel_list.pop(self.id)

		for idx in range(self.id, len(self.text_box_creater.button_done_list)):
			self.text_box_creater.button_done_list[idx].id -= 1
			self.text_box_creater.button_cancel_list[idx].id -= 1

		with open('dashboard.txt', 'br') as f:
			with open('dashboard2.txt', 'w') as f2:
				lines = parser(f.read())
				f2.write(''.join(deparser(lines)))

		with open('dashboard.txt', 'w') as f:
			f.write('\n'.join(deparser(text_list))+'\n')

		now = datetime.datetime.now()

		with open('1.txt', 'a') as f:
			f.write('{} {}/{}/{}\n'.format(''.join(deparser([item_done])), now.month, now.day, now.year))

		with open('backup.txt', 'a') as f:
			f.write('{} {}/{}/{}\n'.format(''.join(deparser([item_done])), now.month, now.day, now.year))

class ButtonCancel(Button):
	def __init__(self, id, master, text_box_creater):
		self.id = id
		self.text_box_creater = text_box_creater

		super(ButtonCancel, self).__init__(master=master, text='cancel', width=10, height=1)

		self.button.bind('<Button-1>', self._cancel)

	def _cancel(self, event):
		text = self.text_box_creater.text_box.get('1.0', 'end')
		text_list = text.split('\n')
		while text_list and not text_list[-1]:
			text_list.pop()

		item_cancel = text_list[self.id]
		text_list.pop(self.id)

		self.text_box_creater.text_box.delete('{}.0'.format(self.id+1), '{}.end + 1 char'.format(self.id+1))

		frame_creater4 = self.text_box_creater.frame_creater4_list[self.id]
		frame_creater4.frame.pack_forget()

		self.text_box_creater.frame_creater4_list.pop(self.id)
		self.text_box_creater.button_done_list.pop(self.id)
		self.text_box_creater.button_cancel_list.pop(self.id)

		for idx in range(self.id, len(self.text_box_creater.button_done_list)):
			self.text_box_creater.button_done_list[idx].id -= 1
			self.text_box_creater.button_cancel_list[idx].id -= 1

		with open('dashboard.txt', 'br') as f:
			with open('dashboard2.txt', 'w') as f2:
				lines = parser(f.read())
				f2.write(''.join(deparser(lines)))

		with open('dashboard.txt', 'w') as f:
			f.write('\n'.join(deparser(text_list)))
			f.write('\n')

class ButtonAdd(Button):
	def __init__(self, master, text_box_creater):
		self.text_box_creater = text_box_creater

		super(ButtonAdd, self).__init__(master=master, text='add', width=22, height=1, side=tkinter.TOP)

		self.button.bind('<Button-1>', self._add)

	def _add(self, event):
		self.text_box_creater.text_box.insert('end', '\n')

		text = self.text_box_creater.text_box.get('1.0', 'end')
		text_lines = text.split('\n')
		while text_lines and not text_lines[-1]:
			text_lines.pop()

		item_add = text_lines[-1]

		self.text_box_creater.button_add.button.pack_forget()

		frame_creater4 = FrameCreater(master=self.text_box_creater.master, width=22, height=1, side=tkinter.TOP)
		self.text_box_creater.frame_creater4_list.append(frame_creater4)

		idx = len(self.text_box_creater.button_done_list)
		self.text_box_creater.button_done_list.append(ButtonDone(id=idx, master=frame_creater4.frame, text_box_creater=self.text_box_creater))
		self.text_box_creater.button_cancel_list.append(ButtonCancel(id=idx, master=frame_creater4.frame, text_box_creater=self.text_box_creater))

		self.text_box_creater.button_add = ButtonAdd(master=self.text_box_creater.master, text_box_creater=self.text_box_creater)

		with open('dashboard.txt', 'a') as f:
			f.write('{}\n'.format(deparser(item_add)))
