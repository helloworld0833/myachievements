import tkinter

from frame import Frame
from text_box import TextBox

window = tkinter.Tk(className='my board')

text_frame = Frame(master=window)
recent_frame = Frame(master=window)
random_frame = Frame(master=window)

TextBox(master=text_frame.frame, file_name='dashboard.txt', state='normal', assign_button=True)
TextBox(master=recent_frame.frame, file_name='1.txt', mode='recent')
TextBox(master=random_frame.frame, file_name='1.txt', mode='random')

window.mainloop()
