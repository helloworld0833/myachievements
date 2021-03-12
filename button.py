import tkinter
import datetime

from frame import Frame
from utilities import parser, deparser, remove_id

class Button(object):
	def __init__(self, master, text, window, width, height=1, side=tkinter.LEFT):
		self.window = window

		self.button = tkinter.Button(
				master = master,
    			text = text,
    			width = width,
			)

		self.button.pack(side=side, expand=True)

	def _refresh(self):
		self.window.refresh()

	def destroy(self):
		self.button.destroy()

class ButtonDone(Button):
	def __init__(self, id, master, text, text_box, window):
		self.id = id
		self.text_box = text_box

		super(ButtonDone, self).__init__(master=master, text=text, window=window, width=10, height=1)

		self.button.bind('<Button-1>', self._done)

	def _done(self, event):
		text = self.text_box.text_box.get('1.0', 'end')
		text_list = text.split('\n')
		while text_list and not text_list[-1]:
			text_list.pop()

		text_list = remove_id(text_list)

		item_done = text_list[self.id]
		text_list.pop(self.id)

		self.text_box.text_box.delete('{}.0'.format(self.id+1), '{}.end + 1 char'.format(self.id+1))

		button_frame = self.text_box.button_frame_list[self.id]
		button_frame.frame.pack_forget()

		self.text_box.button_frame_list.pop(self.id)
		self.text_box.button_done_list.pop(self.id)
		self.text_box.button_cancel_list.pop(self.id)

		for idx in range(self.id, len(self.text_box.button_done_list)):
			self.text_box.button_done_list[idx].id -= 1
			self.text_box.button_cancel_list[idx].id -= 1

		with open('dashboard.txt', 'ab+') as f:
			f.seek(0)
			with open('dashboard_backup.txt', 'w+') as f2:
				lines = parser(f.read())
				f2.write(''.join(deparser(lines)))

		with open('dashboard.txt', 'w+') as f:
			f.write('\n'.join(deparser(text_list))+'\n')

		now = datetime.datetime.now()

		with open('complete.txt', 'a') as f:
			f.write('{} {}/{}/{}\n'.format(''.join(deparser(item_done)), now.month, now.day, now.year))

		with open('backup.txt', 'a') as f:
			f.write('{} {}/{}/{}\n'.format(''.join(deparser(item_done)), now.month, now.day, now.year))

		self._refresh()

class ButtonCancel(Button):
	def __init__(self, id, master, text, text_box, window):
		self.id = id
		self.text_box = text_box

		super(ButtonCancel, self).__init__(master=master, text=text, window=window, width=10, height=1)

		self.button.bind('<Button-1>', self._cancel)

	def _cancel(self, event):
		text = self.text_box.text_box.get('1.0', 'end')
		text_list = text.split('\n')
		while text_list and not text_list[-1]:
			text_list.pop()

		text_list = remove_id(text_list)

		item_cancel = text_list[self.id]
		text_list.pop(self.id)

		self.text_box.text_box.delete('{}.0'.format(self.id+1), '{}.end + 1 char'.format(self.id+1))

		button_frame = self.text_box.button_frame_list[self.id]
		button_frame.frame.pack_forget()

		self.text_box.button_frame_list.pop(self.id)
		self.text_box.button_done_list.pop(self.id)
		self.text_box.button_cancel_list.pop(self.id)

		for idx in range(self.id, len(self.text_box.button_done_list)):
			self.text_box.button_done_list[idx].id -= 1
			self.text_box.button_cancel_list[idx].id -= 1

		with open('dashboard.txt', 'ab+') as f:
			f.seek(0)
			with open('dashboard_backup.txt', 'w+') as f2:
				lines = parser(f.read())
				f2.write(''.join(deparser(lines)))

		with open('dashboard.txt', 'w+') as f:
			f.write('\n'.join(deparser(text_list)))
			f.write('\n')

		self._refresh()

class ButtonAdd(Button):
	def __init__(self, master, text_box, window):
		self.text_box = text_box

		super(ButtonAdd, self).__init__(master=master, text='add', window=window, width=22, height=1, side=tkinter.TOP)

		self.button.bind('<Button-1>', self._add)

	def _add(self, event):
		self.text_box.text_box.insert('end', '\n')

		text = self.text_box.text_box.get('1.0', 'end')
		text_lines = text.split('\n')
		while text_lines and not text_lines[-1]:
			text_lines.pop()

		item_add = text_lines[-1]

		self.text_box.button_add.button.pack_forget()

		button_frame = Frame(master=self.text_box.master, width=22, height=1, side=tkinter.TOP)
		self.text_box.button_frame_list.append(button_frame)

		idx = len(self.text_box.button_done_list)
		self.text_box.button_done_list.append(ButtonDone(id=idx, master=button_frame.frame, text='{}.done'.format(idx+1), text_box=self.text_box, window=self.window))
		self.text_box.button_cancel_list.append(ButtonCancel(id=idx, master=button_frame.frame, text='{}.cancel'.format(idx+1), text_box=self.text_box, window=self.window))

		self.text_box.button_add = ButtonAdd(master=self.text_box.master, text_box=self.text_box, window=self.window)

		with open('dashboard.txt', 'a') as f:
			f.write('{}\n'.format(''.join(deparser([item_add]))))

		self._refresh()
