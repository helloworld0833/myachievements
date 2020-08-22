import tkinter

from frame import Frame
from text_box_creater import TextBoxCreater

window = tkinter.Tk(className='my board')

text_frame = Frame(master=window)
recent_frame = Frame(master=window)
random_frame = Frame(master=window)

TextBoxCreater(master=text_frame.frame, file_name='dashboard.txt', state='normal', assign_button=True)
TextBoxCreater(master=recent_frame.frame, file_name='1.txt', mode='recent')
TextBoxCreater(master=random_frame.frame, file_name='1.txt', mode='random')

window.mainloop()
