import tkinter

from frame_creater import FrameCreater
from text_box_creater import TextBoxCreater

window = tkinter.Tk(className='my board')

frame_creater1 = FrameCreater(master=window)
frame_creater2 = FrameCreater(master=window)
frame_creater3 = FrameCreater(master=window)

TextBoxCreater(master=frame_creater1.frame, file_name='dashboard.txt', state='normal', assign_button=True)
TextBoxCreater(master=frame_creater2.frame, file_name='1.txt', mode='recent')
TextBoxCreater(master=frame_creater3.frame, file_name='1.txt', mode='random')

window.mainloop()
